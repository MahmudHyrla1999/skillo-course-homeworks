browser_history = []


def visit_web_page(page):
    browser_history.append(page)


def go_back():
    if len(browser_history) > 1:
        current_page = browser_history.pop()
        previous_page = browser_history[-1]
        return previous_page
    else:
        return "Cannot go back further. You are on the first page."


visit_web_page("Home Page")
visit_web_page("Page A")
visit_web_page("Page B")

print("Current Page:", browser_history[-1])
print("Going back...")

previous_page = go_back()
print("Current Page:", previous_page)
print("Going back...")
previous_page = go_back()
print("Current Page:", previous_page)
