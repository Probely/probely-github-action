import argparse

import requests


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--region", required=True)
    parser.add_argument("--scan-profile", required=True)
    namespace = parser.parse_args()
    return (
        namespace.api_key,
        namespace.target_id,
        namespace.region,
        namespace.scan_profile,
    )


def scan(api_key: str, target_id: str, base_url: str, scan_profile: str):
    response = requests.post(
        f"{base_url}/targets/{target_id}/scan_now/",
        json={"scan_profile": scan_profile} if scan_profile else {},
        headers={"Authorization": f"JWT {api_key}"},
    )
    try:
        response.raise_for_status()

    except requests.HTTPError:
        print("Received error from Probely's API when starting the scan:")
        print(f"Status code: {response.status_code}")
        print(f"Content: {response.content.decode()}")
        exit(1)

    else:
        print("Scan started successfully.")


if __name__ == "__main__":
    api_key, target_id, region, scan_profile = parse_args()
    base_url = f"https://api.{region}.probely.com"
    scan(api_key, target_id, base_url, scan_profile)
