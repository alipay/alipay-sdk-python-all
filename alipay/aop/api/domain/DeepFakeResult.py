#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeepFakeResult(object):

    def __init__(self):
        self._fake_reason = None
        self._result = None
        self._score = None

    @property
    def fake_reason(self):
        return self._fake_reason

    @fake_reason.setter
    def fake_reason(self, value):
        self._fake_reason = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.fake_reason:
            if hasattr(self.fake_reason, 'to_alipay_dict'):
                params['fake_reason'] = self.fake_reason.to_alipay_dict()
            else:
                params['fake_reason'] = self.fake_reason
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
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
        o = DeepFakeResult()
        if 'fake_reason' in d:
            o.fake_reason = d['fake_reason']
        if 'result' in d:
            o.result = d['result']
        if 'score' in d:
            o.score = d['score']
        return o


