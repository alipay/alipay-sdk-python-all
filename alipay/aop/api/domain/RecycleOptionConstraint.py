#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOptionConstraint(object):

    def __init__(self):
        self._question_code = None
        self._retain_options = None
        self._selected_option_code = None

    @property
    def question_code(self):
        return self._question_code

    @question_code.setter
    def question_code(self, value):
        self._question_code = value
    @property
    def retain_options(self):
        return self._retain_options

    @retain_options.setter
    def retain_options(self, value):
        if isinstance(value, list):
            self._retain_options = list()
            for i in value:
                self._retain_options.append(i)
    @property
    def selected_option_code(self):
        return self._selected_option_code

    @selected_option_code.setter
    def selected_option_code(self, value):
        self._selected_option_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.question_code:
            if hasattr(self.question_code, 'to_alipay_dict'):
                params['question_code'] = self.question_code.to_alipay_dict()
            else:
                params['question_code'] = self.question_code
        if self.retain_options:
            if isinstance(self.retain_options, list):
                for i in range(0, len(self.retain_options)):
                    element = self.retain_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.retain_options[i] = element.to_alipay_dict()
            if hasattr(self.retain_options, 'to_alipay_dict'):
                params['retain_options'] = self.retain_options.to_alipay_dict()
            else:
                params['retain_options'] = self.retain_options
        if self.selected_option_code:
            if hasattr(self.selected_option_code, 'to_alipay_dict'):
                params['selected_option_code'] = self.selected_option_code.to_alipay_dict()
            else:
                params['selected_option_code'] = self.selected_option_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOptionConstraint()
        if 'question_code' in d:
            o.question_code = d['question_code']
        if 'retain_options' in d:
            o.retain_options = d['retain_options']
        if 'selected_option_code' in d:
            o.selected_option_code = d['selected_option_code']
        return o


