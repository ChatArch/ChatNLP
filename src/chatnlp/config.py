"Typed environment configuration for ChatNLP."

from chatenv import BaseEnvConfig, EnvField


class ChatnlpConfig(BaseEnvConfig):
    "ChatNLP ChatEnv configuration."

    _title = "ChatNLP Configuration"
    _aliases = ["chatnlp"]
    _storage_dir = "Chatnlp"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATNLP_API_KEY = EnvField(
        "CHATNLP_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatnlpConfig"]
