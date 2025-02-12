from datetime import datetime
import pytz


def prebuilt_get_current_datetime(timezone: str) -> str:
    try:
        tz = pytz.timezone(timezone)
        return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    except pytz.UnknownTimeZoneError:
        return "Invalid timezone"
