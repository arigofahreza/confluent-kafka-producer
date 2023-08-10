import json
import os

import pandas as pd
import typer
from loguru import logger

from confluent_kafka_producer.src.config.kafka import producer, KafkaConfig, create_topic
from timeit import default_timer as timer

current_dir = os.getcwd()

app = typer.Typer()


@app.command()
def produce_message():
    ProducerService().read_file()


class ProducerService:
    def __init__(self):
        self._producer_client = producer()
        self._filepath: str = f'{current_dir}\\confluent_kafka_producer\\src\\resource\\Size file.xlsx'
        self._topic: str = KafkaConfig().KAFKA_PRODUCER_TOPIC
        create_topic()

    def produce(self, message: str) -> None:
        self._producer_client.produce(self._topic, message)
        self._producer_client.poll(1)

    def read_file(self) -> None:
        df = pd.read_excel(self._filepath)
        for index, row in df.iterrows():
            now = timer()
            self.produce(json.dumps(row.to_dict()))
            logger.info(f'[>>] produce message to {self._topic}')
            logger.info(f'[!!] execution time = {timer() - now}')
        logger.complete()
