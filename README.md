# Opoona
> The thicket opener

## Requirements

- Git
- Python 2.7.x or Python 3.5.x

## Getting Started

```
$ pip install git+https://github.com/pine/opoona.git
```

## Usage

```
$ opoona
usage:
    opoona setup
    opoona <issue>

$ opoona setup
`/home/username/.opoona.yaml` is created.

$ vim ~/.opoona.yaml
# edit your `opoona` setting

$ opoona issues-1
fetching github issue...
checkout issues/1
create empty commit
pushing to origin...
creating pull request...
  master <- issues/1
  done! https://github.com/pine/opoona/pull/8
```

Enjoy :tada: :tada: :tada:


## Development
### venv
For Python 2.7.x users:

```
$ pip install virtualenv
$ virtualenv venv-2.7
$ . venv-2.7/bin/activate
```

For Python 3.5.x users:

```
$ python -m venv venv-3.5
$ . venv-3.5/bin/activate
```

### Install dependencies

```
$ pip install -r requirements.txt
```

### Run opoona
Try to execute in project root directory.

```
$ python -m opoona
```

### Run tests

```
$ pip install -r tests/requirements.txt
$ python runtests.py
```

## License
MIT License
