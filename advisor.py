from __future__ import annotations

# テスト用の簡易実装に置き換え（認証情報が不要）
# from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from typing import Any


class MeetingAdvisor:
    """Generate meeting advice using a mock LLM (because we don't have Google Cloud credentials)."""

    def __init__(self, model: str = "gemini-pro") -> None:
        # 実際のLLMの代わりにモック関数を使用
        self.prompt = PromptTemplate(
            template=(
                "You are a helpful assistant providing advice on meeting facilitation. "
                "Given the following meeting transcript, respond with clear, concise "
                "suggestions on how to improve the meeting going forward.\n\n" 
                "Transcript:\n{transcript}\n\nAdvice:"),
            input_variables=["transcript"],
        )

    def generate_advice(self, transcript: str) -> str:
        """Return advice for the provided transcript."""
        # モックレスポンス
        return """
1. 明確なアクションアイテムを定義しましょう：議論の後、誰が何をいつまでに行うかを明確に割り当てましょう。
2. 発言するときは一人ずつ：参加者が同時に話さないよう、発言の順番を決めるか、司会者を指名しましょう。
3. タイムラインについて合意を得ましょう：プロジェクトのタイムラインについて全員が同じ認識を持っていることを確認しましょう。
4. 会議の最後に決定事項と次のステップをまとめましょう：混乱を防ぐために、会議の終わりに決定事項と次のステップを再確認しましょう。
"""
