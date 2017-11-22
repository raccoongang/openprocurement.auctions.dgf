# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, time, date
from openprocurement.api.models import (TZ)


MINIMAL_EXPOSITION_PERIOD = timedelta(days=7)
MINIMAL_EXPOSITION_REQUIRED_FROM = datetime(2017, 11, 17, tzinfo=TZ)
MINIMAL_PERIOD_FROM_ENQUIRY_END = timedelta(days=5)
ENQUIRY_END_EDITING_AND_VALIDATION_REQUIRED_FROM = datetime(2017, 11, 21, tzinfo=TZ)
