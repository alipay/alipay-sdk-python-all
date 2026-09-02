#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplatePriceDateRule import MerchantCardTemplatePriceDateRule
from alipay.aop.api.domain.MerchantCardTemplatePriceWeekRule import MerchantCardTemplatePriceWeekRule


class MerchantCardTemplateShopPrice(object):

    def __init__(self):
        self._date_price_list = None
        self._original_price = None
        self._sale_price = None
        self._shop_id = None
        self._week_price_list = None

    @property
    def date_price_list(self):
        return self._date_price_list

    @date_price_list.setter
    def date_price_list(self, value):
        if isinstance(value, list):
            self._date_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplatePriceDateRule):
                    self._date_price_list.append(i)
                else:
                    self._date_price_list.append(MerchantCardTemplatePriceDateRule.from_alipay_dict(i))
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def week_price_list(self):
        return self._week_price_list

    @week_price_list.setter
    def week_price_list(self, value):
        if isinstance(value, list):
            self._week_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplatePriceWeekRule):
                    self._week_price_list.append(i)
                else:
                    self._week_price_list.append(MerchantCardTemplatePriceWeekRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.date_price_list:
            if isinstance(self.date_price_list, list):
                for i in range(0, len(self.date_price_list)):
                    element = self.date_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_price_list[i] = element.to_alipay_dict()
            if hasattr(self.date_price_list, 'to_alipay_dict'):
                params['date_price_list'] = self.date_price_list.to_alipay_dict()
            else:
                params['date_price_list'] = self.date_price_list
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.week_price_list:
            if isinstance(self.week_price_list, list):
                for i in range(0, len(self.week_price_list)):
                    element = self.week_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_price_list[i] = element.to_alipay_dict()
            if hasattr(self.week_price_list, 'to_alipay_dict'):
                params['week_price_list'] = self.week_price_list.to_alipay_dict()
            else:
                params['week_price_list'] = self.week_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCardTemplateShopPrice()
        if 'date_price_list' in d:
            o.date_price_list = d['date_price_list']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'week_price_list' in d:
            o.week_price_list = d['week_price_list']
        return o


