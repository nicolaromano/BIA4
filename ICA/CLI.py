import argparse

parser = argparse.ArgumentParser(description="Print a greeting message to the user.")
parser.add_argument("name", type=str, help="The name of the user to greet.")

args = parser.parse_args()

print(f"Hello, {args.name}!")
