from fasthtml.common import *

from ..components.app_link import AppLink
from ..components.app_page import AppPage


def PrivacyPolicy(player: dict = None):
    return AppPage(
        Div(
            H1("Privacy Policy", cls="text-center text-3xl"),
            H2("Collection and Use of Steam Data", cls="text-lg text-center"),
            P(
                "At MySteamStats (",
                AppLink(
                    "https://www.mysteamstats.com", href="https://www.mysteamstats.com"
                ),
                '), we are committed to protecting the privacy of our users and ensuring that all nonpublic end user data, including data retrieved from Steam ("Steam Data"), is handled in accordance with this Privacy Policy.',
            ),
            Ol(
                Li(
                    "Collection of Steam Data",
                    Ul(
                        Li(
                            "We will only retrieve Steam Data about a Steam end user upon the explicit request of the end user. The Steam Data we collect may include, but is not limited to, user profile information, gameplay statistics, and any other data the user consents to share with us from their Steam account."
                        )
                    ),
                ),
                Li(
                    "User Consent and Transparency",
                    Ul(
                        Li(
                            "Prior to retrieving any Steam Data, we will clearly inform the end user about the specific data that will be accessed and the purposes for which it will be used. Users will have the opportunity to review this information and give their consent before any data retrieval takes place."
                        ),
                    ),
                ),
                Li(
                    "Storage of Steam Data",
                    Ul(
                        Li(
                            "We will store the Steam Data in the United States. These locations have been selected to ensure that the data is stored securely and in compliance with applicable data protection laws."
                        ),
                    ),
                ),
                Li(
                    "Use and Disclosure of Steam Data",
                    Ul(
                        Li(
                            "The Steam Data collected will be used solely for the purposes described at the time of collection. We will not disclose or share this data with any third parties unless required by law or with the explicit consent of the end user."
                        ),
                    ),
                ),
                Li(
                    "Data Security",
                    Ul(
                        Li(
                            "We implement appropriate technical and organizational measures to protect the Steam Data against unauthorized access, alteration, disclosure, or destruction. We regularly review our security practices to ensure the ongoing protection of your data."
                        ),
                    ),
                ),
                Li(
                    "User Rights",
                    Ul(
                        Li(
                            "Users have the right to access, correct, or request the deletion of their Steam Data at any time. If you wish to exercise these rights, please contact us via our website at ",
                            AppLink(
                                "Privacy Policy Contact Form",
                                href="/feedback?reason=Privacy Policy",
                            ),
                            ".",
                        ),
                    ),
                ),
                Li(
                    "Updates to this Policy",
                    Ul(
                        Li(
                            "We may update this Privacy Policy from time to time to reflect changes in our practices or legal obligations. We will notify users of any significant changes and obtain their consent if required."
                        ),
                    ),
                ),
                cls="list-decimal ml-4 space-y-2",
            ),
            cls="container mx-auto space-y-4",
        ),
        player=player,
        title="Privacy Policy",
    )
