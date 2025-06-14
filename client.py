import grpc

import advice_service_pb2 as pb2
import advice_service_pb2_grpc as pb2_grpc


def run() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = pb2_grpc.MeetingAdvisorStub(channel)
    transcript = (
        "Yesterday we discussed project timelines but did not assign any action items. "
        "Several participants spoke over each other."
    )
    response = stub.GenerateAdvice(pb2.Transcript(content=transcript))  # type: ignore[attr-defined]
    print("Advice:\n", response.content)


if __name__ == "__main__":
    run()
