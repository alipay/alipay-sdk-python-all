#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignBenefitSendModel(object):

    def __init__(self):
        self._channel = None
        self._discount_type = None
        self._item_id = None
        self._out_biz_no = None
        self._shop_id = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        o = KoubeiMarketingCampaignBenefitSendModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


