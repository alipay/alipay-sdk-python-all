#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfOrderMemoInfo(object):

    def __init__(self):
        self._bd_name = None
        self._other_memo = None

    @property
    def bd_name(self):
        return self._bd_name

    @bd_name.setter
    def bd_name(self, value):
        self._bd_name = value
    @property
    def other_memo(self):
        return self._other_memo

    @other_memo.setter
    def other_memo(self, value):
        self._other_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_name:
            if hasattr(self.bd_name, 'to_alipay_dict'):
                params['bd_name'] = self.bd_name.to_alipay_dict()
            else:
                params['bd_name'] = self.bd_name
        if self.other_memo:
            if hasattr(self.other_memo, 'to_alipay_dict'):
                params['other_memo'] = self.other_memo.to_alipay_dict()
            else:
                params['other_memo'] = self.other_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfOrderMemoInfo()
        if 'bd_name' in d:
            o.bd_name = d['bd_name']
        if 'other_memo' in d:
            o.other_memo = d['other_memo']
        return o


