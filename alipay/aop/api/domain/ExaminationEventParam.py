#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookTimeParam import BookTimeParam


class ExaminationEventParam(object):

    def __init__(self):
        self._book_time = None
        self._check_no = None

    @property
    def book_time(self):
        return self._book_time

    @book_time.setter
    def book_time(self, value):
        if isinstance(value, BookTimeParam):
            self._book_time = value
        else:
            self._book_time = BookTimeParam.from_alipay_dict(value)
    @property
    def check_no(self):
        return self._check_no

    @check_no.setter
    def check_no(self, value):
        self._check_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_time:
            if hasattr(self.book_time, 'to_alipay_dict'):
                params['book_time'] = self.book_time.to_alipay_dict()
            else:
                params['book_time'] = self.book_time
        if self.check_no:
            if hasattr(self.check_no, 'to_alipay_dict'):
                params['check_no'] = self.check_no.to_alipay_dict()
            else:
                params['check_no'] = self.check_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationEventParam()
        if 'book_time' in d:
            o.book_time = d['book_time']
        if 'check_no' in d:
            o.check_no = d['check_no']
        return o


