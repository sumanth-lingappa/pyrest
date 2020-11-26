# pyrest
On the go templates for Python REST APIs

# Source:
> https://docs.python.org/3/library/argparse.html

# Argument Parser
```python
import argparse
art_parser = argparse.ArgumentParser(
                        description="",
                        prog="Name of the program (default: sys.argv[0])",
             )
````
# The add_argument() method
```python
arg_parser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
````

## name or flags
- positional arg 
    > name without `-` or `--` prefix
    - `add_argument("positional_arg")`
- optional arg
    - `-v`, `--verbose`
    - `add_argument("-v", "--verbose")`

## action
    - `store` - default action (no `action` arg)
        - `prog.py --foo 15` <-- foo=15 
    - `store_const` 
        - add_argument("-foo", action="store_const", const=30)
        - `prog.py --foo` <-- foo=30 
    - `store_true`
        - `prog.py --foo` <-- foo=True
    - `store_false`
        - `prog.py --foo` <-- foo=False
    - `append`
        - `prog.py --foo 1 --foo 2` <-- store foo=['1', '2']
    - `count`
        - `parser.add_argument('--verbose', '-v', action='count', default=0)` <-- `default=None` unless explicitly set 
        - `prog.py -vvv` <-- verbose=3

## nargs
    - N
        - `parser.add_argument('--foo', nargs=2)`
        - `prog.py --foo 1 2 3 4` <-- foo=['1', '2', '3', '4']
    - ?
        - `parser.add_argument('--foo', nargs=?)`
        - `parser.add_argument('--foo', nargs='?', const='c', default='d')` 
        - `parser.add_argument('bar', nargs='?', default='d')`
            - `prog.py XX --foo YY` <-- bar=d foo=YY
            - `prog.py XX --foo` <-- bar=d foo=c
            - `prog.py` <-- bar=d foo=d 
            - `prog.py XX` <-- bar=XX foo=d
    - * / +
        - `parser.add_argument('--foo', nargs='*')`
        - `parser.add_argument('baz', nargs='*')`
            - `prog.py a b c d --foo 1 2 3 4 5` <-- baz=['a', 'b', 'c', 'd'] foo=['1', '2', '3', '4', '5']

    - argparse.REMAINDER
            - parser = argparse.ArgumentParser(prog='PROG')
            - parser.add_argument('--foo')
            - parser.add_argument('command')
            - parser.add_argument('args', nargs=argparse.REMAINDER)
            - print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))
                - args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B'

## type
    - `parser.add_argument('foo', type=int)`
    - `parser.add_argument('bar', type=open)`
        - prog.py 2 tmp.txt <-- foo=2 bar=<file-handler of temp.txt>

## choices
    - parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
    - parser.add_argument('door', type=int, choices=range(1, 4))

## required
    - parser.add_argument('--foo', required=True)

## dest
    - parser.add_argument('--foo', dest='bar')
