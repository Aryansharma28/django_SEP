"""Email backend that writes messages to a file."""

import datetime
import os

# For Custom Coverage
import json

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

class EmailBackend(ConsoleEmailBackend):
    def __init__(self, *args, file_path=None, **kwargs):
        self._fname = None

        coverage_json_path = "my-coverage.json"
        with open(coverage_json_path, 'r') as file:
            coverage_json = json.load(file)
            file.close()

        if file_path is not None:
            # ID: K11
            coverage_json["K11"]["covered"] = 'true'
            self.file_path = file_path
        else:
            # ID: K12
            coverage_json["K12"]["covered"] = 'true'
            self.file_path = getattr(settings, "EMAIL_FILE_PATH", None)
        self.file_path = os.path.abspath(self.file_path)
        try:
            os.makedirs(self.file_path, exist_ok=True)
        except FileExistsError:
            # ID: K13
            coverage_json["K13"]["covered"] = 'true'
            with open(coverage_json_path, 'w') as file2:
                json.dump(coverage_json, file2, indent=4)
                file2.close()
            raise ImproperlyConfigured(
                "Path for saving email messages exists, but is not a directory: %s"
                % self.file_path
            )
        except OSError as err:
            # ID: K14
            coverage_json["K14"]["covered"] = 'true'
            with open(coverage_json_path, 'w') as file2:
                json.dump(coverage_json, file2, indent=4)
                file2.close()
            raise ImproperlyConfigured(
                "Could not create directory for saving email messages: %s (%s)"
                % (self.file_path, err)
            )
        # Make sure that self.file_path is writable.
        if not os.access(self.file_path, os.W_OK):
            # ID: K15
            coverage_json["K15"]["covered"] = 'true'
            with open(coverage_json_path, 'w') as file2:
                json.dump(coverage_json, file2, indent=4)
                file2.close()
            raise ImproperlyConfigured(
                "Could not write to directory: %s" % self.file_path
            )
        # Finally, call super().
        # Since we're using the console-based backend as a base,
        # force the stream to be None, so we don't default to stdout

        # ID: K16
        coverage_json["K16"]["covered"] = 'true'
        kwargs["stream"] = None
        # print_email_backend_coverage()
        with open(coverage_json_path, 'w') as file2:
            json.dump(coverage_json, file2, indent=4)
            file2.close()
        super().__init__(*args, **kwargs)

    def write_message(self, message):
        self.stream.write(message.message().as_bytes() + b"\n")
        self.stream.write(b"-" * 79)
        self.stream.write(b"\n")

    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.log" % (timestamp, abs(id(self)))
            self._fname = os.path.join(self.file_path, fname)
        return self._fname

    def open(self):
        coverage_json_path = "my-coverage.json"
        with open(coverage_json_path, 'r') as file:
            coverage_json = json.load(file)
            file.close()

        if self.stream is None:
            # ID: K21
            coverage_json["K21"]["covered"] = 'true'

            with open(coverage_json_path, 'w') as file2:
                json.dump(coverage_json, file2, indent=4)
                file2.close()

            self.stream = open(self._get_filename(), "ab")
            return True

        # ID: K22
        coverage_json["K22"]["covered"] = 'true'

        with open(coverage_json_path, 'w') as file2:
            json.dump(coverage_json, file2, indent=4)
            file2.close()
        return False

    def close(self):
        try:
            if self.stream is not None:
                self.stream.close()
        finally:
            self.stream = None
