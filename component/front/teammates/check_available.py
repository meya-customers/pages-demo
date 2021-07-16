from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.front.integration import FrontIntegration
from meya.front.integration import FrontIntegrationRef
from meya.front.payload.teammate import FrontTeammateList
from typing import List


@dataclass
class CheckAvailableComponent(Component):
    @dataclass
    class Response:
        result: bool = response_field()

    teammates: FrontTeammateList = element_field()
    integration: FrontIntegrationRef = element_field()

    async def start(self) -> List[Entry]:
        integration: FrontIntegration = await self.resolve(self.integration)

        available = False
        for teammate in self.teammates.results:
            if (
                teammate.email != integration.bot_teammate_email
                and teammate.is_available
            ):
                available = True
                break

        return self.respond(data=self.Response(result=available))
