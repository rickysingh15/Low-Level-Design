
from logger import Logger
from logLevel import LogLevel
from concreteOutput import FileOutputStrategy, ConsoleOutputStrategy, DatabaseOutputStrategy
from concreteOutputFormatter import JsonOutputFormatter, PlainTextOutputFormatter

logger = Logger(
    min_log_level=LogLevel.INFO.value,
    output_strategies=[ConsoleOutputStrategy(PlainTextOutputFormatter()), FileOutputStrategy("file_path", JsonOutputFormatter())]
)


logger.warning("error occured while adding two integers")


# logger.info("Database connection established")
# logger.debug("api params received are ------ ")

# logger.fatal("fatal error occured at line 50")