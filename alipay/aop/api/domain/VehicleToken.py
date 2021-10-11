#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleToken(object):

    def __init__(self):
        self._expires_in_timestamp = None
        self._refresh_expires_in_timestamp = None
        self._vehicle_access_token = None
        self._vehicle_refresh_token = None

    @property
    def expires_in_timestamp(self):
        return self._expires_in_timestamp

    @expires_in_timestamp.setter
    def expires_in_timestamp(self, value):
        self._expires_in_timestamp = value
    @property
    def refresh_expires_in_timestamp(self):
        return self._refresh_expires_in_timestamp

    @refresh_expires_in_timestamp.setter
    def refresh_expires_in_timestamp(self, value):
        self._refresh_expires_in_timestamp = value
    @property
    def vehicle_access_token(self):
        return self._vehicle_access_token

    @vehicle_access_token.setter
    def vehicle_access_token(self, value):
        self._vehicle_access_token = value
    @property
    def vehicle_refresh_token(self):
        return self._vehicle_refresh_token

    @vehicle_refresh_token.setter
    def vehicle_refresh_token(self, value):
        self._vehicle_refresh_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.expires_in_timestamp:
            if hasattr(self.expires_in_timestamp, 'to_alipay_dict'):
                params['expires_in_timestamp'] = self.expires_in_timestamp.to_alipay_dict()
            else:
                params['expires_in_timestamp'] = self.expires_in_timestamp
        if self.refresh_expires_in_timestamp:
            if hasattr(self.refresh_expires_in_timestamp, 'to_alipay_dict'):
                params['refresh_expires_in_timestamp'] = self.refresh_expires_in_timestamp.to_alipay_dict()
            else:
                params['refresh_expires_in_timestamp'] = self.refresh_expires_in_timestamp
        if self.vehicle_access_token:
            if hasattr(self.vehicle_access_token, 'to_alipay_dict'):
                params['vehicle_access_token'] = self.vehicle_access_token.to_alipay_dict()
            else:
                params['vehicle_access_token'] = self.vehicle_access_token
        if self.vehicle_refresh_token:
            if hasattr(self.vehicle_refresh_token, 'to_alipay_dict'):
                params['vehicle_refresh_token'] = self.vehicle_refresh_token.to_alipay_dict()
            else:
                params['vehicle_refresh_token'] = self.vehicle_refresh_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleToken()
        if 'expires_in_timestamp' in d:
            o.expires_in_timestamp = d['expires_in_timestamp']
        if 'refresh_expires_in_timestamp' in d:
            o.refresh_expires_in_timestamp = d['refresh_expires_in_timestamp']
        if 'vehicle_access_token' in d:
            o.vehicle_access_token = d['vehicle_access_token']
        if 'vehicle_refresh_token' in d:
            o.vehicle_refresh_token = d['vehicle_refresh_token']
        return o


