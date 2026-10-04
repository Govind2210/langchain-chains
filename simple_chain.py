from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    base_url=os.getenv("OPENAI_COMPAT_BASE_URL"),
    api_key=os.getenv("OPENAI_COMPAT_API_KEY"),
    model=os.getenv("OPENAI_COMPAT_MODEL"),
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()