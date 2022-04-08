from component.onboarding.option import Option
from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from mortgage import Loan
from typing import List


@dataclass
class OnboardingOptionsComponent(Component):
    @dataclass
    class Response:
        result: List[Option] = response_field()

    total_price: str = element_field()
    downpayment: str = element_field()
    income: str = element_field()

    async def start(self) -> List[Entry]:
        options = [
            self.calculate_option(
                variable=True,
                name="Variable",
                description="This mortgage rate can change over time.",
                rate=3.9,
            ),
            self.calculate_option(
                variable=False,
                name="Fixed (1 year)",
                description="This mortgage rate will remain the same for 1 year.",
                rate=4.0,
            ),
            self.calculate_option(
                variable=False,
                name="Fixed (5 years)",
                description="This mortgage rate will remain the same for 5 years.",
                rate=5.0,
            ),
        ]
        print(options)
        return self.respond(data=self.Response(options))

    def calculate_option(
        self, *, variable: bool, name: str, description: str, rate: float
    ) -> Option:
        principal = float(self.total_price) - float(self.downpayment)
        loan = Loan(principal=principal, interest=rate / 100.0, term=30)
        return Option(
            variable=variable,
            name=name,
            description=description,
            rate=rate,
            payment=float(loan.monthly_payment),
            income_fraction=float(loan.monthly_payment)
            / (float(self.income) / 12.0),
        )
