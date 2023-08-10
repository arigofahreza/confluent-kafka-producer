from pydantic.v1 import BaseSettings


class KafkaConfig(BaseSettings):
    KAFKA_BOOTSTRAP: str
    KAFKA_PRODUCER_TOPIC: str
    KAFKA_GROUP_ID: str
    KAFKA_AUTO_OFFSET_RESET: str
    KAFKA_MAX_POLL_RECORDS: str