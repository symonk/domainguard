from fastapi.testclient import TestClient
from assertpy import assert_that
from http import HTTPStatus
from app import main
import json
import typing

def test_analyse_returns_200_ok() -> typing.NoReturn:
    client = TestClient(main.app)
    response = client.get("/health")
    assert_that(response.status_code == HTTPStatus.OK)
    body = json.loads(response.content)
    assert_that(body).contains_key("uptime")
    assert_that(body["uptime"]).matches(r"\d+ seconds")
