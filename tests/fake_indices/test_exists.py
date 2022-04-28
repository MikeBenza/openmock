# -*- coding: utf-8 -*-

from tests import Testopenmock, INDEX_NAME


class TestExists(Testopenmock):

    def test_should_return_false_when_index_does_not_exists(self):
        self.assertFalse(self.es.indices.exists(INDEX_NAME))

    def test_should_return_true_when_index_exists(self):
        self.es.indices.create(INDEX_NAME)
        self.assertTrue(self.es.indices.exists(INDEX_NAME))
