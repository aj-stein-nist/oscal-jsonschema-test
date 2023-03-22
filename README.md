# oscal-jsonschema-tests

## Example Error Message

Below is the error message reported from a community member with the current commit hashes.

Similar errors occurred with `develop` (at `45ad64221aee3c7483ce88f66bb3956ba0b392dd`) and `main` (at `6e9dc7a5aca3052e8a448ed94a0a104761cb1708`).

```sh
$ git submodule update --init --recursive
$ git rev-parse HEAD
b9ed7373658f398fa6ea23420b6b7e5a51a16bfa
$ popd
$ python -c 'from sys import version; print(version)'
3.9.16 (main, Mar 22 2023, 18:36:10)
[GCC 11.3.0]
$ python -m venv venv
$ source ./venv/bin/activate
$ python test_oscal_ap.py 2>&1 | tee README.md
E..
======================================================================
ERROR: test_empty_document (__main__.OscalAssessmentPlanJsonSchemaTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/me/oscal-jsonschema-tests/venv/lib/python3.9/site-packages/jsonschema/_format.py", line 135, in check
    result = func(instance)
  File "/home/me/oscal-jsonschema-tests/venv/lib/python3.9/site-packages/jsonschema/_format.py", line 387, in is_regex
    return bool(re.compile(instance))
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/re.py", line 252, in compile
    return _compile(pattern, flags)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_compile.py", line 788, in compile
    p = sre_parse.parse(p, flags)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 955, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 444, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 841, in _parse
    p = _parse_sub(source, state, sub_verbose, nested + 1)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 444, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 526, in _parse
    code = _escape(source, this, state)
  File "/home/me/.asdf/installs/python/3.9.16/lib/python3.9/sre_parse.py", line 427, in _escape
    raise source.error("bad escape %s" % escape, len(escape))
re.error: bad escape \p at position 2

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/me/oscal-jsonschema-tests/test_oscal_ap.py", line 13, in test_empty_document
    validate(document_instance, schema=self.schema)
  File "/home/me/oscal-jsonschema-tests/venv/lib/python3.9/site-packages/jsonschema/validators.py", line 1117, in validate
    cls.check_schema(schema)
  File "/home/me/oscal-jsonschema-tests/venv/lib/python3.9/site-packages/jsonschema/validators.py", line 231, in check_schema
    raise exceptions.SchemaError.create_from(error)
jsonschema.exceptions.SchemaError: '^(\\p{L}|_)(\\p{L}|\\p{N}|[.\\-_])*$' is not a 'regex'

Failed validating 'format' in metaschema['properties']['definitions']['additionalProperties']['properties']['properties']['additionalProperties']['properties']['pattern']:
    {'format': 'regex', 'type': 'string'}

On schema['definitions']['oscal-ap-oscal-metadata:responsible-role']['properties']['role-id']['pattern']:
    '^(\\p{L}|_)(\\p{L}|\\p{N}|[.\\-_])*$'

----------------------------------------------------------------------
Ran 3 tests in 0.012s

FAILED (errors=1)
```
