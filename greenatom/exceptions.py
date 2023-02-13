"""Exceptions file."""


class WrongInputData(Exception):

    def __init__(self, url: str, body: str) -> None:
        """Initialization funcrion.

        Args:
            url (str): request's url.
            body (str): request's body.
        """
        super().__init__(url, body)
        self.url = url
        self.body = body

    def __str__(self) -> str:
        """Exception in special format."""
        return "Impossible to get graphql data with url: {0} and body {1}!".format(self.url, self.body)
