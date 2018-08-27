#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskRiskscanSingleQueryModel(object):

    def __init__(self):
        self._app_key = None
        self._event_data = None
        self._event_type = None
        self._secret_key = None

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
    @property
    def event_data(self):
        return self._event_data

    @event_data.setter
    def event_data(self, value):
        self._event_data = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
        if self.event_data:
            if hasattr(self.event_data, 'to_alipay_dict'):
                params['event_data'] = self.event_data.to_alipay_dict()
            else:
                params['event_data'] = self.event_data
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.secret_key:
            if hasattr(self.secret_key, 'to_alipay_dict'):
                params['secret_key'] = self.secret_key.to_alipay_dict()
            else:
                params['secret_key'] = self.secret_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskRiskscanSingleQueryModel()
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'event_data' in d:
            o.event_data = d['event_data']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'secret_key' in d:
            o.secret_key = d['secret_key']
        return o


