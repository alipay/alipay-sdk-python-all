#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookInfoModify(object):

    def __init__(self):
        self._book_table_position = None
        self._book_timeout = None

    @property
    def book_table_position(self):
        return self._book_table_position

    @book_table_position.setter
    def book_table_position(self, value):
        self._book_table_position = value
    @property
    def book_timeout(self):
        return self._book_timeout

    @book_timeout.setter
    def book_timeout(self, value):
        self._book_timeout = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_table_position:
            if hasattr(self.book_table_position, 'to_alipay_dict'):
                params['book_table_position'] = self.book_table_position.to_alipay_dict()
            else:
                params['book_table_position'] = self.book_table_position
        if self.book_timeout:
            if hasattr(self.book_timeout, 'to_alipay_dict'):
                params['book_timeout'] = self.book_timeout.to_alipay_dict()
            else:
                params['book_timeout'] = self.book_timeout
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookInfoModify()
        if 'book_table_position' in d:
            o.book_table_position = d['book_table_position']
        if 'book_timeout' in d:
            o.book_timeout = d['book_timeout']
        return o


