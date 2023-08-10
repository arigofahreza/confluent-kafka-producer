from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic, Producer
from loguru import logger
from pydantic.v1 import BaseSettings


class KafkaConfig(BaseSettings):
    KAFKA_BOOTSTRAP: str
    KAFKA_PRODUCER_TOPIC: str
    KAFKA_PARTITIONS: int
    KAFKA_REPLICATIONS: int

    class Config:
        env_file = ".env"


def create_topic() -> None:
    kafka_config = KafkaConfig()
    admin_client = AdminClient({'bootstrap.servers': kafka_config.KAFKA_BOOTSTRAP})
    admin_client.create_topics([NewTopic(kafka_config.KAFKA_PRODUCER_TOPIC,
                                         num_partitions=kafka_config.KAFKA_PARTITIONS,
                                         replication_factor=kafka_config.KAFKA_REPLICATIONS)])
    logger.info(f'[!!] Success creating topic: {kafka_config.KAFKA_PRODUCER_TOPIC}')


def producer() -> Producer:
    kafka_config = KafkaConfig()
    return Producer({'bootstrap.servers': kafka_config.KAFKA_BOOTSTRAP})
