#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EstablishFraudData(object):

    def __init__(self):
        self._device_identifier = None
        self._is_biometric_capable = None
        self._user_identifier = None

    @property
    def device_identifier(self):
        return self._device_identifier

    @device_identifier.setter
    def device_identifier(self, value):
        self._device_identifier = value
    @property
    def is_biometric_capable(self):
        return self._is_biometric_capable

    @is_biometric_capable.setter
    def is_biometric_capable(self, value):
        self._is_biometric_capable = value
    @property
    def user_identifier(self):
        return self._user_identifier

    @user_identifier.setter
    def user_identifier(self, value):
        self._user_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_identifier:
            if hasattr(self.device_identifier, 'to_alipay_dict'):
                params['device_identifier'] = self.device_identifier.to_alipay_dict()
            else:
                params['device_identifier'] = self.device_identifier
        if self.is_biometric_capable:
            if hasattr(self.is_biometric_capable, 'to_alipay_dict'):
                params['is_biometric_capable'] = self.is_biometric_capable.to_alipay_dict()
            else:
                params['is_biometric_capable'] = self.is_biometric_capable
        if self.user_identifier:
            if hasattr(self.user_identifier, 'to_alipay_dict'):
                params['user_identifier'] = self.user_identifier.to_alipay_dict()
            else:
                params['user_identifier'] = self.user_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EstablishFraudData()
        if 'device_identifier' in d:
            o.device_identifier = d['device_identifier']
        if 'is_biometric_capable' in d:
            o.is_biometric_capable = d['is_biometric_capable']
        if 'user_identifier' in d:
            o.user_identifier = d['user_identifier']
        return o


