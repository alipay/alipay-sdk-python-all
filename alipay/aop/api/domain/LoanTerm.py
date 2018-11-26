#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanTerm(object):

    def __init__(self):
        self._term = None
        self._term_unit = None

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def term_unit(self):
        return self._term_unit

    @term_unit.setter
    def term_unit(self, value):
        self._term_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        if self.term_unit:
            if hasattr(self.term_unit, 'to_alipay_dict'):
                params['term_unit'] = self.term_unit.to_alipay_dict()
            else:
                params['term_unit'] = self.term_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanTerm()
        if 'term' in d:
            o.term = d['term']
        if 'term_unit' in d:
            o.term_unit = d['term_unit']
        return o


