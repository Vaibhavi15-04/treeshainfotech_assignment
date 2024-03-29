# -*- coding: utf-8 -*-
"""restful.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155EVefrsWxenCuV3y-m9tO1_gpgDZX9X
"""

#!/usr/bin/env python3
import requests
import json
import argparse
import sys
import csv

class RestfulClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, method, endpoint, outfile=None):
        self.method = method
        self.endpoint = endpoint
        self.outfile = outfile

    def perform_request(self):
        url = f"{self.BASE_URL}{self.endpoint}"
        response = None

        if self.method == 'get':
            response = requests.get(url)
        elif self.method == 'post':
            # For simplicity, POST request is not implemented in this example
            print("POST method is not implemented in this example.")
            sys.exit(1)
        else:
            print(f"Invalid method: {self.method}")
            sys.exit(1)

        self.handle_response(response)

    def handle_response(self, response):
        print(f"HTTP Status Code: {response.status_code}")

        if response.status_code // 100 == 2:  # Check if status code is 2xx
            if self.outfile:
                self.save_to_file(response.json())
            else:
                print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error: {response.status_code}")
            sys.exit(1)

    def save_to_file(self, data):
        if self.outfile.endswith('.json'):
            with open(self.outfile, 'w') as json_file:
                json.dump(data, json_file, indent=2)
            print(f"Response saved to {self.outfile}")
        elif self.outfile.endswith('.csv'):
            # For simplicity, CSV saving is not implemented in this example
            print("CSV saving is not implemented in this example.")
            sys.exit(1)
        else:
            print("Unsupported output file format. Supported formats: .json, .csv")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="A simple command-line REST client for JSONPlaceholder.")
    parser.add_argument("method", choices=["get", "post"], help="HTTP method (get or post)")
    parser.add_argument("endpoint", help="URI fragment (e.g., /posts/1)")
    parser.add_argument("-o", "--output", help="Output file path (optional)")

    args = parser.parse_args()

    client = RestfulClient(args.method, args.endpoint, args.output)
    client.perform_request()

if __name__ == "__main__":
    main()