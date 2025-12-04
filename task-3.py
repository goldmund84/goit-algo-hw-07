from tree_utils import build_sample_tree, sum_values


def main() -> None:
    tree = build_sample_tree()
    total = sum_values(tree.root)
    print(f"Сума всіх значень у дереві: {total}")


if __name__ == "__main__":
    main()
