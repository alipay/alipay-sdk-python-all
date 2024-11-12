#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardPropertyCycle import CardPropertyCycle
from alipay.aop.api.domain.CardPeriodPrice import CardPeriodPrice


class AlipayCommerceMerchantcardPricepropertyCreateModel(object):

    def __init__(self):
        self._card_property_cycle = None
        self._card_template_id = None
        self._card_template_name = None
        self._card_type = None
        self._original_price = None
        self._period_price_list = None
        self._sale_price = None

    @property
    def card_property_cycle(self):
        return self._card_property_cycle

    @card_property_cycle.setter
    def card_property_cycle(self, value):
        if isinstance(value, CardPropertyCycle):
            self._card_property_cycle = value
        else:
            self._card_property_cycle = CardPropertyCycle.from_alipay_dict(value)
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_template_name(self):
        return self._card_template_name

    @card_template_name.setter
    def card_template_name(self, value):
        self._card_template_name = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def period_price_list(self):
        return self._period_price_list

    @period_price_list.setter
    def period_price_list(self, value):
        if isinstance(value, list):
            self._period_price_list = list()
            for i in value:
                if isinstance(i, CardPeriodPrice):
                    self._period_price_list.append(i)
                else:
                    self._period_price_list.append(CardPeriodPrice.from_alipay_dict(i))
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_property_cycle:
            if hasattr(self.card_property_cycle, 'to_alipay_dict'):
                params['card_property_cycle'] = self.card_property_cycle.to_alipay_dict()
            else:
                params['card_property_cycle'] = self.card_property_cycle
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_template_name:
            if hasattr(self.card_template_name, 'to_alipay_dict'):
                params['card_template_name'] = self.card_template_name.to_alipay_dict()
            else:
                params['card_template_name'] = self.card_template_name
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.period_price_list:
            if isinstance(self.period_price_list, list):
                for i in range(0, len(self.period_price_list)):
                    element = self.period_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_price_list[i] = element.to_alipay_dict()
            if hasattr(self.period_price_list, 'to_alipay_dict'):
                params['period_price_list'] = self.period_price_list.to_alipay_dict()
            else:
                params['period_price_list'] = self.period_price_list
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardPricepropertyCreateModel()
        if 'card_property_cycle' in d:
            o.card_property_cycle = d['card_property_cycle']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_template_name' in d:
            o.card_template_name = d['card_template_name']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'period_price_list' in d:
            o.period_price_list = d['period_price_list']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o


