#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleQuestionOptionInfo(object):

    def __init__(self):
        self._option_code = None
        self._option_value = None
        self._question_code = None

    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_value(self):
        return self._option_value

    @option_value.setter
    def option_value(self, value):
        self._option_value = value
    @property
    def question_code(self):
        return self._question_code

    @question_code.setter
    def question_code(self, value):
        self._question_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_value:
            if hasattr(self.option_value, 'to_alipay_dict'):
                params['option_value'] = self.option_value.to_alipay_dict()
            else:
                params['option_value'] = self.option_value
        if self.question_code:
            if hasattr(self.question_code, 'to_alipay_dict'):
                params['question_code'] = self.question_code.to_alipay_dict()
            else:
                params['question_code'] = self.question_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQuestionOptionInfo()
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_value' in d:
            o.option_value = d['option_value']
        if 'question_code' in d:
            o.question_code = d['question_code']
        return o


