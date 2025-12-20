darkness = {
    "simple_selector": {
        # Esqueleto totalmente oscuro (secondary)
        "body":   {"color": "white", "background-color": "secondary"},
        "header": {"color": "white", "background-color": "secondary"},
        "footer": {"color": "white", "background-color": "secondary"},
        
        # Títulos en color claro acentuado
        "text_htags": {"color": "quaternary"},
        "text_tags": {"color": "white"},
        
        # Los contenedores de bloques usan un fondo ligeramente diferente (principal)
        "block_tags": {"background-color": "principal", "color": "white"},
        
        "button": {"color": "black", "background-color": "quaternary"}
    },

    "doble_selector": {
        "header>a": {"color":"quaternary"},
        "footer>a": {"color": "quaternary"},
        # El texto en los bloques mantiene el blanco, solo cambia sutilmente el fondo
        "block_tags>text_tags": {"color": "white"} 
    },

    "triple_selector": {}
}