#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplatePriceDateRuleVO import MerchantCardTemplatePriceDateRuleVO
from alipay.aop.api.domain.MerchantCardTemplatePriceWeekRuleVO import MerchantCardTemplatePriceWeekRuleVO


class MerchantCardTemplatePriceItem(object):

    def __init__(self):
        self._city_code = None
        self._date_price_list = None
        self._district_code = None
        self._original_price = None
        self._price_mode = None
        self._province_code = None
        self._region_level = None
        self._sale_price = None
        self._shop_id = None
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
                if isinstance(i, MerchantCardTemplatePriceDateRuleVO):
                    self._date_price_list.append(i)
                else:
                    self._date_price_list.append(MerchantCardTemplatePriceDateRuleVO.from_alipay_dict(i))
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
    def price_mode(self):
        return self._price_mode

    @price_mode.setter
    def price_mode(self, value):
        self._price_mode = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def region_level(self):
        return self._region_level

    @region_level.setter
    def region_level(self, value):
        self._region_level = value
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
                if isinstance(i, MerchantCardTemplatePriceWeekRuleVO):
                    self._week_price_list.append(i)
                else:
                    self._week_price_list.append(MerchantCardTemplatePriceWeekRuleVO.from_alipay_dict(i))


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
        if self.price_mode:
            if hasattr(self.price_mode, 'to_alipay_dict'):
                params['price_mode'] = self.price_mode.to_alipay_dict()
            else:
                params['price_mode'] = self.price_mode
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.region_level:
            if hasattr(self.region_level, 'to_alipay_dict'):
                params['region_level'] = self.region_level.to_alipay_dict()
            else:
                params['region_level'] = self.region_level
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
        o = MerchantCardTemplatePriceItem()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'date_price_list' in d:
            o.date_price_list = d['date_price_list']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price_mode' in d:
            o.price_mode = d['price_mode']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'region_level' in d:
            o.region_level = d['region_level']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'week_price_list' in d:
            o.week_price_list = d['week_price_list']
        return o


