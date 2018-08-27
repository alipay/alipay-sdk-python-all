#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductProvider import ProductProvider


class SaleProduct(object):

    def __init__(self):
        self._channel_type = None
        self._id = None
        self._market_price = None
        self._product_provider = None
        self._sale_price = None
        self._status = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def market_price(self):
        return self._market_price

    @market_price.setter
    def market_price(self, value):
        self._market_price = value
    @property
    def product_provider(self):
        return self._product_provider

    @product_provider.setter
    def product_provider(self, value):
        if isinstance(value, ProductProvider):
            self._product_provider = value
        else:
            self._product_provider = ProductProvider.from_alipay_dict(value)
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.market_price:
            if hasattr(self.market_price, 'to_alipay_dict'):
                params['market_price'] = self.market_price.to_alipay_dict()
            else:
                params['market_price'] = self.market_price
        if self.product_provider:
            if hasattr(self.product_provider, 'to_alipay_dict'):
                params['product_provider'] = self.product_provider.to_alipay_dict()
            else:
                params['product_provider'] = self.product_provider
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleProduct()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'id' in d:
            o.id = d['id']
        if 'market_price' in d:
            o.market_price = d['market_price']
        if 'product_provider' in d:
            o.product_provider = d['product_provider']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'status' in d:
            o.status = d['status']
        return o


