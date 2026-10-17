def get_disk_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    return "NORMAL"


def get_memory_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    return "NORMAL"
