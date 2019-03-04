#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CodeResInfo(object):

    def __init__(self):
        self._code_id = None
        self._code_url = None

    @property
    def code_id(self):
        return self._code_id

    @code_id.setter
    def code_id(self, value):
        self._code_id = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_id:
            if hasattr(self.code_id, 'to_alipay_dict'):
                params['code_id'] = self.code_id.to_alipay_dict()
            else:
                params['code_id'] = self.code_id
        if self.code_url:
            if hasattr(self.code_url, 'to_alipay_dict'):
                params['code_url'] = self.code_url.to_alipay_dict()
            else:
                params['code_url'] = self.code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CodeResInfo()
        if 'code_id' in d:
            o.code_id = d['code_id']
        if 'code_url' in d:
            o.code_url = d['code_url']
        return o


