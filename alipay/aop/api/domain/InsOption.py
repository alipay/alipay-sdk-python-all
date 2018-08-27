#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOption(object):

    def __init__(self):
        self._coverage = None
        self._coverage_text = None

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value
    @property
    def coverage_text(self):
        return self._coverage_text

    @coverage_text.setter
    def coverage_text(self, value):
        self._coverage_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.coverage:
            if hasattr(self.coverage, 'to_alipay_dict'):
                params['coverage'] = self.coverage.to_alipay_dict()
            else:
                params['coverage'] = self.coverage
        if self.coverage_text:
            if hasattr(self.coverage_text, 'to_alipay_dict'):
                params['coverage_text'] = self.coverage_text.to_alipay_dict()
            else:
                params['coverage_text'] = self.coverage_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOption()
        if 'coverage' in d:
            o.coverage = d['coverage']
        if 'coverage_text' in d:
            o.coverage_text = d['coverage_text']
        return o


