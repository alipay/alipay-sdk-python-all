#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TiansuoIsvBindVO(object):

    def __init__(self):
        self._business_license_no = None
        self._isv_pid = None
        self._operation = None

    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TiansuoIsvBindVO()
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'operation' in d:
            o.operation = d['operation']
        return o


