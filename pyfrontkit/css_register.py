# Copyright (c) 2025 Eduardo Antonio Ferrera Rodríguez
# SPDX-License-Identifier: MIT

from typing import Any

class CSSRegistry:
    """
    Manages CSS selectors in memory. Filters out empty rules, 
    cleans up default placeholders, and minifies output for production.
    """
    _tags = set()
    _ids = set()
    _classes = set()
    _cascades = set() 

    _VOID_TAGS_TO_EXCLUDE = {
        "hr", "link", "source", "param", "track", "wbr", "base"
    }

    @classmethod
    def _get_child_tag(cls, child: Any) -> str | None:
        if hasattr(child, "tag"):
            return getattr(child, "tag")
        return None

    @classmethod
    def _register_cascades_by_tag(cls, block):
        parent_tag = block.tag
        for child in getattr(block, "children", []):
            child_tag = cls._get_child_tag(child)
            if child_tag:
                selector_1 = f"{parent_tag} > {child_tag}" if parent_tag else child_tag
                cls._cascades.add(selector_1)
                if hasattr(child, "children"):
                    for grandchild in child.children:
                        grandchild_tag = cls._get_child_tag(grandchild)
                        if grandchild_tag:
                            selector_2 = f"{parent_tag} > {child_tag} > {grandchild_tag}" if parent_tag else f"{child_tag} > {grandchild_tag}"
                            cls._cascades.add(selector_2)

    @classmethod
    def register_single_selectors(cls, element):
        attrs = getattr(element, "attrs", {})
        element_id = attrs.get("id")
        if hasattr(element, "tag") and element.tag:
            if element.tag not in cls._VOID_TAGS_TO_EXCLUDE:
                cls._tags.add(element.tag)
        if element_id:
            cls._ids.add(element_id)
        classes = attrs.get("class")
        if classes:
            for cls_name in str(classes).split():
                cls._classes.add(cls_name)

    @classmethod
    def register_block(cls, block):
        cls.register_single_selectors(block)
        block_id = getattr(block, "attrs", {}).get("id")
        children = list(getattr(block, "children", []))
        if block_id:
            for child in children:
                child_tag = getattr(child, "tag", None)
                if child_tag:
                    cls._cascades.add(f"#{block_id} > {child_tag}")
        cls._register_cascades_by_tag(block)
        for child in children:
            if hasattr(child, "children"):
                cls.register_block(child)
        for ctn_item in getattr(block, "content_items", []):
            cls.register_single_selectors(ctn_item)

    @classmethod
    def generate_css(cls) -> str:
        """
        Returns a minified CSS string containing only selectors with active rules.
        Removes internal newlines and empty blocks.
        """
        try:
            from .style_manager import CSS_RULES_STYLE
        except ImportError:
            CSS_RULES_STYLE = []

        # 1. Map selectors and CLEAN internal content
        active_styles = {}
        for rule_dict in CSS_RULES_STYLE:
            for selector, data in rule_dict.items():
                raw_content = data.get("css", "").strip()
                if raw_content:
                    # Minification: Remove extra newlines and spaces within the rules
                    # This converts multi-line CSS into a clean single-line rule
                    clean_lines = [line.strip() for line in raw_content.splitlines() if line.strip()]
                    active_styles[selector] = " ".join(clean_lines)

        lines = []
        # 2. Build the final output
        all_selectors = (
            list(cls._tags) + 
            [f"#{i}" for i in cls._ids] + 
            [f".{c}" for c in cls._classes] + 
            list(cls._cascades)
        )

        for selector in sorted(set(all_selectors)):
            if selector in active_styles:
                # Format: selector { property: value; property: value; }
                lines.append(f"{selector} {{ {active_styles[selector]} }}")

        return "\n".join(lines)

    @classmethod
    def clear_registry(cls):
        """Wipes memory for the next request."""
        cls._tags.clear()
        cls._ids.clear()
        cls._classes.clear()
        cls._cascades.clear()