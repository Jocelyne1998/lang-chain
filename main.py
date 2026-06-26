from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from icebreaker!")
    information = """
    Born in Surabaya, Indonesia, to restaurateur parents, Reynold Poernomo grew up in a world surrounded by passionate and talented cooks.

Moving to Australia at age four, Reynold watched on as his parents worked in hospitality and his two elder brothers entered the industry. His family were firm that they didn’t want their youngest son to pursue a career in the industry, knowing it can be tough.

But Reynold had a passion for food and worked on his skills, cooking after school and picking up tips from his mum, from cookbooks and online. He also cooked for girlfriend Sarah, trying to impress her with his creativity.

Reynold continued to pester both his mum and eldest brother Ronald to be allowed to help in the family business, Sydney patisserie Artplate. Eventually they relented and he juggled a casual role as a delivery driver and kitchen hand with his full-time studies.
Since bowing out of the seventh season of MasterChef Australia in fourth place, Sydney’s Reynold Poernomo has gone onto become one of the most successful alumni of the highly competitive show.

Shortly after he finished, he joined forces with his brothers to launch KOI Dessert Bar in 2016. The successful venture featured innovative and creative desserts, and the family has now expanded with KOI Dessert Kitchen, Monkey’s Corner and TiNi Artisan Bakehouse.

Alongside his burgeoning businesses, Reynold was also named a finalist in the Gault & Millau Pastry Chef of the Year awards in 2017, was listed in Forbes Asia’s 30 under 30 the same year, appeared on the fifth season of MasterChef Indonesia as a guest judge, and hosted a TEDx talk
    """
    sumary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=sumary_template
    )

    #llm = ChatOpenAI(model="gpt-5", temperature=0)
    Sllm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()

