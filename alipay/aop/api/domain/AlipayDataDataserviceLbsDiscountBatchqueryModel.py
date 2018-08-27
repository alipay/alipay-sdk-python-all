#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceLbsDiscountBatchqueryModel(object):

    def __init__(self):
        self._channel = None
        self._imei = None
        self._latitude = None
        self._longitude = None
        self._mobile = None
        self._size = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
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
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
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
        o = AlipayDataDataserviceLbsDiscountBatchqueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'imei' in d:
            o.imei = d['imei']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'size' in d:
            o.size = d['size']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


