#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertDeliveryDiscountWebBatchqueryModel(object):

    def __init__(self):
        self._channel = None
        self._latitude = None
        self._longitude = None
        self._mobile = None
        self._shop_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertDeliveryDiscountWebBatchqueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


