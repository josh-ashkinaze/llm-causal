import os
import logging
import requests
from bs4 import BeautifulSoup
from chatgpt_wrapper import ChatGPT
import csv

# Set up logging
log_file = os.path.splitext(os.path.basename(__file__))[0] + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s')

gpt_prompt = """I will give you HTML content for a study. 
Return:
- Authors: Authors of study 
- Date: Date of study
- Title: Title of study 
- Abstract: Abstract of study 
- Hypotheses: Hypotheses of the study (e.g: H1: Hypothes1, H2: Hypothesis2
- Experimental conditions: Conditions of experiment 
- Distinct factors: Number of experimental factors
- DVs: Dependent variables
- Results: Which hypotheses were supported (e.g: H1:Supported, H2:Not supported)

If any of these fields are not available, return "NA" for that specific field. 
###"""


def main():
    bot = ChatGPT()
    tess_studies = "https://www.tessexperiments.org/paststudies"
    response = requests.get(tess_studies)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [link['href'] for link in soup.find_all('a', href=True)]
    study_links = ["https://www.tessexperiments.org" + link.replace("./study", "/study") for link in links if 'study' in link]
    logging.info(f"Found {len(study_links)} study links")
    with open('tess.csv', mode='w', newline='') as csv_file:
        fieldnames = ['link', 'response']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i, link in enumerate(study_links, 1):
            soup = BeautifulSoup(requests.get(link).content, 'html.parser')
            response = bot.ask(f"""{gpt_prompt}\n###{soup.text}""")
            writer.writerow({'link': link, 'response': response})
            logging.info(f"Processed study {i} out of {len(study_links)} at link {link}")

if __name__ == "__main__":
    main()
