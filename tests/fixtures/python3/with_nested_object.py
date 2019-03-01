from typing import Dict, Optional, List, Any


class Nested(object):
    def __init__(self, data: Optional[Dict] = None):
        data = data or {}

        self.x: Optional[str] = data.get("x")


class Test(object):
    def __init__(self, data: Optional[Dict] = None):
        data = data or {}

        self.nested: Optional[Nested] = data.get("nested")
