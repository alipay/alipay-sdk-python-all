#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpProductCodeModifyModel(object):

    def __init__(self):
        self._code_id = None

    @property
    def code_id(self):
        return self._code_id

    @code_id.setter
    def code_id(self, value):
        self._code_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_id:
            if hasattr(self.code_id, 'to_alipay_dict'):
                params['code_id'] = self.code_id.to_alipay_dict()
            else:
                params['code_id'] = self.code_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpProductCodeModifyModel()
        if 'code_id' in d:
            o.code_id = d['code_id']
        return o


