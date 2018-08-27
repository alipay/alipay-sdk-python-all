#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliTrustScore(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AliTrustScore()
        if 'score' in d:
            o.score = d['score']
        return o


