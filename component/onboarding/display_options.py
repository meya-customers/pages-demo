from component.onboarding.option import Option
from dataclasses import dataclass
from meya.button.component.ask import ButtonAskComponent
from meya.component.element import Component
from meya.component.spec import ComponentSpec
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.text.component.info import InfoComponent
from meya.util.dict import to_dict
from textwrap import dedent
from typing import List


@dataclass
class OnboardingOptionsComponent(Component):
    @dataclass
    class Response:
        result: List[dict] = response_field()

    options: List[Option] = element_field()

    async def start(self) -> List[Entry]:
        widgets = []
        for option in self.options:
            widgets += [
                dict(
                    info=dedent(
                        f"""
                        ## {option.name} ({option.rate:.2f}%)

                        {option.description}

                        **Payment:** ${option.payment:.2f}
                        """
                    )
                ),
                dict(
                    buttons=[
                        dict(
                            text="View details",
                            action=dict(
                                flow="flow.onboarding.option_details",
                                data=dict(option=to_dict(option)),
                            ),
                        )
                    ]
                ),
            ]
        return self.respond(data=self.Response(widgets))
