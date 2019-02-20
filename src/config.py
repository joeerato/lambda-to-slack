"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SLACK_URL = os.getenv('https://hooks.slack.com/services/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')
