import os
import pandas as pd
from datetime import datetime
import subprocess
# from sklearn.metrics import accuracy_score


def get_git_revision_hash() -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode("ascii")
            .strip()
        )
    except Exception:
        return "unknown"


def main():
    # 1. Load the test dataset
    test_data_path = "data/test.csv"
    # df_test = pd.read_csv(test_data_path)

    # 2. Load the model and generate predictions
    # TODO: Implement your model loading and inference logic here
    # predictions = my_model.predict(df_test.drop(columns=['target_column']))
    # actuals = df_test['target_column']

    # 3. Calculate Accuracy
    # accuracy = accuracy_score(actuals, predictions)
    accuracy = 0.95  # Mocked accuracy for demonstration

    # 4. Update the Leaderboard
    leaderboard_file = "leaderboard.csv"
    commit_hash = get_git_revision_hash()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_entry = pd.DataFrame(
        [{"timestamp": timestamp, "commit_hash": commit_hash, "accuracy": accuracy}]
    )

    if os.path.exists(leaderboard_file):
        leaderboard = pd.read_csv(leaderboard_file)
        leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
    else:
        leaderboard = new_entry

    # Sort by accuracy descending to maintain the "leaderboard" aspect
    leaderboard = leaderboard.sort_values(by="accuracy", ascending=False)
    leaderboard.to_csv(leaderboard_file, index=False)

    print(
        f"Evaluated commit {commit_hash}. Accuracy: {accuracy:.4f}. Leaderboard updated."
    )


if __name__ == "__main__":
    main()
