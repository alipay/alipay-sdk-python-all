#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertInfoResponse(object):

    def __init__(self):
        self._cert_name = None
        self._cert_number = None
        self._cert_type = None
        self._uid = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_number(self):
        return self._cert_number

    @cert_number.setter
    def cert_number(self, value):
        self._cert_number = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        if isinstance(value, list):
            self._uid = list()
            for i in value:
                self._uid.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_number:
            if hasattr(self.cert_number, 'to_alipay_dict'):
                params['cert_number'] = self.cert_number.to_alipay_dict()
            else:
                params['cert_number'] = self.cert_number
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.uid:
            if isinstance(self.uid, list):
                for i in range(0, len(self.uid)):
                    element = self.uid[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid[i] = element.to_alipay_dict()
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertInfoResponse()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_number' in d:
            o.cert_number = d['cert_number']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'uid' in d:
            o.uid = d['uid']
        return o


