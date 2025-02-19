# Argument

> Auto-generated documentation for [mypy_boto3_builder.structures.argument](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py) module.

Method or function argument.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Argument
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
        - [Argument().is_kwflag](#argumentis_kwflag)
        - [Argument.kwflag](#argumentkwflag)
        - [Argument().required](#argumentrequired)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py#L12)

```python
class Argument():
    def __init__(
        name: str,
        type_annotation: Optional[FakeAnnotation],
        default: Optional[TypeConstant] = None,
        prefix: str = '',
    ):
```

Method or function argument.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py#L42)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Argument().is_kwflag

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py#L39)

```python
def is_kwflag() -> bool:
```

### Argument.kwflag

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py#L35)

```python
@classmethod
def kwflag() -> _R:
```

### Argument().required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/argument.py#L51)

```python
@property
def required() -> bool:
```
