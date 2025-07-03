from typing import Optional
import logging


class LoggerConfig:
    """Configura logging para ver errores."""
    
    def setup_logging(self):
        """Configura el logger con formato y nivel de logging."""    
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        logger = logging.getLogger(__name__)
        return logger