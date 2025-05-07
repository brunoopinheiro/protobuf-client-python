from http import HTTPStatus
from logging import getLogger
from typing import TypeVar

from betterproto import Message
from requests import get, post, put, delete, Response


ProtoModel = TypeVar("ProtoModel", bound=Message)


logger = getLogger(__name__)


def get_proto(
    proto_model: ProtoModel,
    url: str,
) -> ProtoModel:
    """Get a proto model from the server.

    Args:
        proto_model (ProtoModel): The proto model to use.
        url (str): The url to get the proto model from.
        qargs (Optional[str], optional): Optional query parameters to be added
            to the url. Defaults to None.

    Returns:
        ProtoModel: _description_
    """
    response: Response = get(url)

    logger_msg = f"GET {url} - {response.status_code}"

    if response.status_code == HTTPStatus.OK:
        decoded = proto_model().parse(response.content)
        logger.info(f"{logger_msg} - {decoded}")
        return decoded
    else:
        logger.error(f"{logger_msg} - {response.text}")


def post_proto(
    url: str,
    proto_data: ProtoModel,
    proto_model: ProtoModel,
) -> Response:
    """Post a proto model to the server.

    Args:
        url (str): The url to post the proto model to.
        proto_data (ProtoModel): The proto model to post.

    Returns:
        Response: The response from the server.
    """
    response: Response = post(url, data=proto_data.SerializeToString())

    logger_msg = f"POST {url} - {response.status_code}"

    if (
        response.status_code == HTTPStatus.OK
        or response.status_code == HTTPStatus.CREATED
    ):
        decoded = proto_model().parse(response.content)
        logger.info(f"{logger_msg} - {decoded}")
        return decoded
    else:
        logger.error(f"{logger_msg} - {response.text}")

    return response


def put_proto(
    url: str,
    proto_data: ProtoModel,
    proto_model: ProtoModel,
) -> Response:
    """Put a proto model to the server.

    Args:
        url (str): The url to put the proto model to.
        proto_data (ProtoModel): The proto model to put.

    Returns:
        Response: The response from the server.
    """
    response: Response = put(url, data=proto_data.SerializeToString())

    logger_msg = f"PUT {url} - {response.status_code}"

    if response.status_code == HTTPStatus.OK:
        decoded = proto_model().parse(response.content)
        logger.info(f"{logger_msg} - {decoded}")
        return decoded
    else:
        logger.error(f"{logger_msg} - {response.text}")

    return response


def delete_proto(
    url: str,
) -> Response:
    """Delete a proto model from the server.

    Args:
        url (str): The url to delete the proto model from.

    Returns:
        Response: The response from the server.
    """
    response: Response = delete(url)

    logger_msg = f"DELETE {url} - {response.status_code}"

    if response.status_code == HTTPStatus.OK:
        logger.info(f"{logger_msg} - {response.text}")
        return response
    else:
        logger.error(f"{logger_msg} - {response.text}")

    return response
