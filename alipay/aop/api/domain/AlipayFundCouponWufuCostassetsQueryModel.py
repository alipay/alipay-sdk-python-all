#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponWufuCostassetsQueryModel(object):

    def __init__(self):
        self._cost_count = None
        self._cost_merchant_card = None
        self._ext_info = None
        self._open_id = None
        self._source = None
        self._user_id = None

    @property
    def cost_count(self):
        return self._cost_count

    @cost_count.setter
    def cost_count(self, value):
        self._cost_count = value
    @property
    def cost_merchant_card(self):
        return self._cost_merchant_card

    @cost_merchant_card.setter
    def cost_merchant_card(self, value):
        self._cost_merchant_card = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cost_count:
            if hasattr(self.cost_count, 'to_alipay_dict'):
                params['cost_count'] = self.cost_count.to_alipay_dict()
            else:
                params['cost_count'] = self.cost_count
        if self.cost_merchant_card:
            if hasattr(self.cost_merchant_card, 'to_alipay_dict'):
                params['cost_merchant_card'] = self.cost_merchant_card.to_alipay_dict()
            else:
                params['cost_merchant_card'] = self.cost_merchant_card
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayFundCouponWufuCostassetsQueryModel()
        if 'cost_count' in d:
            o.cost_count = d['cost_count']
        if 'cost_merchant_card' in d:
            o.cost_merchant_card = d['cost_merchant_card']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


