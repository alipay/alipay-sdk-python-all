#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenFormFieldDO(object):

    def __init__(self):
        self._optional = None
        self._required = None

    @property
    def optional(self):
        return self._optional

    @optional.setter
    def optional(self, value):
        self._optional = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.optional:
            if hasattr(self.optional, 'to_alipay_dict'):
                params['optional'] = self.optional.to_alipay_dict()
            else:
                params['optional'] = self.optional
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenFormFieldDO()
        if 'optional' in d:
            o.optional = d['optional']
        if 'required' in d:
            o.required = d['required']
        return o


