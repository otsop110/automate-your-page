def generate_content_HTML(content_lesson, content_title, content_description):
    html_text_1 = '''
<div class="lesson">
        ''' + content_lesson
    html_text_2 = '''
<div class="content">
    <div class="content-title">
        ''' + content_title
    html_text_3 = '''
    </div>
    <div class="content-description">
        ''' + content_description
    html_text_4 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text
def get_lesson(content):
    start_location = content.find('LESSON:')
    end_location = content.find('TITLE:')
    title = content[start_location+8 : end_location-1]
    return title

def get_title(content):
    start_location = content.find('TITLE:')
    end_location = content.find('DESCRIPTION:')
    title = content[start_location+7 : end_location-1]
    return title

def get_description(content):
    start_location = content.find('DESCRIPTION:')
    description = content[start_location+13 :]
    return description

def get_content_by_number(text, content_number):
    counter = 0
    while counter < content_number:
        counter = counter + 1
        next_content_start = text.find('LESSON:')
        next_content_end   = text.find('LESSON:', next_content_start + 1)
        content = text[next_content_start:next_content_end]
        text = text[next_content_end:]
    return content
        

TEST_TEXT = """
LESSON: Stage 0: Introduction to web
TITLE: New concepts
DESCRIPTION: After the first unit we are familiar with concepts such the web, html, urls and web applications. We know how I, my computer (browser), the internet, http and servers are connected to each other. We are also familiar with  basic html markups. We have learned how to edit text and how to add images and urls to our website.
LESSON: Stage 1: Creating a structured document with HTML
TITLE: New concepts
DESCRIPTION: After the stage 1 we know that web pages are constructed of boxes. HTML provides the structure to the website and CSS it`s style. Javascript provides interaction to the site. We are familiar with the concepts such as DOM (document object model) which provides the tree-like structure of the website. We also know that developers boxify their design.
LESSON: Stage 2: Introduction to "serious" programming
TITLE: New concepts
DESCRIPTION: After the stage 2 we are familiar with the concepts such as programming languages, interpreter, Python, grammar and Python expressions. I also know that my computer is fast in processing cycles. Cycle is a time computer has to do one step. My computer does 2,7 billion cycles per second. One step 2.7 billion times/second. In the time my computer does a cycle, light travels 11.1cm.
"""


def generate_all_html(text):
    current_content_number = 1
    content = get_content_by_number(text, current_content_number)
    all_html = ''
    while content != '':
        lesson = get_lesson(content)
        title = get_title(content)
        description = get_description(content)
        content_html = generate_content_HTML(lesson, title, description)
        all_html = all_html + content_html
        current_content_number = current_content_number + 1
        content = get_content_by_number(text, current_content_number)
    return all_html


print generate_all_html(TEST_TEXT)