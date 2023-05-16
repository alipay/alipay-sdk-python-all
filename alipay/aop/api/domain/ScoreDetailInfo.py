#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScoreDetailInfo(object):

    def __init__(self):
        self._score = None
        self._score_code = None
        self._score_name = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def score_code(self):
        return self._score_code

    @score_code.setter
    def score_code(self, value):
        self._score_code = value
    @property
    def score_name(self):
        return self._score_name

    @score_name.setter
    def score_name(self, value):
        self._score_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.score_code:
            if hasattr(self.score_code, 'to_alipay_dict'):
                params['score_code'] = self.score_code.to_alipay_dict()
            else:
                params['score_code'] = self.score_code
        if self.score_name:
            if hasattr(self.score_name, 'to_alipay_dict'):
                params['score_name'] = self.score_name.to_alipay_dict()
            else:
                params['score_name'] = self.score_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScoreDetailInfo()
        if 'score' in d:
            o.score = d['score']
        if 'score_code' in d:
            o.score_code = d['score_code']
        if 'score_name' in d:
            o.score_name = d['score_name']
        return o


