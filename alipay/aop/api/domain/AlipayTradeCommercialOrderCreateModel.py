#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCommercialOrderCreateModel(object):

    def __init__(self):
        self._customer_id = None
        self._page_code = None
        self._price_id = None
        self._redirect_url = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.page_code:
            if hasattr(self.page_code, 'to_alipay_dict'):
                params['page_code'] = self.page_code.to_alipay_dict()
            else:
                params['page_code'] = self.page_code
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCommercialOrderCreateModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'page_code' in d:
            o.page_code = d['page_code']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


