"""
Configuration file for API & data settings
"""
from os import getenv

# FastAPI settings
TIME_SERIES_HOURS = 48
UNIT = "metric"
OUTPUT = "json"

# Literal values to be fetched from dataseries
VALUES = ["cloudcover", "temp2m"]
