#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FqNumChargeInfo(object):

    def __init__(self):
        self._term = None

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value


    def to_alipay_dict(self):
        params = dict()
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FqNumChargeInfo()
        if 'term' in d:
            o.term = d['term']
        return o


