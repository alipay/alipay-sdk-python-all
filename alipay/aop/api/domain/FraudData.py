#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FraudData(object):

    def __init__(self):
        self._device_identifier = None
        self._user_identifier = None

    @property
    def device_identifier(self):
        return self._device_identifier

    @device_identifier.setter
    def device_identifier(self, value):
        self._device_identifier = value
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
        o = FraudData()
        if 'device_identifier' in d:
            o.device_identifier = d['device_identifier']
        if 'user_identifier' in d:
            o.user_identifier = d['user_identifier']
        return o


