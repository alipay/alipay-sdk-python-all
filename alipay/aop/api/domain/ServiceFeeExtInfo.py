#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceFeeExtInfo(object):

    def __init__(self):
        self._city_name = None
        self._origin_consume_amount = None
        self._origin_peer_pay_amount = None
        self._shop_id = None
        self._shop_name = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def origin_consume_amount(self):
        return self._origin_consume_amount

    @origin_consume_amount.setter
    def origin_consume_amount(self, value):
        self._origin_consume_amount = value
    @property
    def origin_peer_pay_amount(self):
        return self._origin_peer_pay_amount

    @origin_peer_pay_amount.setter
    def origin_peer_pay_amount(self, value):
        self._origin_peer_pay_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.origin_consume_amount:
            if hasattr(self.origin_consume_amount, 'to_alipay_dict'):
                params['origin_consume_amount'] = self.origin_consume_amount.to_alipay_dict()
            else:
                params['origin_consume_amount'] = self.origin_consume_amount
        if self.origin_peer_pay_amount:
            if hasattr(self.origin_peer_pay_amount, 'to_alipay_dict'):
                params['origin_peer_pay_amount'] = self.origin_peer_pay_amount.to_alipay_dict()
            else:
                params['origin_peer_pay_amount'] = self.origin_peer_pay_amount
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceFeeExtInfo()
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'origin_consume_amount' in d:
            o.origin_consume_amount = d['origin_consume_amount']
        if 'origin_peer_pay_amount' in d:
            o.origin_peer_pay_amount = d['origin_peer_pay_amount']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


