#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelExchangerateQueryModel(object):

    def __init__(self):
        self._country_code = None
        self._currency = None
        self._extend_param = None
        self._latitude = None
        self._longitude = None
        self._user_id = None

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelExchangerateQueryModel()
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


