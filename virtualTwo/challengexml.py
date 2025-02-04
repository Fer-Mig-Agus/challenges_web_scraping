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

    # Definir el namespace correcto
    ns = {'news': 'http://www.google.com/schemas/sitemap-news/1.1'}
    
    # Encontrar todas las noticias
    new_items = tree.findall('.//news:news', namespaces=ns)
    
    result = []
    
    for new in new_items:
        title = new.find('.//news:title', namespaces=ns)
        publication_date = new.find('.//news:publication_date', namespaces=ns)
        
        result.append({
            'title': title.text if title is not None else None,
            'publication_date': publication_date.text if publication_date is not None else None
        })
    
    return result

if __name__ == '__main__':
    url = 'https://www.diariopanorama.com/rss/news?token=llo387fg12fu54ks'
    data = get_data(url)
    
    for new in data:
        print(new)
