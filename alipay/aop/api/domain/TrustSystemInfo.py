#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChargeSystemInfo import ChargeSystemInfo


class TrustSystemInfo(object):

    def __init__(self):
        self._adjustable = None
        self._charge_system_info = None
        self._system_status = None
        self._system_type = None

    @property
    def adjustable(self):
        return self._adjustable

    @adjustable.setter
    def adjustable(self, value):
        self._adjustable = value
    @property
    def charge_system_info(self):
        return self._charge_system_info

    @charge_system_info.setter
    def charge_system_info(self, value):
        if isinstance(value, ChargeSystemInfo):
            self._charge_system_info = value
        else:
            self._charge_system_info = ChargeSystemInfo.from_alipay_dict(value)
    @property
    def system_status(self):
        return self._system_status

    @system_status.setter
    def system_status(self, value):
        self._system_status = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjustable:
            if hasattr(self.adjustable, 'to_alipay_dict'):
                params['adjustable'] = self.adjustable.to_alipay_dict()
            else:
                params['adjustable'] = self.adjustable
        if self.charge_system_info:
            if hasattr(self.charge_system_info, 'to_alipay_dict'):
                params['charge_system_info'] = self.charge_system_info.to_alipay_dict()
            else:
                params['charge_system_info'] = self.charge_system_info
        if self.system_status:
            if hasattr(self.system_status, 'to_alipay_dict'):
                params['system_status'] = self.system_status.to_alipay_dict()
            else:
                params['system_status'] = self.system_status
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustSystemInfo()
        if 'adjustable' in d:
            o.adjustable = d['adjustable']
        if 'charge_system_info' in d:
            o.charge_system_info = d['charge_system_info']
        if 'system_status' in d:
            o.system_status = d['system_status']
        if 'system_type' in d:
            o.system_type = d['system_type']
        return o


