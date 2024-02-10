import requests
import time

# list of subdomains to check
subdomains = ['subdomain1.example.com', 'subdomain2.example.com', 'subdomain3.example.com']

def check_status(subdomain):
    try:
        response = requests.get(f'http://{subdomain}')
        status_code = response.status_code
        if status_code == 200:
            return 'Up'
        else:
            return f'Down ({status_code})'
    except requests.ConnectionError:
        return 'Down (Connection Error)'

def display_status(subdomain_statuses):
    print("-" * 40)
    print("Subdomain\t|\tStatus")
    print("-" * 40)
    for subdomain, status in subdomain_statuses.items():
        print(f"{subdomain}\t|\t{status}")
    print("-" * 40)

def main():
    while True:
        subdomain_statuses = {}
        for subdomain in subdomains:
            status = check_status(subdomain)
            subdomain_statuses[subdomain] = status
        display_status(subdomain_statuses)
        time.sleep(30)  # Wait for 30 seconds before checking again

if __name__ == "__main__":
    main()
