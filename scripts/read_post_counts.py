import oyaml as yaml
import frontmatter
from os import walk
import yaml
import requests

POSTS_FOLDER = "_posts"
CONFIG_FILE = "_config.yml"
REQUEST_COUNT_URL = "https://api.applause-button.com/get-multiple"
ORDERING = ["title", "header", "excerpt", "date", "show_date", "toc", "toc_label", "toc_sticky", "tags", "read_count"]

def get_base_url():
    with open(CONFIG_FILE, 'r') as file:
        site_name = yaml.safe_load(file)
    base_url = site_name["url"]
    return base_url

def create_count_url(post_name):
    post_components = post_name[:-3].split("-")
    article_name = "-".join(post_components[3:])
    return article_name

def get_urls_to_fetch_counts_for():
    base_url = get_base_url()
    filenames = next(walk(POSTS_FOLDER), (None, None, []))[2]
    return list(map(lambda name: "{0}/{1}/".format(base_url, name), map(create_count_url, filenames))), filenames

def form_request_url(article_names):
    headers = {'Content-type': 'text/plain'}
    binary_data = "["
    for article in article_names:
        binary_data += '"' + article + '"' + ","
    binary_data = binary_data[:-1] + "]"
    return requests.post(REQUEST_COUNT_URL, headers=headers, data=binary_data)

def update_claps_from_response(response_data, filenames):
    url_to_count = {}
    base_url = get_base_url()
    for js in response_data:
        url_to_count[js["url"]] = js["claps"]
    for article in filenames:
        article_url_name = "{0}/{1}/".format(base_url, create_count_url(article))[8:]
        count = url_to_count.get(article_url_name, 0)
        article_file = "{0}/{1}".format(POSTS_FOLDER, article)
        with open(article_file, 'r+', encoding="utf8") as f:
            post = frontmatter.load(f)
            post["applause_count"] = count
            sorted_metadata = dict(sorted(post.metadata.items(), key=lambda x: ORDERING.index(x[0]) if x[0] in ORDERING else float("inf")))
            post.metadata = sorted_metadata
            content = frontmatter.dumps(post)

            f.seek(0)
            f.write(content)
            f.truncate()

urls, filenames = get_urls_to_fetch_counts_for()
response = form_request_url(urls)
update_claps_from_response(response.json(), filenames)
    
