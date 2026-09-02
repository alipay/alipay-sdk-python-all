#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookTimeParam(object):

    def __init__(self):
        self._book_end_time = None
        self._book_start_time = None

    @property
    def book_end_time(self):
        return self._book_end_time

    @book_end_time.setter
    def book_end_time(self, value):
        self._book_end_time = value
    @property
    def book_start_time(self):
        return self._book_start_time

    @book_start_time.setter
    def book_start_time(self, value):
        self._book_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_end_time:
            if hasattr(self.book_end_time, 'to_alipay_dict'):
                params['book_end_time'] = self.book_end_time.to_alipay_dict()
            else:
                params['book_end_time'] = self.book_end_time
        if self.book_start_time:
            if hasattr(self.book_start_time, 'to_alipay_dict'):
                params['book_start_time'] = self.book_start_time.to_alipay_dict()
            else:
                params['book_start_time'] = self.book_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookTimeParam()
        if 'book_end_time' in d:
            o.book_end_time = d['book_end_time']
        if 'book_start_time' in d:
            o.book_start_time = d['book_start_time']
        return o


