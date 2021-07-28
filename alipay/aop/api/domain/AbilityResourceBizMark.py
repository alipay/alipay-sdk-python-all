#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AbilityResourceBizMark(object):

    def __init__(self):
        self._biz_code = None
        self._execution_time = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def execution_time(self):
        return self._execution_time

    @execution_time.setter
    def execution_time(self, value):
        self._execution_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.execution_time:
            if hasattr(self.execution_time, 'to_alipay_dict'):
                params['execution_time'] = self.execution_time.to_alipay_dict()
            else:
                params['execution_time'] = self.execution_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AbilityResourceBizMark()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'execution_time' in d:
            o.execution_time = d['execution_time']
        return o


