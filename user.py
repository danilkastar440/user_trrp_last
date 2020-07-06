#!/usr/bin/env  python3
import sys
import json
import pprint
import argparse
import requests


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='I can help to make a request for api')
    parser.add_argument('--url', help='api url')
    parser.add_argument("--method", help="request method")
    parser.add_argument("--timeout", help="request timeout")
    parser.add_argument("--body", help="request body")
    parser.add_argument("--headers", help="request headers")
    parser.add_argument("--data", help="add data to response", action="store_true")
    args = parser.parse_args()


    if not (args.url):
        url = input("Enter api url: ")
    else:
        url = args.url

    if not args.method:
        method = input("Enter request method: ")
    else:
        method = args.method
    
    if not args.timeout:
        timeout = input("Enter request timeout: ")
    else:
        timeout = args.timeout
        
    if not args.body:
        body = input("Enter request body(json): ")
    else:
        body = args.body

    payload = {
            "endpoint": url,
            "http_method": method,
            "timeout": f"{timeout}s"
        }
    headers = {
            "Host": "trrv-univer.ew.r.appspot.com",
            "User-Agent": "curl/7.68.0",
            "Accept": "*/*",
        }
    #pprint.pprint(payload)
    response = requests.post("https://trrv-univer.ew.r.appspot.com/command", headers = headers, json = payload)
    #print(response.status_code)
    #pprint.pprint(response.json())
    json_response = response.json()
    i = 1
    print(response.status_code)
    if args.data:
        for item in json_response:
            print(f"Agent #{i}")
            print(f"bot_id: {item['bot_id']}")
            print(f"request time: {item['request_time']}")
            print(f"data: {item['endpoint_data']}")
            print("\n")
            i += 1
    else:
        for item in json_response:
            print(f"Agent #{i}")
            print(f"bot_id: {item['bot_id']}")
            print(f"request time: {item['request_time']}")
            print("\n")
            i += 1

