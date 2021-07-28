#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardPriceRequestItem(object):

    def __init__(self):
        self._base_price_cent = None
        self._card_type = None
        self._default_promo_price_cent = None
        self._high_price_cent = None
        self._last_promo_price = None
        self._lower_price_cent = None
        self._pricing = None
        self._visible = None

    @property
    def base_price_cent(self):
        return self._base_price_cent

    @base_price_cent.setter
    def base_price_cent(self, value):
        self._base_price_cent = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def default_promo_price_cent(self):
        return self._default_promo_price_cent

    @default_promo_price_cent.setter
    def default_promo_price_cent(self, value):
        self._default_promo_price_cent = value
    @property
    def high_price_cent(self):
        return self._high_price_cent

    @high_price_cent.setter
    def high_price_cent(self, value):
        self._high_price_cent = value
    @property
    def last_promo_price(self):
        return self._last_promo_price

    @last_promo_price.setter
    def last_promo_price(self, value):
        self._last_promo_price = value
    @property
    def lower_price_cent(self):
        return self._lower_price_cent

    @lower_price_cent.setter
    def lower_price_cent(self, value):
        self._lower_price_cent = value
    @property
    def pricing(self):
        return self._pricing

    @pricing.setter
    def pricing(self, value):
        self._pricing = value
    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_price_cent:
            if hasattr(self.base_price_cent, 'to_alipay_dict'):
                params['base_price_cent'] = self.base_price_cent.to_alipay_dict()
            else:
                params['base_price_cent'] = self.base_price_cent
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.default_promo_price_cent:
            if hasattr(self.default_promo_price_cent, 'to_alipay_dict'):
                params['default_promo_price_cent'] = self.default_promo_price_cent.to_alipay_dict()
            else:
                params['default_promo_price_cent'] = self.default_promo_price_cent
        if self.high_price_cent:
            if hasattr(self.high_price_cent, 'to_alipay_dict'):
                params['high_price_cent'] = self.high_price_cent.to_alipay_dict()
            else:
                params['high_price_cent'] = self.high_price_cent
        if self.last_promo_price:
            if hasattr(self.last_promo_price, 'to_alipay_dict'):
                params['last_promo_price'] = self.last_promo_price.to_alipay_dict()
            else:
                params['last_promo_price'] = self.last_promo_price
        if self.lower_price_cent:
            if hasattr(self.lower_price_cent, 'to_alipay_dict'):
                params['lower_price_cent'] = self.lower_price_cent.to_alipay_dict()
            else:
                params['lower_price_cent'] = self.lower_price_cent
        if self.pricing:
            if hasattr(self.pricing, 'to_alipay_dict'):
                params['pricing'] = self.pricing.to_alipay_dict()
            else:
                params['pricing'] = self.pricing
        if self.visible:
            if hasattr(self.visible, 'to_alipay_dict'):
                params['visible'] = self.visible.to_alipay_dict()
            else:
                params['visible'] = self.visible
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardPriceRequestItem()
        if 'base_price_cent' in d:
            o.base_price_cent = d['base_price_cent']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'default_promo_price_cent' in d:
            o.default_promo_price_cent = d['default_promo_price_cent']
        if 'high_price_cent' in d:
            o.high_price_cent = d['high_price_cent']
        if 'last_promo_price' in d:
            o.last_promo_price = d['last_promo_price']
        if 'lower_price_cent' in d:
            o.lower_price_cent = d['lower_price_cent']
        if 'pricing' in d:
            o.pricing = d['pricing']
        if 'visible' in d:
            o.visible = d['visible']
        return o


