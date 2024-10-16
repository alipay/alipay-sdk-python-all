#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScalesActivationCodeDeviceInfo(object):

    def __init__(self):
        self._activation_code = None
        self._activation_type = None
        self._biz_tid = None
        self._isv_tid = None
        self._modified_time = None

    @property
    def activation_code(self):
        return self._activation_code

    @activation_code.setter
    def activation_code(self, value):
        self._activation_code = value
    @property
    def activation_type(self):
        return self._activation_type

    @activation_type.setter
    def activation_type(self, value):
        self._activation_type = value
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
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_code:
            if hasattr(self.activation_code, 'to_alipay_dict'):
                params['activation_code'] = self.activation_code.to_alipay_dict()
            else:
                params['activation_code'] = self.activation_code
        if self.activation_type:
            if hasattr(self.activation_type, 'to_alipay_dict'):
                params['activation_type'] = self.activation_type.to_alipay_dict()
            else:
                params['activation_type'] = self.activation_type
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
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScalesActivationCodeDeviceInfo()
        if 'activation_code' in d:
            o.activation_code = d['activation_code']
        if 'activation_type' in d:
            o.activation_type = d['activation_type']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'isv_tid' in d:
            o.isv_tid = d['isv_tid']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        return o


