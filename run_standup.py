"""Script to initiate and run the standup reporting process."""

import argparse
import logging

from standup.runner import Runner


def configure_logging(level: str) -> None:
    """Configure the logging level and format for the application.

    Args:
        level (str): The logging level.
    """
    logging_level = getattr(logging, level.upper(), logging.ERROR)
    logging.basicConfig(
        level=logging_level, format="%(asctime)s [%(levelname)s]: %(message)s"
    )


def main() -> None:
    """Execute the Runner to display information from providers.

    Args:
        args (argparse.Namespace): Command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Run the standup! Grab your coffee.")
    parser.add_argument(
        "--log-level",
        choices=["critical", "error", "warning", "info", "debug"],
        default="error",
        help="Set the logging level.",
    )
    args = parser.parse_args()

    configure_logging(args.log_level)

    runner = Runner()
    runner.run()


if __name__ == "__main__":
    main()
