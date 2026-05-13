import os
import zipfile


EXPORT_FOLDER = "exports"


def export_website_zip(project_id: int):

    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    html_content = f"""
    <html>
        <head>
            <title>Website Export</title>
        </head>

        <body>
            <h1>Project {project_id}</h1>
            <p>AI Generated Website</p>
        </body>
    </html>
    """

    html_path = f"{EXPORT_FOLDER}/index.html"

    with open(html_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    zip_path = f"{EXPORT_FOLDER}/website.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(html_path, arcname="index.html")

    return zip_path