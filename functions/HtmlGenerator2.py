def tagBlock(text, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{text}</{tag}>'


if __name__ == '__main__':
    print(tagBlock('block'))
    print(tagBlock('inline and class', 'info', True))
    print(tagBlock('inline', inline=True))
    print(tagBlock(inline=True, text='inline'))
    print(tagBlock('fail', classe='error'))
