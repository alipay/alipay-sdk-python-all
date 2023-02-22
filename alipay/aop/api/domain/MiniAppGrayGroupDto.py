#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppGrayGroupDto(object):

    def __init__(self):
        self._gray_code = None
        self._name = None

    @property
    def gray_code(self):
        return self._gray_code

    @gray_code.setter
    def gray_code(self, value):
        self._gray_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.gray_code:
            if hasattr(self.gray_code, 'to_alipay_dict'):
                params['gray_code'] = self.gray_code.to_alipay_dict()
            else:
                params['gray_code'] = self.gray_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppGrayGroupDto()
        if 'gray_code' in d:
            o.gray_code = d['gray_code']
        if 'name' in d:
            o.name = d['name']
        return o


