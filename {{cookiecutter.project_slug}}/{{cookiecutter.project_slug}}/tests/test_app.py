import pytest

from {{cookiecutter.project_slug}}.app import do_work

pytestmark = pytest.mark.asyncio


async def test_main():
    assert True


async def test_do_work(caplog):
    await do_work()
    assert "Job's Done!" in caplog.text
