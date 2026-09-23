#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayNowpayPurchaseConsultModel(object):

    def __init__(self):
        self._callback_url = None
        self._external_buyer_id = None
        self._external_owner_id = None
        self._out_product_id = None

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def external_buyer_id(self):
        return self._external_buyer_id

    @external_buyer_id.setter
    def external_buyer_id(self, value):
        self._external_buyer_id = value
    @property
    def external_owner_id(self):
        return self._external_owner_id

    @external_owner_id.setter
    def external_owner_id(self, value):
        self._external_owner_id = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.external_buyer_id:
            if hasattr(self.external_buyer_id, 'to_alipay_dict'):
                params['external_buyer_id'] = self.external_buyer_id.to_alipay_dict()
            else:
                params['external_buyer_id'] = self.external_buyer_id
        if self.external_owner_id:
            if hasattr(self.external_owner_id, 'to_alipay_dict'):
                params['external_owner_id'] = self.external_owner_id.to_alipay_dict()
            else:
                params['external_owner_id'] = self.external_owner_id
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayNowpayPurchaseConsultModel()
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'external_buyer_id' in d:
            o.external_buyer_id = d['external_buyer_id']
        if 'external_owner_id' in d:
            o.external_owner_id = d['external_owner_id']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        return o


