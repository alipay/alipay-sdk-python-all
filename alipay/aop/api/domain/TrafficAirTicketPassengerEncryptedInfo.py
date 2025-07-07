#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficAirTicketPassengerEncryptedInfo(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._mobile_no = None
        self._name = None
        self._self = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def self(self):
        return self._self

    @self.setter
    def self(self, value):
        self._self = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.self:
            if hasattr(self.self, 'to_alipay_dict'):
                params['self'] = self.self.to_alipay_dict()
            else:
                params['self'] = self.self
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirTicketPassengerEncryptedInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'name' in d:
            o.name = d['name']
        if 'self' in d:
            o.self = d['self']
        return o


