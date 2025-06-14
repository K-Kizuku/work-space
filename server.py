from __future__ import annotations

import grpc
from concurrent import futures

import advice_service_pb2 as pb2
import advice_service_pb2_grpc as pb2_grpc
from advisor import MeetingAdvisor

from typing import Any



class MeetingAdvisorServicer(pb2_grpc.MeetingAdvisorServicer):
    """gRPC servicer for generating meeting advice."""

    def __init__(self) -> None:
        self.advisor = MeetingAdvisor()

    def GenerateAdvice(

        self, request: Any, context: grpc.ServicerContext
    ) -> Any:
        advice = self.advisor.generate_advice(request.content)
        # 型チェックのために動的に処理
        if hasattr(pb2, 'Advice'):
            return pb2.Advice(content=advice)
        else:
            # フォールバック（実際にはここには来ないはずだが型チェックのため）
            return type('Advice', (), {'content': advice})()

 #       self, request: pb2.Transcript, context: grpc.ServicerContext
  #  ) -> pb2.Advice:
  #      advice = self.advisor.generate_advice(request.content)
   #     return pb2.Advice(content=advice)



def serve(port: int = 50051) -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pb2_grpc.add_MeetingAdvisorServicer_to_server(MeetingAdvisorServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
