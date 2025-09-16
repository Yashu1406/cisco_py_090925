import argparse
import requests
import json


API = "http://127.0.0.1:5000/api"


def create_patient(name, age, disease):
    resp = requests.post(f"{API}/patients", json={"name": name, "age": age, "disease": disease})
    print(resp.status_code, resp.json())


def list_patients(limit=10):
    resp = requests.get(f"{API}/patients", params={"limit": limit})
    print(json.dumps(resp.json(), indent=2))


def main():
    parser = argparse.ArgumentParser("HMS CLI")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("create")
    p1.add_argument("--name", required=True)
    p1.add_argument("--age", type=int, required=True)
    p1.add_argument("--disease", default="")

    p2 = sub.add_parser("list")
    p2.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()
    if args.cmd == "create":
        create_patient(args.name, args.age, args.disease)
    elif args.cmd == "list":
        list_patients(args.limit)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
