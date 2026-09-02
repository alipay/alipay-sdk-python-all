#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechWeatherAlertQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._latitude = None
        self._longitude = None
        self._request_id = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechWeatherAlertQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


