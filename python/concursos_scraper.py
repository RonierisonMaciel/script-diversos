import requests
from bs4 import BeautifulSoup
import json
import re
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

URL = "cole_aqui_a_url_do_pci_concursos"

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

job_listings = []

# Considerando divs com classe 'fa' e 'na'
for div in soup.find_all('div', {'class': ['fa', 'na']}):
    title = div.find('a').get_text()
    location = div.find('div', class_='cc').get_text()
    
    details_div = div.find('div', class_='cd')
    
    position_spans = details_div.find_all('span')
    education = position_spans[-1].get_text() if position_spans else None
    
    details_text = details_div.get_text()
    match = re.search(r'(\d+ vagas até R\$ [\d\.,]+)(.*)', details_text)
    if match:
        vacancies_salary = match.group(1)
        position = match.group(2).replace(education, '').strip()
    

    if "Professor" in position:
        education_levels = education.split(" / ")
        if "Superior" in education_levels:
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

count = len(job_listings)

final_data = {
    "total_listings": count,
    "listings": job_listings
}

with open('docente_professor.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)

print(f"Arquivo 'docente_professor.json' salvo com sucesso! Total de listagens: {count}")
