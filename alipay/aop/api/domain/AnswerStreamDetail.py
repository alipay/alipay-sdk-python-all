#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerStreamDetail(object):

    def __init__(self):
        self._follow_question = None
        self._stream_out = None

    @property
    def follow_question(self):
        return self._follow_question

    @follow_question.setter
    def follow_question(self, value):
        self._follow_question = value
    @property
    def stream_out(self):
        return self._stream_out

    @stream_out.setter
    def stream_out(self, value):
        self._stream_out = value


    def to_alipay_dict(self):
        params = dict()
        if self.follow_question:
            if hasattr(self.follow_question, 'to_alipay_dict'):
                params['follow_question'] = self.follow_question.to_alipay_dict()
            else:
                params['follow_question'] = self.follow_question
        if self.stream_out:
            if hasattr(self.stream_out, 'to_alipay_dict'):
                params['stream_out'] = self.stream_out.to_alipay_dict()
            else:
                params['stream_out'] = self.stream_out
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerStreamDetail()
        if 'follow_question' in d:
            o.follow_question = d['follow_question']
        if 'stream_out' in d:
            o.stream_out = d['stream_out']
        return o


