import base64
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from utils import create_bot

class Model:
    def __init__(self):
        self.model = create_bot()
        self.text = "This is my resume. Give me some suggestions to improve it in less than 150 words."

    def model_response(self, pdf_base):

        message = HumanMessage(
            content=[
                {"type": "text", "text": self.text},
                {
                    "type": "file",
                    "base64": pdf_base,
                },
            ]
        )
        return self.model.invoke([message]).text