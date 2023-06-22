from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    # create soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()
    for h in soup.findAll('h3', class_= 'gs-c-promo-heading__title'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)
    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    term_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            term_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <----------------"{term}')
        else:
            print(f'{i}: {headline.capitalize()} ')

    print('-'* 40)
    if term_found:
        print(f'"{term}" was mentioned {term_found} times')
        print('-' * 40)

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}:  {headline.capitalize()}')

    else:
        print(f'No matches found for {term}')
        print('-' * 40)

def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)
    user_input: str = 'spotify'
    check_headlines(headlines, user_input)



if __name__ == '__main__':
    main()
