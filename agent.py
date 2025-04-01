from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI

load_dotenv()

agent = create_csv_agent(ChatOpenAI(temperature=0),
                         "freelancer_earnings_bd.csv",
                         allow_dangerous_code=True,
                         verbose=True)


def get_csv_agent_response(prompt: str) -> str:
    response = agent.invoke(prompt)

    return response["output"]
