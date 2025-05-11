#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GeographyInfo(object):

    def __init__(self):
        self._code = None
        self._score = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GeographyInfo()
        if 'code' in d:
            o.code = d['code']
        if 'score' in d:
            o.score = d['score']
        return o


