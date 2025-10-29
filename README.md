[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ijhLvRTY)
# Contact Autocomplete (BST)

## Story
You’re implementing **autocomplete** for a contacts app. As a user types, you suggest up to `k` names that start with the prefix in **lexicographic order**.

## Task (What to Build)
Implement a Binary Search Tree of strings with **duplicate-reject** policy in `src/autocomplete_bst.py`:
- `insert(name) -> bool`  
- `find(name) -> bool`  
- `autocomplete(prefix, k) -> list[str]`: up to `k` matches starting with `prefix`, sorted.

You must leverage BST structure to **prune** traversal (don’t scan everything).

## Hints
- Use inorder traversal but **skip** subtrees outside the window `[prefix, prefix + '\uffff']`.
- Stop early when you have `k` results.
- Reject duplicates on insert to keep behavior deterministic.

## Run Tests Locally
```bash
python -m pytest -q
```

## Common Problems

- Forgetting to short-circuit traversal once keys exceed the high bound.
- Returning more than k candidates.
- Not enforcing the duplicates rule.

## Complexity

- insert/find: O(h) time.
- autocomplete: O(h + m) time, where m ≤ k (plus pruned subtrees); space O(h).

## Example

```bash
names = ["amy","anna","andrew","bob","bobby","carla"]
autocomplete("an", 5) -> ["andrew","anna"] or ["anna","andrew"] (both acceptable lexicographic lexicographic outputs)
```