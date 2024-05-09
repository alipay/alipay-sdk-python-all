#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceBusinessMallCreateModel(object):

    def __init__(self):
        self._business_code = None
        self._mall_distance = None
        self._mall_latitude = None
        self._mall_longitude = None
        self._mall_name = None
        self._partner_id = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def mall_distance(self):
        return self._mall_distance

    @mall_distance.setter
    def mall_distance(self, value):
        self._mall_distance = value
    @property
    def mall_latitude(self):
        return self._mall_latitude

    @mall_latitude.setter
    def mall_latitude(self, value):
        self._mall_latitude = value
    @property
    def mall_longitude(self):
        return self._mall_longitude

    @mall_longitude.setter
    def mall_longitude(self, value):
        self._mall_longitude = value
    @property
    def mall_name(self):
        return self._mall_name

    @mall_name.setter
    def mall_name(self, value):
        self._mall_name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.mall_distance:
            if hasattr(self.mall_distance, 'to_alipay_dict'):
                params['mall_distance'] = self.mall_distance.to_alipay_dict()
            else:
                params['mall_distance'] = self.mall_distance
        if self.mall_latitude:
            if hasattr(self.mall_latitude, 'to_alipay_dict'):
                params['mall_latitude'] = self.mall_latitude.to_alipay_dict()
            else:
                params['mall_latitude'] = self.mall_latitude
        if self.mall_longitude:
            if hasattr(self.mall_longitude, 'to_alipay_dict'):
                params['mall_longitude'] = self.mall_longitude.to_alipay_dict()
            else:
                params['mall_longitude'] = self.mall_longitude
        if self.mall_name:
            if hasattr(self.mall_name, 'to_alipay_dict'):
                params['mall_name'] = self.mall_name.to_alipay_dict()
            else:
                params['mall_name'] = self.mall_name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceBusinessMallCreateModel()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'mall_distance' in d:
            o.mall_distance = d['mall_distance']
        if 'mall_latitude' in d:
            o.mall_latitude = d['mall_latitude']
        if 'mall_longitude' in d:
            o.mall_longitude = d['mall_longitude']
        if 'mall_name' in d:
            o.mall_name = d['mall_name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


