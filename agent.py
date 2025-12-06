import os
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from utils import Context, CareerAdvice, create_bot
from load_dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

SYSTEM_PROMPT = """You are an expert Academic Counseelor or Career Advisor.


You will be provided with either the prompt or his/her resume:

- prompt: User will provide his career details in bulleted points
- user_pdf: User will provide his resume in pdf format

Based on the above information, first you have to give him resume score out of 100 and then suggest improvements and projects that he can add it to the resume.
Suggestions should not exceeds more than 150 words
"""

class AgentBuilder:
    def __init__(self):
        self.model = create_bot()
        self.system_prompt = SYSTEM_PROMPT
    
    def agent(self):
        return create_agent(
            model=self.model,
            system_prompt=self.system_prompt,
            context_schema=Context,
            response_format=ToolStrategy(CareerAdvice),
        )

    def agent_response(self, user_input, config=None):
        agent = self.agent()
        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"configurable": {"thread_id": "1"}},
            context=Context(user_id="1")
        )
        final_response = response["structured_response"]
        return final_response


if __name__ == "__main__":
    user_input = input("Enter the input in 3 bulleted points")
    builder = AgentBuilder()
    response = builder.agent_response(user_input)
    print(response)