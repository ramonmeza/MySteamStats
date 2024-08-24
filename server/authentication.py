from fasthtml.common import RedirectResponse, Request
from urllib.parse import urlencode
from urllib.request import urlopen
import re

from .toasts import set_toast


def user_auth_before(request: Request, session):
    # authentication method, which allows access based on whether the auth parameter is set in the session
    auth = request.scope["auth"] = session.get("auth", None)

    if not auth:
        set_toast(session, "error", "You must sign in!")
        return RedirectResponse(
            "/signin",
            status_code=303,
        )


class SteamAuth:
    PROVIDER: str = "https://steamcommunity.com/openid/login"

    @staticmethod
    def authorize(callback_url: str):
        auth_parameters: dict = {
            "openid.ns": "http://specs.openid.net/auth/2.0",
            "openid.mode": "checkid_setup",
            "openid.return_to": callback_url,
            "openid.realm": callback_url,
            "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select",
            "openid.claimed_id": "http://specs.openid.net/auth/2.0/identifier_select",
        }
        resp = RedirectResponse(
            url=f"{SteamAuth.PROVIDER}?{urlencode(auth_parameters)}",
            status_code=303,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return resp

    @staticmethod
    def validate_authorization(request: Request) -> str | None:
        data = request.query_params

        validation_args = {
            "openid.assoc_handle": data["openid.assoc_handle"],
            "openid.signed": data["openid.signed"],
            "openid.sig": data["openid.sig"],
            "openid.ns": data["openid.ns"],
        }

        signed_args = data["openid.signed"].split(",")
        for arg in signed_args:
            key = f"openid.{arg}"
            if data[key] not in validation_args:
                validation_args[key] = data[key]

        validation_args["openid.mode"] = "check_authentication"

        parsed_args = urlencode(validation_args).encode("utf-8")

        with urlopen(SteamAuth.PROVIDER, parsed_args) as req:
            resp = req.read().decode("utf-8")

        if re.search("is_valid:true", resp):
            matched_id = re.search(
                "https://steamcommunity.com/openid/id/(\d+)", data["openid.claimed_id"]
            )
            if matched_id != None or matched_id.group(1) != None:
                return matched_id.group(1)

        return None
