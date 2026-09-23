#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Options(object):

    def __init__(self):
        self._content = None
        self._correct = None
        self._option_id = None
        self._score = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def correct(self):
        return self._correct

    @correct.setter
    def correct(self, value):
        self._correct = value
    @property
    def option_id(self):
        return self._option_id

    @option_id.setter
    def option_id(self, value):
        self._option_id = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.correct:
            if hasattr(self.correct, 'to_alipay_dict'):
                params['correct'] = self.correct.to_alipay_dict()
            else:
                params['correct'] = self.correct
        if self.option_id:
            if hasattr(self.option_id, 'to_alipay_dict'):
                params['option_id'] = self.option_id.to_alipay_dict()
            else:
                params['option_id'] = self.option_id
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
        o = Options()
        if 'content' in d:
            o.content = d['content']
        if 'correct' in d:
            o.correct = d['correct']
        if 'option_id' in d:
            o.option_id = d['option_id']
        if 'score' in d:
            o.score = d['score']
        return o


