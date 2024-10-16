#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionrecgDeviceactivationQueryModel(object):

    def __init__(self):
        self._activation_code = None
        self._biz_tid = None
        self._isv_tid = None

    @property
    def activation_code(self):
        return self._activation_code

    @activation_code.setter
    def activation_code(self, value):
        self._activation_code = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def isv_tid(self):
        return self._isv_tid

    @isv_tid.setter
    def isv_tid(self, value):
        self._isv_tid = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_code:
            if hasattr(self.activation_code, 'to_alipay_dict'):
                params['activation_code'] = self.activation_code.to_alipay_dict()
            else:
                params['activation_code'] = self.activation_code
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.isv_tid:
            if hasattr(self.isv_tid, 'to_alipay_dict'):
                params['isv_tid'] = self.isv_tid.to_alipay_dict()
            else:
                params['isv_tid'] = self.isv_tid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionrecgDeviceactivationQueryModel()
        if 'activation_code' in d:
            o.activation_code = d['activation_code']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'isv_tid' in d:
            o.isv_tid = d['isv_tid']
        return o


