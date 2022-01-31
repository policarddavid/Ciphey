from typing import Dict, Optional

import base91

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Base91(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base91 decoding
        """
        try:
            file = open("AllDecryptions.txt", "a")
            file.write(f"Base91 decode: {base91.decode(ctext).decode('utf-8')}\n")
            file.close()
            return base91.decode(ctext).decode("utf-8")
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "base91"
