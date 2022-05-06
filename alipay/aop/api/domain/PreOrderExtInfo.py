#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PreOrderExtInfo(object):

    def __init__(self):
        self._brand_id = None
        self._brand_name = None
        self._channel = None
        self._order_feature = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def order_feature(self):
        return self._order_feature

    @order_feature.setter
    def order_feature(self, value):
        self._order_feature = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.order_feature:
            if hasattr(self.order_feature, 'to_alipay_dict'):
                params['order_feature'] = self.order_feature.to_alipay_dict()
            else:
                params['order_feature'] = self.order_feature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreOrderExtInfo()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'channel' in d:
            o.channel = d['channel']
        if 'order_feature' in d:
            o.order_feature = d['order_feature']
        return o


