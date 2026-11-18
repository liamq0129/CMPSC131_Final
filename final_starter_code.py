"""
FinTrack — Personal Budget & Expense Tracker
CMPSC 131 Final Project — Starter Code

Fill in the TODOs. Do not import the csv module — parse lines yourself
with string methods, per the spec.
"""

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class Transaction:
    """Represents a single financial transaction."""

    def __init__(self, date: str, description: str, category: str, amount: float):
        self.date = date                # "MM/DD/YYYY"
        self.description = description
        self.category = category
        self.amount = amount

    def to_line(self) -> str:
        """Return this transaction formatted back into a data-file line."""
        # TODO: return a comma-separated string: date,description,category,amount
        pass

    def __str__(self) -> str:
        # TODO: return a nicely formatted, human-readable one-line summary
        pass


class BudgetTracker:
    """Holds all transactions and budget limits, and performs analysis."""

    def __init__(self):
        self.transactions = []      # list of Transaction objects
        self.budget_limits = {}     # category (str) -> monthly limit (float)

    # ---------- Loading data ----------

    def load_from_file(self, filename: str) -> None:
        """Parse a comma-separated transaction file into Transaction objects."""
        # TODO:
        # - open the file with a `with` statement
        # - for each line: strip it, split on ",", build a Transaction
        # - append it to self.transactions
        pass

    def add_transaction(self, date: str, description: str, category: str, amount: float) -> None:
        """Create and store a new Transaction."""
        # TODO
        pass

    # ---------- Category summary (dictionaries) ----------

    def category_totals(self) -> dict:
        """Return a dict of category -> total amount spent (negative = expense)."""
        # TODO: iterate self.transactions, accumulate into a dict
        pass

    def set_budget_limit(self, category: str, limit: float) -> None:
        """Set/update the monthly budget limit for a category."""
        # TODO
        pass

    def print_category_summary(self) -> None:
        """Print each category's total and flag categories over budget."""
        # TODO: use category_totals() and self.budget_limits
        pass

    # ---------- Monthly matrix (2D lists) ----------

    def build_monthly_matrix(self) -> tuple:
        """
        Build a 2D list: rows = sorted unique categories, columns = months 1-12.
        Returns (categories_list, matrix) where matrix[i][j] is the total
        for categories_list[i] in month j+1.
        """
        # TODO
        pass

    def print_monthly_matrix(self) -> None:
        """Print the monthly matrix as an aligned table with month headers."""
        # TODO
        pass

    # ---------- Two-pointer refund matching ----------

    def find_refund_matches(self) -> list:
        """
        Sort a COPY of self.transactions by amount, then use the two-pointer
        technique (one pointer at each end of the sorted list) to find pairs
        whose amounts sum to approximately 0 (a purchase and its refund).

        Do NOT use a nested loop / brute-force all-pairs search here.
        Return a list of (Transaction, Transaction) tuples.
        """
        # TODO
        pass

    # ---------- Recursive binary search by date ----------

    def find_transactions_by_date(self, target_date: str) -> list:
        """
        Sort a COPY of self.transactions by date, then use a recursive
        binary search to locate transactions on target_date.
        Return a list of matching Transaction objects (there may be more
        than one on the same date).
        """
        # TODO: likely needs a recursive helper function/method that takes
        # the sorted list and a (low, high) range
        pass

    # ---------- Export / save / load ----------

    def export_report(self, filename: str) -> None:
        """Write the category summary and monthly matrix to a text file."""
        # TODO
        pass

    def save_session(self, filename: str) -> None:
        """Write all transactions and budget limits to a save file."""
        # TODO: pick a simple line-based format; document it in your README
        pass

    def load_session(self, filename: str) -> None:
        """Load transactions and budget limits from a save file."""
        # TODO
        pass


def get_valid_amount(prompt: str) -> float:
    """Repeatedly prompt until the user enters a valid float (indefinite loop)."""
    # TODO
    pass


def main() -> None:
    tracker = BudgetTracker()

    while True:
        print("\n===== FinTrack Menu =====")
        print("1. Load transactions from file")
        print("2. View all transactions")
        print("3. Add a new transaction")
        print("4. Category summary")
        print("5. Monthly spending matrix")
        print("6. Set a budget limit")
        print("7. Find refund/purchase matches")
        print("8. Search for a transaction by date")
        print("9. Export report to file")
        print("10. Save session")
        print("11. Load session")
        print("12. Quit")

        choice = input("Choose an option: ").strip()

        # TODO: dispatch to the right method based on `choice`
        if choice == "12":
            print("Goodbye!")
            break
        else:
            print("TODO: implement this option")


if __name__ == "__main__":
    main()
