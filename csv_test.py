from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

agent = create_csv_agent(OpenAI(temperature=0),
                         "./csv_doc/diabetes_prediction_dataset.csv",
                         verbose=True,
                         )
agent.run("how many rows?")