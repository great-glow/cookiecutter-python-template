import sys

from loguru import logger

from {{cookiecutter.project_slug}}.config import settings


async def setup_logger() -> None:
    logger.remove()
    if settings.is_debug:
        level = 'DEBUG'
        diagnose = True
    else:
        level = 'INFO'
        diagnose = False
    logger.add(
        sys.stdout,
        level=level,
        diagnose=diagnose,
    )
