from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.orb.integration import OrbIntegrationRef
from typing import List
from typing import Optional


@dataclass
class AppUser:
    name: str


@dataclass
class LoginComponent(Component):
    integration: OrbIntegrationRef = element_field()

    @dataclass
    class Response:
        result: Optional[str] = response_field()

    async def start(self) -> List[Entry]:
        # Get the app user ID set via orb
        app_user_id = await self.user.try_reverse_lookup(
            integration_id=self.integration.ref
        )
        if not app_user_id:
            return self.respond(data=self.Response(result=None))

        # TODO Replace with HTTP call to app server
        app_user_db = {
            "u-0": AppUser(name="Alfred"),
            "u-1": AppUser(name="Betty"),
            "u-2": AppUser(name="Charlie"),
        }
        app_user = app_user_db[app_user_id]

        # Update user scope with key fields
        self.user.name = app_user.name
        return self.respond(data=self.Response(result=app_user_id))
