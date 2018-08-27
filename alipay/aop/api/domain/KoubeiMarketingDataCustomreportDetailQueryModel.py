#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataCustomreportDetailQueryModel(object):

    def __init__(self):
        self._condition_key = None

    @property
    def condition_key(self):
        return self._condition_key

    @condition_key.setter
    def condition_key(self, value):
        self._condition_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_key:
            if hasattr(self.condition_key, 'to_alipay_dict'):
                params['condition_key'] = self.condition_key.to_alipay_dict()
            else:
                params['condition_key'] = self.condition_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataCustomreportDetailQueryModel()
        if 'condition_key' in d:
            o.condition_key = d['condition_key']
        return o


