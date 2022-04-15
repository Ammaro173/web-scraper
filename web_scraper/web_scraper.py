import requests

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
# res = requests.get(url)


def get_citations_needed_count(url):
    """_summary_

    Args:
        url (_type_): takes a url as an argument

    Returns:
        _type_: returns the number of citations needed
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.findAll("span", text="citation needed")
    print(result, end="\n")
    return len(result)


def get_citations_needed_report(url):
    """_summary_
    Args:
        url (_type_): takes a url as an argument

    Returns:
        _type_: returns a report of the number of citations needed
    """
    report = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    sup_finder = soup.find_all("sup")
    # print(sup_finder)

    for sup in sup_finder:
        if sup.findChildren("span"):
            # print(sup)
            report += f"\n ==> {sup.previous_sibling}[citation needed] ."

    return report


print("\n", "The number of citations are = ", get_citations_needed_count(url), end="\n")
print("\n", "The final report := ", get_citations_needed_report(url), end="\n")

##todo: add timeOut to the requests.get() !! , so you wont get blocked by the server + between operations!!
