import logging
import sys
import io


class LoggerConfig:
    """Configura logging para ver errores."""
    
    def setup_logging(self):
        """Configura el logger con formato y nivel de logging."""    
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            handlers=[
                logging.StreamHandler(stream=sys.stdout),
            ]
        )
     
        # Configuración adicional para la consola en Windows
        if sys.platform == "win32":
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        
        logger = logging.getLogger(__name__)
        
        return logger