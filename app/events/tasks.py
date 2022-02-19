from celery.decorators import task
from celery.utils.log import get_task_logger

from events.serializers import EventSerializer


logger = get_task_logger(__name__)


@task(name="save_event_task")
def save_event_task(data):
    """Saves event data in the db"""
    logger.info("Save new event: %s", str(data))
    serializer = EventSerializer(data=data)
    try:
        if serializer.is_valid():
            serializer.save()
        else:
            logger.error("Invalid event data %s", str(data))
    except Exception as e:
        logger.error("Unexpected error %s", str(e))
    return
