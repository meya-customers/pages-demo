from dataclasses import dataclass
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List

# import arrow


@dataclass
class ParseShiftsComponentElement(Component):
    shifts: List[dict] = element_field()

    async def start(self) -> List[Entry]:
        result = True

        # for shift in self.shifts:
        #     timezone = shift["timezone"]
        #     now = arrow.now(timezone)
        #     day_of_week = now.format("ddd").lower()
        #     todays_shift = shift["times"][day_of_week]
        #
        #     if todays_shift is None:
        #         continue
        #
        #     start_hour = int(todays_shift["start"].split(":"))
        #     end_hour = int(todays_shift["end"].split(":"))
        #     start = now.replace(hour=start_hour)
        #     end = now.replace(hour=end_hour)
        #
        #     if start <= now <= end:
        #         result = True
        #         break

        return self.respond(data=ComponentResponse(result=result))
