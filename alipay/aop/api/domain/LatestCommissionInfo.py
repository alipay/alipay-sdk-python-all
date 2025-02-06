#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LatestCommissionInfo(object):

    def __init__(self):
        self._latest_rate = None
        self._latest_status = None

    @property
    def latest_rate(self):
        return self._latest_rate

    @latest_rate.setter
    def latest_rate(self, value):
        self._latest_rate = value
    @property
    def latest_status(self):
        return self._latest_status

    @latest_status.setter
    def latest_status(self, value):
        self._latest_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.latest_rate:
            if hasattr(self.latest_rate, 'to_alipay_dict'):
                params['latest_rate'] = self.latest_rate.to_alipay_dict()
            else:
                params['latest_rate'] = self.latest_rate
        if self.latest_status:
            if hasattr(self.latest_status, 'to_alipay_dict'):
                params['latest_status'] = self.latest_status.to_alipay_dict()
            else:
                params['latest_status'] = self.latest_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LatestCommissionInfo()
        if 'latest_rate' in d:
            o.latest_rate = d['latest_rate']
        if 'latest_status' in d:
            o.latest_status = d['latest_status']
        return o


