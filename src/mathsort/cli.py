from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    CLI for gathering information after a GoAnywhere Crash
    """)
    parser.add_argument("email", help="email address to send report to")

    return parser


def main():
    parser = create_parser()