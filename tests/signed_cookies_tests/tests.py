from datetime import timedelta

from django.core import signing
from django.http import HttpRequest, HttpResponse
from django.test import SimpleTestCase, override_settings
from django.test.utils import freeze_time
from django.http.request import print_coverage


class SignedCookieTest(SimpleTestCase):

    def test_can_set_and_read_signed_cookies(self):
        response = HttpResponse()
        response.set_signed_cookie("c", "hello")
        self.assertIn("c", response.cookies)
        self.assertTrue(response.cookies["c"].value.startswith("hello:"))
        request = HttpRequest()
        request.COOKIES["c"] = response.cookies["c"].value
        value = request.get_signed_cookie("c")
        self.assertEqual(value, "hello")

    

    def test_can_use_salt(self):
        response = HttpResponse()
        response.set_signed_cookie("a", "hello", salt="one")
        request = HttpRequest()
        request.COOKIES["a"] = response.cookies["a"].value
        value = request.get_signed_cookie("a", salt="one")
        self.assertEqual(value, "hello")
        with self.assertRaises(signing.BadSignature):
            request.get_signed_cookie("a", salt="two")
    
    
    def test_detects_tampering(self):
        response = HttpResponse()
        response.set_signed_cookie("c", "hello")
        request = HttpRequest()
        request.COOKIES["c"] = response.cookies["c"].value[:-2] + "$$"
        with self.assertRaises(signing.BadSignature):
            request.get_signed_cookie("c")
    
    def test_key_error_scenarios(self):
        request = HttpRequest()
        
        result = request.get_signed_cookie('nonexistent_key', default='default_value')
        self.assertEqual(result, 'default_value', "Should return the default value when provided")

        with self.assertRaises(KeyError):
            request.get_signed_cookie('nonexistent_key')
        print()
        print("coverage for key error scenarios in get_signed_cookie()")
        print_coverage()


    def test_default_argument_suppresses_exceptions(self):
        response = HttpResponse()
        response.set_signed_cookie("c", "hello")
        request = HttpRequest()
        request.COOKIES["c"] = response.cookies["c"].value[:-2] + "$$"
        self.assertIsNone(request.get_signed_cookie("c", default=None))

    def test_max_age_argument(self):
        value = "hello"
        with freeze_time(123456789):
            response = HttpResponse()
            response.set_signed_cookie("c", value)
            request = HttpRequest()
            request.COOKIES["c"] = response.cookies["c"].value
            self.assertEqual(request.get_signed_cookie("c"), value)

        with freeze_time(123456800):
            self.assertEqual(request.get_signed_cookie("c", max_age=12), value)
            self.assertEqual(request.get_signed_cookie("c", max_age=11), value)
            self.assertEqual(
                request.get_signed_cookie("c", max_age=timedelta(seconds=11)), value
            )
            with self.assertRaises(signing.SignatureExpired):
                request.get_signed_cookie("c", max_age=10)
            with self.assertRaises(signing.SignatureExpired):
                request.get_signed_cookie("c", max_age=timedelta(seconds=10))
    
    

    def test_set_signed_cookie_max_age_argument(self):
        response = HttpResponse()
        response.set_signed_cookie("c", "value", max_age=100)
        self.assertEqual(response.cookies["c"]["max-age"], 100)
        response.set_signed_cookie("d", "value", max_age=timedelta(hours=2))
        self.assertEqual(response.cookies["d"]["max-age"], 7200)
    
    

    @override_settings(SECRET_KEY=b"\xe7")
    def test_signed_cookies_with_binary_key(self):
        response = HttpResponse()
        response.set_signed_cookie("c", "hello")

        request = HttpRequest()
        request.COOKIES["c"] = response.cookies["c"].value
        self.assertEqual(request.get_signed_cookie("c"), "hello")
    
    
