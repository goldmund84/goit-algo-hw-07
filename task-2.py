from tree_utils import build_sample_tree, find_minimum


def main() -> None:
    tree = build_sample_tree()
    minimum = find_minimum(tree.root)
    print(f"Найменше значення у дереві: {minimum}")


if __name__ == "__main__":
    main()
