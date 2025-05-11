#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterStopclinicNotifyModel(object):

    def __init__(self):
        self._date = None
        self._hospital_id = None
        self._nofity_type = None
        self._platform_code = None
        self._reason = None
        self._register_id = None
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
    def nofity_type(self):
        return self._nofity_type

    @nofity_type.setter
    def nofity_type(self, value):
        self._nofity_type = value
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
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value
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
        if self.nofity_type:
            if hasattr(self.nofity_type, 'to_alipay_dict'):
                params['nofity_type'] = self.nofity_type.to_alipay_dict()
            else:
                params['nofity_type'] = self.nofity_type
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
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
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
        o = AlipayCommerceMedicalRegisterStopclinicNotifyModel()
        if 'date' in d:
            o.date = d['date']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'nofity_type' in d:
            o.nofity_type = d['nofity_type']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'reason' in d:
            o.reason = d['reason']
        if 'register_id' in d:
            o.register_id = d['register_id']
        if 'type' in d:
            o.type = d['type']
        return o


