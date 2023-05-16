from typing import NoReturn

from api.base import NessusAPI
from cli_arguments import CLI_ARGUMENTS
from core.main import Analyze


def main() -> NoReturn:
    api = NessusAPI(
        username=CLI_ARGUMENTS.username,
        password=CLI_ARGUMENTS.password,
        host=CLI_ARGUMENTS.host,
        port=CLI_ARGUMENTS.port,
        secure=CLI_ARGUMENTS.secure,
    )
    analyze = Analyze(address=CLI_ARGUMENTS.address,
                      api=api,
                      proxy=CLI_ARGUMENTS.proxy,
                      output_file=CLI_ARGUMENTS.output_file,
                      demo_mode=CLI_ARGUMENTS.demo_mode,)
    analyze.run_scan_and_get_report()


if __name__ == '__main__':
    main()
