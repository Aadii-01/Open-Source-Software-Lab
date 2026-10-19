
import tkinter as tk
from tkinter import ttk, messagebox
import json
import ast
import operator
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
TRANSLATION_DIR = APP_DIR / "translations"

# English digits -> Devanagari digits
ENGLISH_DIGITS = "0123456789"
DEVANAGARI_DIGITS = "०१२३४५६७८९"

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def localize_digits(value, language):
    """Display numbers using the selected language's digits."""
    value = str(value)

    if language in ("hi", "mr"):
        return value.translate(
            str.maketrans(ENGLISH_DIGITS, DEVANAGARI_DIGITS)
        )

    return value


def normalize_digits(value):
    """Convert Devanagari digits to standard digits for calculation."""
    return value.translate(
        str.maketrans(DEVANAGARI_DIGITS, ENGLISH_DIGITS)
    )


def safe_calculate(expression):
    """Evaluate basic arithmetic without using eval()."""
    expression = normalize_digits(expression)

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Invalid number")

        if isinstance(node, ast.BinOp):
            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operation")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operation")

            return operation(evaluate(node.operand))

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree)


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("360x490")
        self.root.resizable(False, False)

        self.language = "en"
        self.translations = {}

        # Keep the actual calculation expression in English digits.
        self.expression = ""
        self.display_text = tk.StringVar()

        self.load_language("en")
        self.build_interface()
        self.update_texts()

    def load_language(self, language):
        path = TRANSLATION_DIR / f"{language}.json"

        with path.open("r", encoding="utf-8") as file:
            self.translations = json.load(file)

        self.language = language

    def text(self, key):
        return self.translations.get(key, key)

    def refresh_display(self):
        self.display_text.set(
            localize_digits(self.expression, self.language)
        )

    def build_interface(self):
        self.root.title(self.text("title"))

        self.language_box = ttk.Combobox(
            self.root,
            values=["English", "हिन्दी", "मराठी"],
            state="readonly",
            width=12
        )
        self.language_box.current(0)
        self.language_box.pack(pady=10)
        self.language_box.bind(
            "<<ComboboxSelected>>", self.change_language
        )

        self.display = ttk.Entry(
            self.root,
            textvariable=self.display_text,
            font=("DejaVu Sans", 20),
            justify="right",
            state="readonly"
        )
        self.display.pack(
            fill="x", padx=12, ipady=10, pady=8
        )

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(
            fill="both", expand=True, padx=10, pady=10
        )

        self.buttons = []

        layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row_index, row in enumerate(layout):
            for column_index, value in enumerate(row):
                button = ttk.Button(
                    self.button_frame,
                    text=localize_digits(value, self.language),
                    command=lambda v=value: self.press(v)
                )

                button.grid(
                    row=row_index,
                    column=column_index,
                    sticky="nsew",
                    padx=3,
                    pady=3,
                    ipady=10
                )

                self.buttons.append((button, value))

        for column in range(4):
            self.button_frame.columnconfigure(column, weight=1)

        for row in range(4):
            self.button_frame.rowconfigure(row, weight=1)

        self.clear_button = ttk.Button(
            self.root, command=self.clear
        )
        self.clear_button.pack(
            fill="x", padx=12, pady=4
        )

        self.delete_button = ttk.Button(
            self.root, command=self.delete_last
        )
        self.delete_button.pack(
            fill="x", padx=12, pady=4
        )

        self.status = ttk.Label(self.root, anchor="center")
        self.status.pack(fill="x", pady=5)

    def update_texts(self):
        self.root.title(self.text("title"))
        self.clear_button.configure(text=self.text("clear"))
        self.delete_button.configure(text=self.text("delete"))
        self.status.configure(text=self.text("hint"))

        # Update the digit buttons when the language changes.
        for button, value in self.buttons:
            button.configure(
                text=localize_digits(value, self.language)
            )

        self.refresh_display()

    def change_language(self, event=None):
        languages = {
            "English": "en",
            "हिन्दी": "hi",
            "मराठी": "mr",
        }

        language = languages.get(self.language_box.get(), "en")

        try:
            self.load_language(language)
            self.update_texts()
        except (OSError, json.JSONDecodeError):
            messagebox.showerror(
                "Error", "Could not load translation file."
            )

    def press(self, value):
        if value == "=":
            self.calculate()
        else:
            self.expression += value
            self.refresh_display()

    def calculate(self):
        if not self.expression.strip():
            return

        try:
            result = safe_calculate(self.expression)
            self.expression = str(result)
            self.refresh_display()
            self.status.configure(text=self.text("success"))

        except ZeroDivisionError:
            self.status.configure(text=self.text("zero_error"))

        except (
            ValueError, SyntaxError, TypeError, OverflowError
        ):
            self.status.configure(text=self.text("invalid"))

    def clear(self):
        self.expression = ""
        self.refresh_display()
        self.status.configure(text=self.text("hint"))

    def delete_last(self):
        self.expression = self.expression[:-1]
        self.refresh_display()


if __name__ == "__main__":
    window = tk.Tk()
    app = Calculator(window)
    window.mainloop()

