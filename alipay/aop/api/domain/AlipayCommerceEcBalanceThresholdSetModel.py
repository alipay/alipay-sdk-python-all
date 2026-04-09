#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcBalanceThresholdSetModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._threshold = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcBalanceThresholdSetModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'threshold' in d:
            o.threshold = d['threshold']
        return o


