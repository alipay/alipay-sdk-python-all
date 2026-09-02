#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleInspectAnswerVO(object):

    def __init__(self):
        self._answer_type = None
        self._answer_value = None
        self._check_pass = None
        self._check_result_code = None
        self._check_result_msg = None

    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def answer_value(self):
        return self._answer_value

    @answer_value.setter
    def answer_value(self, value):
        self._answer_value = value
    @property
    def check_pass(self):
        return self._check_pass

    @check_pass.setter
    def check_pass(self, value):
        self._check_pass = value
    @property
    def check_result_code(self):
        return self._check_result_code

    @check_result_code.setter
    def check_result_code(self, value):
        self._check_result_code = value
    @property
    def check_result_msg(self):
        return self._check_result_msg

    @check_result_msg.setter
    def check_result_msg(self, value):
        self._check_result_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer_type:
            if hasattr(self.answer_type, 'to_alipay_dict'):
                params['answer_type'] = self.answer_type.to_alipay_dict()
            else:
                params['answer_type'] = self.answer_type
        if self.answer_value:
            if hasattr(self.answer_value, 'to_alipay_dict'):
                params['answer_value'] = self.answer_value.to_alipay_dict()
            else:
                params['answer_value'] = self.answer_value
        if self.check_pass:
            if hasattr(self.check_pass, 'to_alipay_dict'):
                params['check_pass'] = self.check_pass.to_alipay_dict()
            else:
                params['check_pass'] = self.check_pass
        if self.check_result_code:
            if hasattr(self.check_result_code, 'to_alipay_dict'):
                params['check_result_code'] = self.check_result_code.to_alipay_dict()
            else:
                params['check_result_code'] = self.check_result_code
        if self.check_result_msg:
            if hasattr(self.check_result_msg, 'to_alipay_dict'):
                params['check_result_msg'] = self.check_result_msg.to_alipay_dict()
            else:
                params['check_result_msg'] = self.check_result_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInspectAnswerVO()
        if 'answer_type' in d:
            o.answer_type = d['answer_type']
        if 'answer_value' in d:
            o.answer_value = d['answer_value']
        if 'check_pass' in d:
            o.check_pass = d['check_pass']
        if 'check_result_code' in d:
            o.check_result_code = d['check_result_code']
        if 'check_result_msg' in d:
            o.check_result_msg = d['check_result_msg']
        return o


