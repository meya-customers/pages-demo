from calendar import monthrange
from dataclasses import dataclass
from datetime import date
from datetime import timedelta
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.integration import OrbIntegrationRef
from typing import List


@dataclass
class AppUser:
    payment_day: int


@dataclass
class LoginComponent(Component):
    integrations: List[OrbIntegrationRef] = element_field()

    async def start(self) -> List[Entry]:
        # Get the app user ID set via orb
        app_user_id = None
        async for result in (
            await self.user.try_reverse_lookup(integration_id=integration.ref)
            for integration in self.integrations
        ):
            if result:
                app_user_id = result
                break
        if not app_user_id:
            return self.respond()

        # TODO Replace with HTTP call to app server
        app_user_db = {
            "u-0": AppUser(payment_day=10),
            "u-1": AppUser(payment_day=8),
            "u-2": AppUser(payment_day=12),
        }
        app_user = app_user_db.get(app_user_id)
        if not app_user:
            return self.respond()

        # Update user scope with key fields
        today = date.today()
        self.user.app_user_id = app_user_id
        self.user.next_payment = f"{today.replace(day=app_user.payment_day) + (timedelta(days=monthrange(today.year, today.month)[1]) if today.day > app_user.payment_day else 0):%B %-d, %Y}"
        return self.respond()
