#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PricingMode import PricingMode


class AlipayAipayNowpayChargeInitializeModel(object):

    def __init__(self):
        self._callback_url = None
        self._external_owner_id = None
        self._out_product_id = None
        self._pricing_mode_list = None
        self._product_icon_url = None
        self._product_name = None
        self._product_url = None

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
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
    @property
    def pricing_mode_list(self):
        return self._pricing_mode_list

    @pricing_mode_list.setter
    def pricing_mode_list(self, value):
        if isinstance(value, list):
            self._pricing_mode_list = list()
            for i in value:
                if isinstance(i, PricingMode):
                    self._pricing_mode_list.append(i)
                else:
                    self._pricing_mode_list.append(PricingMode.from_alipay_dict(i))
    @property
    def product_icon_url(self):
        return self._product_icon_url

    @product_icon_url.setter
    def product_icon_url(self, value):
        self._product_icon_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_url(self):
        return self._product_url

    @product_url.setter
    def product_url(self, value):
        self._product_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
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
        if self.pricing_mode_list:
            if isinstance(self.pricing_mode_list, list):
                for i in range(0, len(self.pricing_mode_list)):
                    element = self.pricing_mode_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pricing_mode_list[i] = element.to_alipay_dict()
            if hasattr(self.pricing_mode_list, 'to_alipay_dict'):
                params['pricing_mode_list'] = self.pricing_mode_list.to_alipay_dict()
            else:
                params['pricing_mode_list'] = self.pricing_mode_list
        if self.product_icon_url:
            if hasattr(self.product_icon_url, 'to_alipay_dict'):
                params['product_icon_url'] = self.product_icon_url.to_alipay_dict()
            else:
                params['product_icon_url'] = self.product_icon_url
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_url:
            if hasattr(self.product_url, 'to_alipay_dict'):
                params['product_url'] = self.product_url.to_alipay_dict()
            else:
                params['product_url'] = self.product_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayNowpayChargeInitializeModel()
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'external_owner_id' in d:
            o.external_owner_id = d['external_owner_id']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'pricing_mode_list' in d:
            o.pricing_mode_list = d['pricing_mode_list']
        if 'product_icon_url' in d:
            o.product_icon_url = d['product_icon_url']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_url' in d:
            o.product_url = d['product_url']
        return o


