import datetime as dt

UTC = dt.timezone.utc
EPOCH = dt.datetime.utcfromtimestamp(0).replace(tzinfo=UTC)


def get_local_tz():
    """get local timezone"""
    now = dt.datetime.now()
    local_now = now.astimezone()
    return local_now.tzinfo


def utcnow() -> dt.datetime:
    """datetime.datetime.utcnow() replacement with timezone"""
    return dt.datetime.now(dt.timezone.utc)


def ts2utc_dt(ts: int):
    """timestamp to datetime, with utc timezone

    >>> dt = ts2utc_dt(1499436402)
    >>> dt.tzname(), dt.hour
    ('UTC', 14)
    """
    return dt.datetime.utcfromtimestamp(ts).replace(tzinfo=dt.timezone.utc)
