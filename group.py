import pandas as pd
by_person = df.groupby("assignee")[
    "bug_id"].count().reset_index()
by_person.colums = [
    "assignee", "bug_count"]
print(by_person)