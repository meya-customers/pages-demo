from calendar import monthrange
from dataclasses import dataclass
from datetime import date
from datetime import timedelta
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.orb.integration import OrbIntegrationRef
from typing import List
from typing import Optional


@dataclass
class AppUser:
    payment_day: int


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
            "u-0": AppUser(payment_day=10),
            "u-1": AppUser(payment_day=8),
            "u-2": AppUser(payment_day=12),
        }
        app_user = app_user_db[app_user_id]

        # Update user scope with key fields
        today = date.today()
        self.user.next_payment = f"{today.replace(day=app_user.payment_day) + (timedelta(days=monthrange(today.year, today.month)) if today.day > app_user.payment_day else 0):%B %-d, %Y}"
        self.user.logged_in = True
        return self.respond(data=self.Response(result=app_user_id))
