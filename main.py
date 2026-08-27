from cli import create_parser, add_task, list_tasks, complete_task, find_tasks

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.id)
    elif args.command == "search":
        find_tasks(args.query)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
