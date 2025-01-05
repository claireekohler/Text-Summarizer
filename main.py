#import necessary modules from the Text-Summarizer package
#error handling for import errors
try:
    from textSummarizer.custom_logging._init_ import logger
    logger.info("Logger imported successfully!")
except ImportError as e:
    print("ImportError occurred:", e)
    import sys
    print("sys.path:", sys.path)
