#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenapiInterviewProcessItem(object):

    def __init__(self):
        self._ai_interview_code = None
        self._ai_interview_name = None

    @property
    def ai_interview_code(self):
        return self._ai_interview_code

    @ai_interview_code.setter
    def ai_interview_code(self, value):
        self._ai_interview_code = value
    @property
    def ai_interview_name(self):
        return self._ai_interview_name

    @ai_interview_name.setter
    def ai_interview_name(self, value):
        self._ai_interview_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_code:
            if hasattr(self.ai_interview_code, 'to_alipay_dict'):
                params['ai_interview_code'] = self.ai_interview_code.to_alipay_dict()
            else:
                params['ai_interview_code'] = self.ai_interview_code
        if self.ai_interview_name:
            if hasattr(self.ai_interview_name, 'to_alipay_dict'):
                params['ai_interview_name'] = self.ai_interview_name.to_alipay_dict()
            else:
                params['ai_interview_name'] = self.ai_interview_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenapiInterviewProcessItem()
        if 'ai_interview_code' in d:
            o.ai_interview_code = d['ai_interview_code']
        if 'ai_interview_name' in d:
            o.ai_interview_name = d['ai_interview_name']
        return o


