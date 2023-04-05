code = '''
'''


if __name__ == '__main__':

    body = ''''''

    for line in code.splitlines():
        line = line.replace('    ', '\\t')
        line = line.replace('$', '\\\\$')
        line = line.replace('"', '\\"')

        body += f'"{line}",\n'

    print(body)
