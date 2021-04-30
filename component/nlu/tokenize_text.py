import re

from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from typing import List


@dataclass
class SentenceTokenizerComponent(Component):
    text: str = element_field()

    @dataclass
    class Response:
        result: List[str] = response_field()

    async def start(self) -> List[Entry]:
        pattern = r"[.?!][\s]+|[\r\n]+"
        sentences = re.split(pattern, self.text)
        return self.respond(data=self.Response(result=sentences))
