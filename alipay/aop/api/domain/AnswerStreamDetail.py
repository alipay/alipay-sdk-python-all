#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerStreamDetail(object):

    def __init__(self):
        self._follow_question = None
        self._general_bottom_line_answer = None
        self._general_bottom_line_answer_hint = None
        self._stream_out = None

    @property
    def follow_question(self):
        return self._follow_question

    @follow_question.setter
    def follow_question(self, value):
        self._follow_question = value
    @property
    def general_bottom_line_answer(self):
        return self._general_bottom_line_answer

    @general_bottom_line_answer.setter
    def general_bottom_line_answer(self, value):
        self._general_bottom_line_answer = value
    @property
    def general_bottom_line_answer_hint(self):
        return self._general_bottom_line_answer_hint

    @general_bottom_line_answer_hint.setter
    def general_bottom_line_answer_hint(self, value):
        self._general_bottom_line_answer_hint = value
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
        if self.general_bottom_line_answer:
            if hasattr(self.general_bottom_line_answer, 'to_alipay_dict'):
                params['general_bottom_line_answer'] = self.general_bottom_line_answer.to_alipay_dict()
            else:
                params['general_bottom_line_answer'] = self.general_bottom_line_answer
        if self.general_bottom_line_answer_hint:
            if hasattr(self.general_bottom_line_answer_hint, 'to_alipay_dict'):
                params['general_bottom_line_answer_hint'] = self.general_bottom_line_answer_hint.to_alipay_dict()
            else:
                params['general_bottom_line_answer_hint'] = self.general_bottom_line_answer_hint
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
        if 'general_bottom_line_answer' in d:
            o.general_bottom_line_answer = d['general_bottom_line_answer']
        if 'general_bottom_line_answer_hint' in d:
            o.general_bottom_line_answer_hint = d['general_bottom_line_answer_hint']
        if 'stream_out' in d:
            o.stream_out = d['stream_out']
        return o


