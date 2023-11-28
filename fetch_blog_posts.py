import requests

def fetch_latest_posts(username, max_posts=5):
    url = f"https://dev.to/api/articles?username={username}"
    response = requests.get(url)
    response.raise_for_status()

    articles = response.json()
    return articles[:max_posts]

def update_readme(articles):
    with open('README.md', 'r') as file:
        readme_content = file.readlines()

    start_marker = '<!--START_SECTION:blog-->\n'
    end_marker = '<!--END_SECTION:blog-->\n'

    start_index = readme_content.index(start_marker) + 1
    end_index = readme_content.index(end_marker)

    updated_content = readme_content[:start_index] + [f"- [{article['title']}]({article['url']})\n" for article in articles] + readme_content[end_index:]

    with open('README.md', 'w') as file:
        file.writelines(updated_content)

def main():
    username = "aldoportillo" 
    latest_posts = fetch_latest_posts(username)
    update_readme(latest_posts)

if __name__ == "__main__":
    main()
