#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplateCalendarPrice import MerchantCardTemplateCalendarPrice
from alipay.aop.api.domain.MerchantCardTemplateRegionPrice import MerchantCardTemplateRegionPrice
from alipay.aop.api.domain.MerchantCardTemplateShopPrice import MerchantCardTemplateShopPrice


class AlipayCommerceMerchantcardTemplatepriceSetModel(object):

    def __init__(self):
        self._calendar_price = None
        self._card_template_id = None
        self._region_price_list = None
        self._shop_price_list = None

    @property
    def calendar_price(self):
        return self._calendar_price

    @calendar_price.setter
    def calendar_price(self, value):
        if isinstance(value, MerchantCardTemplateCalendarPrice):
            self._calendar_price = value
        else:
            self._calendar_price = MerchantCardTemplateCalendarPrice.from_alipay_dict(value)
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def region_price_list(self):
        return self._region_price_list

    @region_price_list.setter
    def region_price_list(self, value):
        if isinstance(value, list):
            self._region_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplateRegionPrice):
                    self._region_price_list.append(i)
                else:
                    self._region_price_list.append(MerchantCardTemplateRegionPrice.from_alipay_dict(i))
    @property
    def shop_price_list(self):
        return self._shop_price_list

    @shop_price_list.setter
    def shop_price_list(self, value):
        if isinstance(value, list):
            self._shop_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplateShopPrice):
                    self._shop_price_list.append(i)
                else:
                    self._shop_price_list.append(MerchantCardTemplateShopPrice.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_price:
            if hasattr(self.calendar_price, 'to_alipay_dict'):
                params['calendar_price'] = self.calendar_price.to_alipay_dict()
            else:
                params['calendar_price'] = self.calendar_price
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.region_price_list:
            if isinstance(self.region_price_list, list):
                for i in range(0, len(self.region_price_list)):
                    element = self.region_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_price_list[i] = element.to_alipay_dict()
            if hasattr(self.region_price_list, 'to_alipay_dict'):
                params['region_price_list'] = self.region_price_list.to_alipay_dict()
            else:
                params['region_price_list'] = self.region_price_list
        if self.shop_price_list:
            if isinstance(self.shop_price_list, list):
                for i in range(0, len(self.shop_price_list)):
                    element = self.shop_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_price_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_price_list, 'to_alipay_dict'):
                params['shop_price_list'] = self.shop_price_list.to_alipay_dict()
            else:
                params['shop_price_list'] = self.shop_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplatepriceSetModel()
        if 'calendar_price' in d:
            o.calendar_price = d['calendar_price']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'region_price_list' in d:
            o.region_price_list = d['region_price_list']
        if 'shop_price_list' in d:
            o.shop_price_list = d['shop_price_list']
        return o


