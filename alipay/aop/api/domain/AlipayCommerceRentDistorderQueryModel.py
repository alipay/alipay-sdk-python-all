#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentDistorderQueryModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._channel_buyer_id = None
        self._channel_order_id = None
        self._distribution_channel = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def channel_buyer_id(self):
        return self._channel_buyer_id

    @channel_buyer_id.setter
    def channel_buyer_id(self, value):
        self._channel_buyer_id = value
    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def distribution_channel(self):
        return self._distribution_channel

    @distribution_channel.setter
    def distribution_channel(self, value):
        self._distribution_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.channel_buyer_id:
            if hasattr(self.channel_buyer_id, 'to_alipay_dict'):
                params['channel_buyer_id'] = self.channel_buyer_id.to_alipay_dict()
            else:
                params['channel_buyer_id'] = self.channel_buyer_id
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.distribution_channel:
            if hasattr(self.distribution_channel, 'to_alipay_dict'):
                params['distribution_channel'] = self.distribution_channel.to_alipay_dict()
            else:
                params['distribution_channel'] = self.distribution_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentDistorderQueryModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'channel_buyer_id' in d:
            o.channel_buyer_id = d['channel_buyer_id']
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'distribution_channel' in d:
            o.distribution_channel = d['distribution_channel']
        return o


