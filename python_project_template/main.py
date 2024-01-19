import json
import os
from tests import test_version

os.environ["TZ"] = "UTC"


def foo() -> str:
    json.dumps({"foo": "bar"})
    # mypy issue here
    return 5
