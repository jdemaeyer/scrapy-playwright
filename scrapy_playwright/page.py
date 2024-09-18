from typing import Any, Callable, Union

from playwright.async_api import Page


__all__ = ["PageMethod"]


class PageMethod:
    """
    Represents a method to be called (and awaited if necessary) on a
    Playwright page, such as "click", "screenshot", "evaluate", etc.

    If a callable is received, it will be called with the page as its first argument.
    Any additional arguments are passed positionally to the callable after the page.
    """

    def __init__(self, method: Union[str, Callable[[Page], Any]], *args, **kwargs) -> None:
        self.method: Union[str, Callable[[Page], Any]] = method
        self.args: tuple = args
        self.kwargs: dict = kwargs
        self.result: Any = None

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} for method '{self.method}'>"

    __repr__ = __str__
