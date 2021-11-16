#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationResultExtInfo(object):

    def __init__(self):
        self._activation_time = None
        self._device_no = None

    @property
    def activation_time(self):
        return self._activation_time

    @activation_time.setter
    def activation_time(self, value):
        self._activation_time = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_time:
            if hasattr(self.activation_time, 'to_alipay_dict'):
                params['activation_time'] = self.activation_time.to_alipay_dict()
            else:
                params['activation_time'] = self.activation_time
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperationResultExtInfo()
        if 'activation_time' in d:
            o.activation_time = d['activation_time']
        if 'device_no' in d:
            o.device_no = d['device_no']
        return o


