from dotenv import load_dotenv
load_dotenv()

from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatMistralAI(model="mistral-small")
tool_tavily = TavilySearch(max_results = 5)

prompt_template = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Summarize the given news into short and clear bullet points.

{news}
"""
)

chain = prompt_template | model | StrOutputParser()

def get_news_summary(topic):

    news_result = tool_tavily.run(topic)

    final_result = chain.invoke(
        {
            "news": news_result
        }
    )

    return final_result

#for terminal
# topic = input("Enter news topic: ")

# result = get_news_summary(topic)

# print(result)