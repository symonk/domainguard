from fastapi.testclient import TestClient
from assertpy import assert_that
from http import HTTPStatus
from app import main
import json
import typing


def test_health_returns_uptime() -> typing.NoReturn:
    client = TestClient(main.app)
    response = client.get("/health")
    assert_that(response.status_code == HTTPStatus.OK)
    assert_that(body := json.loads(response.content)).is_type_of(dict).contains_key(
        "uptime"
    )
    assert_that(body["uptime"]).matches(r"\d+ seconds")
