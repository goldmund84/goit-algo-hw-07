from tree_utils import build_sample_tree, find_maximum


def main() -> None:
    tree = build_sample_tree()
    maximum = find_maximum(tree.root)
    print(f"Найбільше значення у дереві: {maximum}")


if __name__ == "__main__":
    main()
