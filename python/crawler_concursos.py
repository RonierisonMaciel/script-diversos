import requests
from bs4 import BeautifulSoup
import json
import re
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

BASE_URL = "https://www.pciconcursos.com.br/concursos/nordeste/"


def fetch_webpage(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def extract_job_details(div):
    title = div.find('a').get_text()
    location = div.find('div', class_='cc').get_text()
    details_div = div.find('div', class_='cd')
    position_spans = details_div.find_all('span')
    education = position_spans[-1].get_text() if position_spans else None
    details_text = details_div.get_text()
    match = re.search(r'(\d+ vagas até R\$ [\d\.,]+)(.*)', details_text)
    vacancies_salary = match.group(1) if match else None
    position = match.group(2).replace(education, '').strip() if match else None

    return title, location, vacancies_salary, position, education


def is_professor_position(position, education):
    if not position or not education:
        return False
    return "Professor" in position and "Superior" in education.split(" / ")


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    soup = fetch_webpage(BASE_URL)
    job_listings = []

    for div in soup.find_all('div', {'class': ['fa', 'na']}):
        title, location, vacancies_salary, position, education = extract_job_details(div)

        if is_professor_position(position, education):
            deadline = div.find('div', class_='ce').get_text()
            link = div.find('a')['href']

            job_listings.append({
                "Título": title,
                "Localização": location,
                "Vaga e Salário": vacancies_salary,
                "Vaga": position,
                "Nível": education,
                "Inscrições até": deadline,
                "Link": link
            })

    final_data = {
        "total_listings": len(job_listings),
        "listings": job_listings
    }

    save_to_json(final_data, 'docente_professor.json')
    print(f"Arquivo 'docente_professor.json' salvo com sucesso! Total de listagens: {len(job_listings)}")


if __name__ == "__main__":
    main()
