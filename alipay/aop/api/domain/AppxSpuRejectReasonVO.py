#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppxSpuRejectReasonVO(object):

    def __init__(self):
        self._remark = None
        self._risk_name = None

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.risk_name:
            if hasattr(self.risk_name, 'to_alipay_dict'):
                params['risk_name'] = self.risk_name.to_alipay_dict()
            else:
                params['risk_name'] = self.risk_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppxSpuRejectReasonVO()
        if 'remark' in d:
            o.remark = d['remark']
        if 'risk_name' in d:
            o.risk_name = d['risk_name']
        return o


