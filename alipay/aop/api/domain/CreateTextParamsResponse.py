#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreateTextParamsResponse(object):

    def __init__(self):
        self._push_bailingual_flag = None

    @property
    def push_bailingual_flag(self):
        return self._push_bailingual_flag

    @push_bailingual_flag.setter
    def push_bailingual_flag(self, value):
        self._push_bailingual_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.push_bailingual_flag:
            if hasattr(self.push_bailingual_flag, 'to_alipay_dict'):
                params['push_bailingual_flag'] = self.push_bailingual_flag.to_alipay_dict()
            else:
                params['push_bailingual_flag'] = self.push_bailingual_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateTextParamsResponse()
        if 'push_bailingual_flag' in d:
            o.push_bailingual_flag = d['push_bailingual_flag']
        return o


