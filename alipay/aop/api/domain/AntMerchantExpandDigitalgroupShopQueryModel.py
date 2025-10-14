#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandDigitalgroupShopQueryModel(object):

    def __init__(self):
        self._channel = None
        self._channel_shop_id = None
        self._digital_poi_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_shop_id(self):
        return self._channel_shop_id

    @channel_shop_id.setter
    def channel_shop_id(self, value):
        self._channel_shop_id = value
    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_shop_id:
            if hasattr(self.channel_shop_id, 'to_alipay_dict'):
                params['channel_shop_id'] = self.channel_shop_id.to_alipay_dict()
            else:
                params['channel_shop_id'] = self.channel_shop_id
        if self.digital_poi_id:
            if hasattr(self.digital_poi_id, 'to_alipay_dict'):
                params['digital_poi_id'] = self.digital_poi_id.to_alipay_dict()
            else:
                params['digital_poi_id'] = self.digital_poi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDigitalgroupShopQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_shop_id' in d:
            o.channel_shop_id = d['channel_shop_id']
        if 'digital_poi_id' in d:
            o.digital_poi_id = d['digital_poi_id']
        return o


