"""
Parent class for all type annotation wrappers.
"""
from abc import ABC, abstractmethod
from typing import Any, Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class FakeAnnotation(ABC):
    """
    Parent class for all type annotation wrappers.
    """

    def __hash__(self) -> int:
        return hash(self.render())

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FakeAnnotation):
            raise ValueError(f"Cannot compare FakeAnnotation with {other}")

        return self.get_sort_key() == other.get_sort_key()

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, FakeAnnotation):
            raise ValueError(f"Cannot compare FakeAnnotation with {other}")

        return not self == other

    def __gt__(self, other: "FakeAnnotation") -> bool:
        return self.get_sort_key() > other.get_sort_key()

    def __lt__(self, other: "FakeAnnotation") -> bool:
        return not self > other

    def get_sort_key(self) -> str:
        """
        Get string to sort annotations.
        """
        return str(self)

    def __str__(self) -> str:
        return self.render()

    @abstractmethod
    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.
        """

    @abstractmethod
    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """

    def get_types(self) -> Set["FakeAnnotation"]:
        """
        Get all used type annotations recursively including self.
        """
        return {self}

    def add_child(self, child: "FakeAnnotation") -> None:
        """
        Add new child to `TypeSubscript` or `TypeTypedDict` annotation.
        """

    def is_dict(self) -> bool:
        """
        Whether type annotation is `Dict` or `TypedDict`.
        """
        return False

    def is_typed_dict(self) -> bool:
        """
        Whether type annotation is `TypedDict`.
        """
        return False

    def is_list(self) -> bool:
        """
        Whether type annotation is `List`.
        """
        return False

    def is_literal(self) -> bool:
        """
        Whether type annotation is `Literal`.
        """
        return False

    @abstractmethod
    def copy(self) -> "FakeAnnotation":
        """
        Create a copy of type annotation wrapper.
        """
