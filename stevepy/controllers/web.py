from bs4 import BeautifulSoup
import requests


class WebController:
    pass


class WebController:

    def __init__(self, steve_url : str) -> None:
        self.url = steve_url

    @staticmethod
    def task_result(task_url : str):
        try:
            result = requests.get(url=task_url)
            content = BeautifulSoup(result.content, "html.parser")
            content = str(content.find_all('tbody', {"id": "TaskResultsTable"})[0])
            content = BeautifulSoup(content, 'html.parser')

            # Find all the 'tr' elements
            rows = content.find_all('tr')

            # Initialize an empty dictionary to store the results
            result_dict = {}

            # Iterate through the rows to extract TaskResultKey and Status
            for row in rows:
                task_key = row.find('td', id='TaskResultKey').get_text(strip=True)
                status = row.find('td', id='TaskResultStatus').get_text(strip=True)
                result_dict[task_key] = status

            return result_dict
        except IndexError:
            return 404 #Task not found