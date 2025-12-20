mono_accent = {
    "simple_selector": {
        
        "body":   {"color": "black", "background-color": "quaternary"},
        "header": {"color": "black", "background-color": "quaternary"},
        "footer": {"color": "black", "background-color": "quaternary"},
        
        "text_htags": {"color": "principal"},
        "text_tags": {"color": "black"},
        
        
        "block_tags": {"background-color": "tertiary", "color": "black"},
        
        "button": {"color": "white", "background-color": "principal"}
    },

    "doble_selector": {
        "header>text_tags": {"color":"black"},
        "footer>text_tags": {"color": "black"},
        
        "block_tags>text_htags": {"color": "secondary"}
    },

    "triple_selector": {
        
        "block_tags>p": {"color": "principal"}
    }
}