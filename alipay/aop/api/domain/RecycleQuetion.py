#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleOption import RecycleOption


class RecycleQuetion(object):

    def __init__(self):
        self._options = None
        self._question_code = None
        self._question_name = None

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, RecycleOption):
                    self._options.append(i)
                else:
                    self._options.append(RecycleOption.from_alipay_dict(i))
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
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
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
        o = RecycleQuetion()
        if 'options' in d:
            o.options = d['options']
        if 'question_code' in d:
            o.question_code = d['question_code']
        if 'question_name' in d:
            o.question_name = d['question_name']
        return o


