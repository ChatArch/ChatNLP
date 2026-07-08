from click.testing import CliRunner

from chatnlp import __version__
from chatnlp.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatnlp, version {__version__}" in result.output
