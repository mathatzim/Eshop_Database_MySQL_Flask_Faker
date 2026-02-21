from __future__ import annotations

from pathlib import Path

from flask import Flask, render_template, url_for

from .db import get_connection
from .queries import ALL_QUERIES

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "templates"

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))


@app.route("/")
def index():
    links = [f"<li><a href='{url_for('run_query', qid=i)}'>Query {i}</a></li>" for i in sorted(ALL_QUERIES)]
    return "<h2>Online Store Database</h2><p>Select a query:</p><ul>" + "".join(links) + "</ul>"


@app.route("/query/<int:qid>")
def run_query(qid: int):
    if qid not in ALL_QUERIES:
        return "Query not found", 404

    sql = ALL_QUERIES[qid]
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Templates from the original coursework expect slightly different variable names.
    if qid == 1:
        return render_template("Query1.html", data=rows, query=sql)

    query_key = f"query{qid-1}"
    data_key = f"data{qid-1}"
    kwargs = {query_key: sql, data_key: rows}
    return render_template(f"Query{qid}.html", **kwargs)


def main():
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
