"""
Ejercicio para superar el challenge

Objetivo:
Extraer productos de una tienda online ficticia que tiene datos tanto en HTML como en JavaScript dinámico.
Requisitos del ejercicio

    Extraer el nombre del producto y su precio usando XPath.
    Extraer el enlace del producto usando Regex desde una etiqueta <script> (como si estuviera en un JSON dentro del HTML).
    Guardar los datos en un DataFrame de pandas.
"""

html = """
<div class="product">
    <h2 class="name">Monitor 24 pulgadas</h2>
    <span class="price">$199.99</span>
</div>

<div class="product">
    <h2 class="name">Teclado Mecánico RGB</h2>
    <span class="price">$89.99</span>
</div>

<script>
    var products = [
        {"name": "Monitor 24 pulgadas", "url": "https://tienda.com/producto1"},
        {"name": "Teclado Mecánico RGB", "url": "https://tienda.com/producto2"}
    ];
</script>
"""
