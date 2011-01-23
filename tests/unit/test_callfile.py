"""Unit tests for `pycall.callfile`."""

from unittest import TestCase

from nose.tools import assert_false, eq_, ok_, raises

from pycall import Application, Call, CallFile


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.call = Call('local/18882223333@outgoing')
		self.action = Application('Playback', 'hello-world')
		self.spool_dir = '/'

	@raises(TypeError)
	def test_create_callfile(self):
		"""Ensure creating an empty `CallFile` object fails."""
		CallFile()

	def test_callfile_attrs(self):
		"""Ensure `CallFile` attributes stick."""
		c = CallFile(0, 1, 2, 3, 4, 5, 6, 7)
		eq_(c.call, 0)
		eq_(c.action, 1)
		eq_(c.set_var, 2)
		eq_(c.archive, 3)
		eq_(c.user, 4)
		eq_(c.tmpdir, 5)
		eq_(c.file_name, 6)
		eq_(c.spool_dir, 7)

	def test_is_valid_valid_call_and_valid_action_and_valid_spool_dir(self):
		"""Ensure `is_valid` works with well-formed `call`, `action`, and
		`spool_dir` attributes."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_call(self):
		"""Ensure `is_valid` fails with an invalid `call` attribute."""
		c = CallFile('call', self.action, spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_call_validation(self):
		"""Ensure that the `call` attribute's `is_valid` method fails if the
		`Call` object is invalid.
		"""
		c = CallFile(Call('local/18882223333@outgoing', wait_time='wait_time'),
				self.action, spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_action(self):
		"""Ensure `is_valid` fails with an invalid `action` attribute."""
		c = CallFile(self.call, 'action', spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_valid_set_var(self):
		"""Ensure `is_valid` works with a well-formed `set_var` attribute."""
		c = CallFile(self.call, self.action, set_var={'a': 'b'},
				spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_set_var(self):
		"""Ensure `is_valid` fails with an invalid `set_var` attribute."""
		c = CallFile(self.call, self.action, set_var='set_var',
				spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_valid_tmpdir(self):
		"""Ensure `is_valid` works with a well-formed `tmpdir` attribute."""
		c = CallFile(self.call, self.action, tmpdir='/',
				spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_tmpdir(self):
		"""Ensure `is_valid` fails with an invalid `tmpdir` attribute."""
		c = CallFile(self.call, self.action, tmpdir='tmpdir',
				spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_spool_dir(self):
		"""Ensure `is_valid` fails with an invalid `spool_dir` attribute."""
		c = CallFile(self.call, self.action, spool_dir='spool_dir')
		assert_false(c.is_valid())