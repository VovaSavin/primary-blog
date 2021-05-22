from django.core.mail import send_mail


def mailing(theme: str, text: str, list_recipients: list):
    """Сервисная функция для розсылки новых уведомлений на почти подписавшихся"""
    send_mail(
        theme,
        text,
        "volodimirsavin56@gmail.com",
        list_recipients,
    )
    return True
