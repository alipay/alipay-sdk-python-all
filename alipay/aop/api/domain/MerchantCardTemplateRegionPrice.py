#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplatePriceDateRule import MerchantCardTemplatePriceDateRule
from alipay.aop.api.domain.MerchantCardTemplatePriceWeekRule import MerchantCardTemplatePriceWeekRule


class MerchantCardTemplateRegionPrice(object):

    def __init__(self):
        self._city_code = None
        self._date_price_list = None
        self._district_code = None
        self._original_price = None
        self._province_code = None
        self._sale_price = None
        self._week_price_list = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
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
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
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
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
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
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
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
        o = MerchantCardTemplateRegionPrice()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'date_price_list' in d:
            o.date_price_list = d['date_price_list']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'week_price_list' in d:
            o.week_price_list = d['week_price_list']
        return o


