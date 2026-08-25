import sys
from cli import create_parser, add_task, list_tasks

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
