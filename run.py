from app import main
from app.app_logger import LoggerConfig

LoggerConfig().setup_logging()


if __name__ == "__main__":
    main()
    
