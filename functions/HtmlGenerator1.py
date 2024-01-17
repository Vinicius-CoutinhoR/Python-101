def tagBlock(text, classe='success'):
    return f'<div class="{classe}">{text}</div>'


if __name__ == '__main__':
    assert tagBlock('Successfully included') == \
           '<div class="success"> Successfully included!</div>'
    assert tagBlock('Impossible to delete', 'error') == \
           '<div class="error"> Impossible to delete</div>'

print(tagBlock('block'))
