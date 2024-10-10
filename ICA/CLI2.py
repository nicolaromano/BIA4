import argparse

parser = argparse.ArgumentParser(description="Calculate the sum, mean, or median of a list of numbers.")
parser.add_argument("numbers", type=float, nargs="+", help="List of numbers to calculate the sum, mean, or median of.")
parser.add_argument("--sum", action="store_true", help="Calculate the sum of the numbers.")
parser.add_argument("--mean", action="store_true", help="Calculate the mean of the numbers.")
parser.add_argument("--max", action="store_true", help="Calculate the maximum of the numbers.")

args = parser.parse_args()

if args.sum:
    print(f"The sum of the numbers is: {sum(args.numbers)}")

if args.mean:
    print(f"The mean of the numbers is: {sum(args.numbers) / len(args.numbers)}")

if args.max:
    print(f"The maximum of the numbers is: {max(args.numbers)}")

# Because we have defined the --sum, --mean, and --max arguments as optional, we need to check if at least one of them is present.
if not any([args.sum, args.mean, args.max]):
    print("No operation specified. Please use --sum, --mean, or --max.")