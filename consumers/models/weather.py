"""Contains functionality related to Weather"""
import logging
import json

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        data = json.loads(message.value())
        self.temperature = data.get("temperature")
        self.status = data.get("status")
        logger.info("weather process_message was processed")
