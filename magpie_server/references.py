from flask import jsonify
from datetime import datetime
from magpie.app import configuration
from magpie.plugins.dbadapter import ReferenceData, DBProvider

REFERENCES = [
    {
        "repositoryId": "azertyuiopqsdfghjklmwxcvbn",
        "commitId": "nbvcxwmlkjhgfqpiuytra",
        "kind": "cc",
        "subkind": "integration-tests",
        "branch": "main",
        "sizeKiB": 100,
        "collectedAt": datetime.now(),
    },
    {
        "repositoryId": "azertyuiopqsdfghjklmwxcvbn",
        "commitId": "nbvcxwmlkjhgfqpiuytra",
        "kind": "cc",
        "subkind": "unit-tests",
        "branch": "main",
        "sizeKiB": 100,
        "collectedAt": datetime.now(),
    },
    {
        "repositoryId": "azertyuiopqsdfghjklmwxcvbn",
        "commitId": "nbvcxwmlkjhgfqpiuytra",
        "kind": "lint",
        "subkind": "pylint",
        "branch": "main",
        "sizeKiB": 100,
        "collectedAt": datetime.now(),
    },
]


def list():
    db = DBProvider(configuration()).database
    ReferenceData.bind(db)
    query = ReferenceData.select().order_by(ReferenceData.collected_at)
    return jsonify({"items": REFERENCES})
    return {"items": [item for item in query]}
