#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleInspectReportAnswerVO(object):

    def __init__(self):
        self._defect_option = None
        self._option_code = None
        self._option_name = None

    @property
    def defect_option(self):
        return self._defect_option

    @defect_option.setter
    def defect_option(self, value):
        self._defect_option = value
    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_name(self):
        return self._option_name

    @option_name.setter
    def option_name(self, value):
        self._option_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.defect_option:
            if hasattr(self.defect_option, 'to_alipay_dict'):
                params['defect_option'] = self.defect_option.to_alipay_dict()
            else:
                params['defect_option'] = self.defect_option
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_name:
            if hasattr(self.option_name, 'to_alipay_dict'):
                params['option_name'] = self.option_name.to_alipay_dict()
            else:
                params['option_name'] = self.option_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInspectReportAnswerVO()
        if 'defect_option' in d:
            o.defect_option = d['defect_option']
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_name' in d:
            o.option_name = d['option_name']
        return o


