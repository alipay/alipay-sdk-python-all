#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentContractDictVo(object):

    def __init__(self):
        self._code = None
        self._desc = None
        self._dict_content = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def dict_content(self):
        return self._dict_content

    @dict_content.setter
    def dict_content(self, value):
        self._dict_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.dict_content:
            if hasattr(self.dict_content, 'to_alipay_dict'):
                params['dict_content'] = self.dict_content.to_alipay_dict()
            else:
                params['dict_content'] = self.dict_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentContractDictVo()
        if 'code' in d:
            o.code = d['code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'dict_content' in d:
            o.dict_content = d['dict_content']
        return o


