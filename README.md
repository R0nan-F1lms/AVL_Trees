# AVL_Trees

A Python script to **visualise AVL Tree insertions and deletions** step by step using `matplotlib`.

This tool is helpful for **learning**, **teaching**, or **debugging** AVL tree operations with clear visuals and contextual information at each step.

---

## 🔧 Features

- Visualises AVL tree **insertions** and **deletions** dynamically.
- Displays the **current step** (e.g. insertion or deletion).
- Shows **balance factors**, internal and external nodes.
- Highlights **imbalanced nodes** and structural changes in the tree.
- Maintains tree layout in a clean **top-down grid structure**.
- Automatically adjusts figure size and bounding box to fit content.

---

## ▶️ How to Use

### 1. **Insertion Visualisation**

In the `main_insertion_visualisation.py` (or similar file), you'll find:

```python
keys_to_insert = [20, 9, 3, 7, 5, 8, 25, 30, 15, 6, 17]
```

✅ Replace this list with your own sequence of integers to be inserted into the AVL tree.

When you run the script, each step will:
- Show the current AVL tree.
- Indicate whether a rotation is needed or not.
- Display internal and external nodes.
- Update the structure live after each change.

---

### 2. **Deletion Visualisation**

In the deletion script (e.g. `main_deletion_visualisation.py`), a **fully built AVL tree** is used first. Then, a list like the following is provided:

```python
keys_to_delete = [20, 15, 8, 25, 30, 9, 17, 5, 6, 3, 7]
```

✅ Replace the numbers with your desired deletion sequence.

Each step will:
- Highlight the node to be deleted in red.
- Show the resulting AVL tree.
- Indicate if rebalancing is required and apply rotations accordingly.

---

## 📦 Requirements

Make sure you have the following libraries installed:

- `matplotlib`
- `networkx`

If pip doesn't work in your environment, try:

```bash
py -m pip install matplotlib networkx
```

Or install via your package manager or Python environment tool.

---

## 📁 Files

- `main_insertion_visualisation.py` – Visualises insertions.
- `main_deletion_visualisation.py` – Visualises deletions.
- `avl.py` – Contains AVL tree logic (insertion, deletion, balancing).
- `plot_utils.py` – Handles tree drawing and figure annotation.

---

## 🧠 Educational Value

This tool was designed with clarity and correctness in mind. It:
- Visually explains when and why a tree becomes imbalanced.
- Helps you understand which rotation (if any) is required.
- Follows AVL tree rules strictly, including replacing deleted nodes with the **largest element smaller** when applicable.
