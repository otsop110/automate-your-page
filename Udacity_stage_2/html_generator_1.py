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
        <p>
        ''' + content_description
    html_text_4 = '''
        </p>
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def make_HTML(content):
    content_lesson = content[0]
    content_title = content[1]
    content_description = content[2]
    return generate_content_HTML(content_lesson, content_title, content_description)

EXAMPLE_LIST_OF_CONTENTS = [ ['Stage 0: Introduction to web', ' New concepts','After the first unit we are familiar with concepts such the web, html, urls and web applications. We know how I, my computer (browser), the internet, http and servers are connected to each other. We are also familiar with  basic html markups. We have learned how to edit text and how to add images and urls to our website.'],
                             ['tage 1: Creating a structured document with HTML', 'New concepts', 'After the stage 1 we know that web pages are constructed of boxes. HTML provides the structure to the website and CSS it`s style. Javascript provides interaction to the site. We are familiar with the concepts such as DOM (document object model) which provides the tree-like structure of the website. We also know that developers boxify their design.'],
                             ['Stage 2: Introduction to "serious" programming', 'New concepts', 'After the first session of stage 2 we are familiar with the concepts such as programming languages, interpreter, Python, grammar and Python expressions. I also know that my computer is fast in processing cycles. Cycle is a time computer has to do one step. My computer does 2,7 billion cycles per second. One step 2.7 billion times/second. In the time my computer does a cycle, light travels 11.1cm.'] ]


def make_HTML_for_many_contents(list_of_contents):
    HTML = "tarjas website.html"
    for content in list_of_contents:
        content_HTML = make_HTML(content)
        HTML = HTML + content_HTML
    return HTML

print make_HTML_for_many_contents(EXAMPLE_LIST_OF_CONTENTS)