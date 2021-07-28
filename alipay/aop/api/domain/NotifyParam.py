#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotifyParam(object):

    def __init__(self):
        self._params = None
        self._personal_name = None
        self._send_sms = None
        self._service_code = None

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def personal_name(self):
        return self._personal_name

    @personal_name.setter
    def personal_name(self, value):
        self._personal_name = value
    @property
    def send_sms(self):
        return self._send_sms

    @send_sms.setter
    def send_sms(self, value):
        self._send_sms = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.personal_name:
            if hasattr(self.personal_name, 'to_alipay_dict'):
                params['personal_name'] = self.personal_name.to_alipay_dict()
            else:
                params['personal_name'] = self.personal_name
        if self.send_sms:
            if hasattr(self.send_sms, 'to_alipay_dict'):
                params['send_sms'] = self.send_sms.to_alipay_dict()
            else:
                params['send_sms'] = self.send_sms
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NotifyParam()
        if 'params' in d:
            o.params = d['params']
        if 'personal_name' in d:
            o.personal_name = d['personal_name']
        if 'send_sms' in d:
            o.send_sms = d['send_sms']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


