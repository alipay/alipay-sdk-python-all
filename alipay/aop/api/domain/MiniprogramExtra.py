#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniprogramExtra(object):

    def __init__(self):
        self._commission_type = None

    @property
    def commission_type(self):
        return self._commission_type

    @commission_type.setter
    def commission_type(self, value):
        self._commission_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_type:
            if hasattr(self.commission_type, 'to_alipay_dict'):
                params['commission_type'] = self.commission_type.to_alipay_dict()
            else:
                params['commission_type'] = self.commission_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniprogramExtra()
        if 'commission_type' in d:
            o.commission_type = d['commission_type']
        return o


