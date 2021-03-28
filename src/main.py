import logging.config
import pandas as pd
import yaml

logger = logging.getLogger(__name__)

DEALS_HISTORY_FILE_PATH = "../resources/history_files/sg_20210306_history_export.csv"
LOGGING_CONF_FILE_PATH = "../logging.yml"


def main():
    df = pd.read_csv(DEALS_HISTORY_FILE_PATH)
    logger.debug(df)
    pass




if __name__ == '__main__':
    with open(LOGGING_CONF_FILE_PATH, "r") as conf:
        logger_config = yaml.load(conf, Loader=yaml.FullLoader)
        logging.config.dictConfig(logger_config)
    main()
