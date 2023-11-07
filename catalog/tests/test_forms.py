from django.test import TestCase
from django.utils import timezone

from catalog.forms import RenewBookForm

import datetime

class RenewBookFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        conditions = form.fields['renewal_date'].label is None or form.fields['renewal_date'].label == 'renewal_date'
        self.assertTrue(conditions)

    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        hint = 'Enter a date between now and 4 weeks (default 3).'
        self.assertEqual(form.fields['renewal_date'].help_text, hint)

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4, days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())