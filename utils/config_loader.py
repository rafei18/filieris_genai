import yaml

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


## code added below 
def format_docs(docs):

    formatted = []

    for doc in docs:

        page = doc.metadata.get("page", "Unknown")
        header = doc.metadata.get("header", "Sans titre")
        source = doc.metadata.get("source", "Unknown")

        chunk = f"""
Source: {source}
Page: {page}
Section: {header}

Contenu:
{doc.page_content}
"""

        formatted.append(chunk)

    return "\n\n".join(formatted)
