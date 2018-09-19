#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderLogisticsExtInfo import OrderLogisticsExtInfo


class OrderLogisticsInfo(object):

    def __init__(self):
        self._address = None
        self._contact_name = None
        self._ext_info = None
        self._latitude = None
        self._longitude = None
        self._merchant_bind_mobile = None
        self._mobile = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, OrderLogisticsExtInfo):
            self._ext_info = value
        else:
            self._ext_info = OrderLogisticsExtInfo.from_alipay_dict(value)
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
    def merchant_bind_mobile(self):
        return self._merchant_bind_mobile

    @merchant_bind_mobile.setter
    def merchant_bind_mobile(self, value):
        self._merchant_bind_mobile = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.merchant_bind_mobile:
            if hasattr(self.merchant_bind_mobile, 'to_alipay_dict'):
                params['merchant_bind_mobile'] = self.merchant_bind_mobile.to_alipay_dict()
            else:
                params['merchant_bind_mobile'] = self.merchant_bind_mobile
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderLogisticsInfo()
        if 'address' in d:
            o.address = d['address']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'merchant_bind_mobile' in d:
            o.merchant_bind_mobile = d['merchant_bind_mobile']
        if 'mobile' in d:
            o.mobile = d['mobile']
        return o


