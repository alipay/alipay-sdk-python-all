#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CBDMessageBody(object):

    def __init__(self):
        self._template_code = None
        self._template_data = None

    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CBDMessageBody()
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_data' in d:
            o.template_data = d['template_data']
        return o


