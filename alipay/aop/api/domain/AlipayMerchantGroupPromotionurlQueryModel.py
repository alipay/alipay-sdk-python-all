#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupPromotionurlQueryModel(object):

    def __init__(self):
        self._group_id = None
        self._promotion_channel = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def promotion_channel(self):
        return self._promotion_channel

    @promotion_channel.setter
    def promotion_channel(self, value):
        self._promotion_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.promotion_channel:
            if hasattr(self.promotion_channel, 'to_alipay_dict'):
                params['promotion_channel'] = self.promotion_channel.to_alipay_dict()
            else:
                params['promotion_channel'] = self.promotion_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupPromotionurlQueryModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'promotion_channel' in d:
            o.promotion_channel = d['promotion_channel']
        return o


