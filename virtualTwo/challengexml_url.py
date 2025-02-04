import requests
from rich import print
from lxml import etree

def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    
    # Parsear el XML correctamente
    tree = etree.XML(response.content)

    # Definir los dos namespaces
    ns = {
        'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9',
        'news': 'http://www.google.com/schemas/sitemap-news/0.9'
    }
    
    # Encontrar todas las noticias dentro de <url>
    news_items = tree.findall('.//sitemap:url', namespaces=ns)

    if not news_items:
        print("[red]No se encontraron noticias en el XML.[/red]")
        return []

    print(f"[green]Total de noticias encontradas: {len(news_items)}[/green]")

    result = []
    
    for item in news_items:
        # Extraer la URL de la noticia
        url = item.find('sitemap:loc', namespaces=ns)
        news_data = item.find('news:news', namespaces=ns)
        
        if url is None:
            print("[yellow]Advertencia: No se encontró la URL para un elemento.[/yellow]")
        
        if news_data is None:
            print("[yellow]Advertencia: No se encontraron datos de noticia para un elemento.[/yellow]")
            continue  # Si no hay datos de noticia, pasa al siguiente

        title = news_data.find('news:title', namespaces=ns)
        publication_date = news_data.find('news:publication_date', namespaces=ns)
        
        result.append({
            'url': url.text if url is not None else "Sin URL",
            'title': title.text if title is not None else "Sin título",
            'publication_date': publication_date.text if publication_date is not None else "Sin fecha"
        })
    
    return result

if __name__ == '__main__':
    url = 'https://www.diariopanorama.com/rss/news?token=llo387fg12fu54ks'
    data = get_data(url)
    
    if not data:
        print("[red]No se encontraron datos de noticias para imprimir.[/red]")
    else:
        for new in data:
            print(new)
