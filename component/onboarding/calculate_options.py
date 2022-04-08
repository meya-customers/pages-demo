from component.onboarding.option import Option
from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import response_field
from meya.entry import Entry
from typing import List


@dataclass
class OnboardingOptionsComponent(Component):
    @dataclass
    class Response:
        result: List[Option] = response_field()

    async def start(self) -> List[Entry]:
        return self.respond(
            data=self.Response(
                [
                    Option(
                        name="Variable",
                        description="This mortgage rate can change over time.",
                        rate=3.9,
                        payment=3000.0,
                    ),
                    Option(
                        name="Fixed (1 year)",
                        description="This mortgage rate will remain the same for 1 year.",
                        rate=4.0,
                        payment=4000.0,
                    ),
                    Option(
                        name="Fixed (5 years)",
                        description="This mortgage rate will remain the same for 5 years.",
                        rate=5.0,
                        payment=5000.0,
                    ),
                ]
            )
        )
