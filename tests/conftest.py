import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "http://host.docker.internal")