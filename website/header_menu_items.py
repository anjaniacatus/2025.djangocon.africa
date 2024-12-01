from dataclasses import dataclass, field
from typing import List

from django.urls import reverse


@dataclass
class HeaderLink:
    label: str
    href: str = ""
    children: List["HeaderLink"] = field(default_factory=list)
    action_url: str = ""

header_menu_items = [
    HeaderLink(label="Home", href="/"),
    # HeaderLink(
    #     label="About",
    #     children=[
    #         #   HeaderLink("Team", href=reverse("page_team")),
    #     ],
    # ),
]

user_loggedin_link = HeaderLink(
    label='<i class="fas fa-user"></i> User',
    children=[
        # HeaderLink("Profile", href="todo"),
        # HeaderLink("Talk Submissions", href="todo"),
        HeaderLink(label="Logout", action_url=reverse("account_logout")),
    ],
)

user_not_loggedin_link = HeaderLink(
    label='<i class="fas fa-user"></i> Login/Register', href=reverse("account_login")
)
