#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HitSegmentScoreDetail(object):

    def __init__(self):
        self._full_text_score = None
        self._score = None
        self._vector_score = None

    @property
    def full_text_score(self):
        return self._full_text_score

    @full_text_score.setter
    def full_text_score(self, value):
        self._full_text_score = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def vector_score(self):
        return self._vector_score

    @vector_score.setter
    def vector_score(self, value):
        self._vector_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.full_text_score:
            if hasattr(self.full_text_score, 'to_alipay_dict'):
                params['full_text_score'] = self.full_text_score.to_alipay_dict()
            else:
                params['full_text_score'] = self.full_text_score
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.vector_score:
            if hasattr(self.vector_score, 'to_alipay_dict'):
                params['vector_score'] = self.vector_score.to_alipay_dict()
            else:
                params['vector_score'] = self.vector_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HitSegmentScoreDetail()
        if 'full_text_score' in d:
            o.full_text_score = d['full_text_score']
        if 'score' in d:
            o.score = d['score']
        if 'vector_score' in d:
            o.vector_score = d['vector_score']
        return o


