from __future__ import annotations

from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from typing import Any


class MeetingAdvisor:
    """Generate meeting advice using VertexAI via LangChain."""

    def __init__(self, model: str = "gemini-pro") -> None:
        self.llm = VertexAI(model_name=model)
        self.prompt = PromptTemplate(
            template=(
                "You are a helpful assistant providing advice on meeting facilitation. "
                "Given the following meeting transcript, respond with clear, concise "
                "suggestions on how to improve the meeting going forward.\n\n" 
                "Transcript:\n{transcript}\n\nAdvice:"),
            input_variables=["transcript"],
        )
        self.chain: Runnable[[str], str] = self.prompt | self.llm | StrOutputParser()

    def generate_advice(self, transcript: str) -> str:
        """Return advice for the provided transcript."""
        return self.chain.invoke({"transcript": transcript})
