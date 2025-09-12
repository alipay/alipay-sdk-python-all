#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HitSegmentMetaDetail import HitSegmentMetaDetail
from alipay.aop.api.domain.HitSegmentScoreDetail import HitSegmentScoreDetail


class HitSegmentDetail(object):

    def __init__(self):
        self._content = None
        self._meta = None
        self._score = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        if isinstance(value, HitSegmentMetaDetail):
            self._meta = value
        else:
            self._meta = HitSegmentMetaDetail.from_alipay_dict(value)
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, HitSegmentScoreDetail):
            self._score = value
        else:
            self._score = HitSegmentScoreDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.meta:
            if hasattr(self.meta, 'to_alipay_dict'):
                params['meta'] = self.meta.to_alipay_dict()
            else:
                params['meta'] = self.meta
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
        o = HitSegmentDetail()
        if 'content' in d:
            o.content = d['content']
        if 'meta' in d:
            o.meta = d['meta']
        if 'score' in d:
            o.score = d['score']
        return o


