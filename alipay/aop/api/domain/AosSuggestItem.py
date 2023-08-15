#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AosSuggestItem(object):

    def __init__(self):
        self._biz_trace_id = None
        self._score = None
        self._sequence = None
        self._title = None
        self._trace_id = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trace_id:
            if hasattr(self.biz_trace_id, 'to_alipay_dict'):
                params['biz_trace_id'] = self.biz_trace_id.to_alipay_dict()
            else:
                params['biz_trace_id'] = self.biz_trace_id
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AosSuggestItem()
        if 'biz_trace_id' in d:
            o.biz_trace_id = d['biz_trace_id']
        if 'score' in d:
            o.score = d['score']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'title' in d:
            o.title = d['title']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


