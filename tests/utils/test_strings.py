from mypy_boto3_builder.utils.strings import (
    get_anchor_link,
    get_class_prefix,
    get_line_with_indented,
    is_reserved,
)


class TestStrings:
    def test_get_class_prefix(self) -> None:
        assert get_class_prefix("my_func") == "MyFunc"
        assert get_class_prefix("") == ""
        assert get_class_prefix("myFunc") == "MyFunc"

    def test_get_line_with_indented(self) -> None:
        assert get_line_with_indented("a\n\nb\nc") == "a"
        assert get_line_with_indented("a\n\n b\n  c\n\n d\ne") == "a\n\n b\n  c\n\n d"
        assert get_line_with_indented(" a\n  b\n  c\n d") == " a\n  b\n  c"
        assert get_line_with_indented("") == ""
        assert get_line_with_indented("a\n\nb\n c\nd", True) == "a\n\nb\n c"
        assert get_line_with_indented(" a\n\n b\n   c\n  d\ne", True) == " a\n\n b\n   c\n   d"

    def test_get_anchor_link(self) -> None:
        assert get_anchor_link("test") == "test"
        assert get_anchor_link("n.ew_t est") == "new_t-est"

    def test_is_reserved(self) -> None:
        assert is_reserved("lambda")
        assert is_reserved("List")
        assert is_reserved("dict")
        assert not is_reserved("myname")
