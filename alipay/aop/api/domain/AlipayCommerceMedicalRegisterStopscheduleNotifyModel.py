#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterStopscheduleNotifyModel(object):

    def __init__(self):
        self._date = None
        self._hospital_id = None
        self._isv_code = None
        self._notify_type = None
        self._number_ids = None
        self._platform_code = None
        self._reason = None
        self._register_ids = None
        self._stop_prop = None
        self._type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def number_ids(self):
        return self._number_ids

    @number_ids.setter
    def number_ids(self, value):
        self._number_ids = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def register_ids(self):
        return self._register_ids

    @register_ids.setter
    def register_ids(self, value):
        self._register_ids = value
    @property
    def stop_prop(self):
        return self._stop_prop

    @stop_prop.setter
    def stop_prop(self, value):
        self._stop_prop = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.number_ids:
            if hasattr(self.number_ids, 'to_alipay_dict'):
                params['number_ids'] = self.number_ids.to_alipay_dict()
            else:
                params['number_ids'] = self.number_ids
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.register_ids:
            if hasattr(self.register_ids, 'to_alipay_dict'):
                params['register_ids'] = self.register_ids.to_alipay_dict()
            else:
                params['register_ids'] = self.register_ids
        if self.stop_prop:
            if hasattr(self.stop_prop, 'to_alipay_dict'):
                params['stop_prop'] = self.stop_prop.to_alipay_dict()
            else:
                params['stop_prop'] = self.stop_prop
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterStopscheduleNotifyModel()
        if 'date' in d:
            o.date = d['date']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'number_ids' in d:
            o.number_ids = d['number_ids']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'reason' in d:
            o.reason = d['reason']
        if 'register_ids' in d:
            o.register_ids = d['register_ids']
        if 'stop_prop' in d:
            o.stop_prop = d['stop_prop']
        if 'type' in d:
            o.type = d['type']
        return o


