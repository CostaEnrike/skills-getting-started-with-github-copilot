from copy import deepcopy

import pytest

from src import app


@pytest.fixture(autouse=True)
def restore_activities():
    original_activities = deepcopy(app.activities)
    try:
        yield
    finally:
        app.activities.clear()
        app.activities.update(original_activities)
