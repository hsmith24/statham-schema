[![Build Status](https://travis-ci.com/jacksmith15/statham-schema.svg?token=JrMQr8Ynsmu5tphpTQ2p&branch=master)](https://travis-ci.com/jacksmith15/statham-schema)  [![Documentation Status](https://readthedocs.org/projects/statham-schema/badge/?version=latest)](https://statham-schema.readthedocs.io/en/latest/?badge=latest)

# Statham Schema
A tool for generating Python objects from [JSON Schema](https://json-schema.org/) documents. See the [Documentation](https://statham-schema.readthedocs.io/en/stable/).

This project aims to simplify the experience of integrating with external sources, by providing:
1. **External validation**: Ensure that incoming data matches what you expect.
2. **Internal validation**: Ensure your application logic is consistent with the schema. Static type checking (see [mypy](http://mypy-lang.org/)) can do this job for you.
3. **Extensibility**: Extend the generated models with properties and methods useful to you.
4. **Visibility**: Update the model layer against schema changes automatically, and let static tools identify any issues.

The models generated by this tool are declared using a JSONSchema DSL. This DSL can easily be used to write schemas by hand, and extend models with extra features.

## Example DSL Definition
```python
from typing import List

from statham.dsl.elements import Array, Integer, Object, String
from statham.dsl.property import Property


class Choice(Object):
    choice_text: str = Property(String(maxLength=200), required=True)
    votes: int = Property(Integer(default=0))


class Poll(Object):
    question: str = Property(String(), required=True)
    choices: List[Choice] = Property(Array(Choice), required=True)
```

# Requirements
This package is currently tested for Python 3.6.

# Installation
This project may be installed using [pip](https://pip.pypa.io/en/stable/):
```
pip install statham-schema
```

# Generating python classes
Class definitions may be generated with the following command:
```
statham --input /path/to/schema.json
```

This will write generated python classes to stdout. Optionally specify an `--output` path to write to file.

## Command-line arguments
```
Required arguments:
  --input INPUT    Specify the path to the JSON Schema to be generated.

                   If the target schema is not at the root of a document, specify the
                   JSON Pointer in the same format as a JSONSchema `$ref`, e.g.
                   `--input path/to/document.json#/definitions/schema`


Optional arguments:
  --output OUTPUT  Output directory or file in which to write the output.

                   If the provided path is a directory, the command will derive the name
                   from the input argument. If not passed, the command will write to
                   stdout.

  -h, --help       Display this help message and exit.
```


# Using custom format keywords
JSONSchema allows use of custom string formats as specified [here](https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.7.2.3). Custom validation logic for string format may be added like so:
```python
from statham.validators import format_checker

@format_checker.register("my_format")
def _check_my_format(value: str) -> bool:
    ...
```

# Supported JSONSchema features
This library is tested to support [JSON Schema Draft 6](https://json-schema.org/specification-links.html#draft-6), with the following notable exceptions:
- Recursive references are not supported.
- Location-independent references are not supported.
- Changes of base URI via the `$id` keyword are not detected.

Priority order for remaining features is roughly as follows:
1. Support for features of more recent drafts.
2. Support for the exceptions listed above.
3. Support for features of less recent drafts.

However, contributions in any of these areas are welcome.

# Development
1. Clone the repository: `git clone git@github.com:jacksmith15/statham-schema.git && cd statham-schema`
2. Install the requirements: `pip install -r requirements.txt -r requirements-test.txt`
3. Run `pre-commit install`
4. Run the tests: `bash run_test.sh -c -a`

This project uses the following QA tools:
- [PyTest](https://docs.pytest.org/en/latest/) - for running unit tests.
- [PyLint](https://www.pylint.org/) - for enforcing code style.
- [MyPy](http://mypy-lang.org/) - for static type checking.
- [Travis CI](https://travis-ci.org/) - for continuous integration.
- [Black](https://black.readthedocs.io/en/stable/) - for uniform code formatting.

# License
This project is distributed under the MIT license.

![statham](https://giant.gfycat.com/GrotesqueNauticalCaracal.gif)
