#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQuestionOptionInfo import RecycleQuestionOptionInfo


class RecycleQuestion(object):

    def __init__(self):
        self._option_list = None
        self._question_code = None
        self._question_name = None

    @property
    def option_list(self):
        return self._option_list

    @option_list.setter
    def option_list(self, value):
        if isinstance(value, list):
            self._option_list = list()
            for i in value:
                if isinstance(i, RecycleQuestionOptionInfo):
                    self._option_list.append(i)
                else:
                    self._option_list.append(RecycleQuestionOptionInfo.from_alipay_dict(i))
    @property
    def question_code(self):
        return self._question_code

    @question_code.setter
    def question_code(self, value):
        self._question_code = value
    @property
    def question_name(self):
        return self._question_name

    @question_name.setter
    def question_name(self, value):
        self._question_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.option_list:
            if isinstance(self.option_list, list):
                for i in range(0, len(self.option_list)):
                    element = self.option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.option_list[i] = element.to_alipay_dict()
            if hasattr(self.option_list, 'to_alipay_dict'):
                params['option_list'] = self.option_list.to_alipay_dict()
            else:
                params['option_list'] = self.option_list
        if self.question_code:
            if hasattr(self.question_code, 'to_alipay_dict'):
                params['question_code'] = self.question_code.to_alipay_dict()
            else:
                params['question_code'] = self.question_code
        if self.question_name:
            if hasattr(self.question_name, 'to_alipay_dict'):
                params['question_name'] = self.question_name.to_alipay_dict()
            else:
                params['question_name'] = self.question_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQuestion()
        if 'option_list' in d:
            o.option_list = d['option_list']
        if 'question_code' in d:
            o.question_code = d['question_code']
        if 'question_name' in d:
            o.question_name = d['question_name']
        return o


