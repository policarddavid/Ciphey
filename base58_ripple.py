from typing import Dict, Optional

import base58

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Base58_ripple(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base58 (Ripple) decoding
        """
        try:
            file = open("AllDecryptions.txt", "a")
            file.write(f"Base58_ripple decode: {base58.b58decode(ctext, alphabet=base58.RIPPLE_ALPHABET).decode('utf-8')}\n")
            file.close()
            return base58.b58decode(ctext, alphabet=base58.RIPPLE_ALPHABET).decode(
                "utf-8"
            )
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
        return "base58_ripple"
