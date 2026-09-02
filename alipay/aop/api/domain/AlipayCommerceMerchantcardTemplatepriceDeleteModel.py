#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTemplatepriceDeleteModel(object):

    def __init__(self):
        self._card_template_id = None
        self._city_code_list = None
        self._delete_calendar_price = None
        self._district_code_list = None
        self._province_code_list = None
        self._shop_id_list = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def city_code_list(self):
        return self._city_code_list

    @city_code_list.setter
    def city_code_list(self, value):
        if isinstance(value, list):
            self._city_code_list = list()
            for i in value:
                self._city_code_list.append(i)
    @property
    def delete_calendar_price(self):
        return self._delete_calendar_price

    @delete_calendar_price.setter
    def delete_calendar_price(self, value):
        self._delete_calendar_price = value
    @property
    def district_code_list(self):
        return self._district_code_list

    @district_code_list.setter
    def district_code_list(self, value):
        if isinstance(value, list):
            self._district_code_list = list()
            for i in value:
                self._district_code_list.append(i)
    @property
    def province_code_list(self):
        return self._province_code_list

    @province_code_list.setter
    def province_code_list(self, value):
        if isinstance(value, list):
            self._province_code_list = list()
            for i in value:
                self._province_code_list.append(i)
    @property
    def shop_id_list(self):
        return self._shop_id_list

    @shop_id_list.setter
    def shop_id_list(self, value):
        if isinstance(value, list):
            self._shop_id_list = list()
            for i in value:
                self._shop_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.city_code_list:
            if isinstance(self.city_code_list, list):
                for i in range(0, len(self.city_code_list)):
                    element = self.city_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_code_list[i] = element.to_alipay_dict()
            if hasattr(self.city_code_list, 'to_alipay_dict'):
                params['city_code_list'] = self.city_code_list.to_alipay_dict()
            else:
                params['city_code_list'] = self.city_code_list
        if self.delete_calendar_price:
            if hasattr(self.delete_calendar_price, 'to_alipay_dict'):
                params['delete_calendar_price'] = self.delete_calendar_price.to_alipay_dict()
            else:
                params['delete_calendar_price'] = self.delete_calendar_price
        if self.district_code_list:
            if isinstance(self.district_code_list, list):
                for i in range(0, len(self.district_code_list)):
                    element = self.district_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_code_list[i] = element.to_alipay_dict()
            if hasattr(self.district_code_list, 'to_alipay_dict'):
                params['district_code_list'] = self.district_code_list.to_alipay_dict()
            else:
                params['district_code_list'] = self.district_code_list
        if self.province_code_list:
            if isinstance(self.province_code_list, list):
                for i in range(0, len(self.province_code_list)):
                    element = self.province_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.province_code_list[i] = element.to_alipay_dict()
            if hasattr(self.province_code_list, 'to_alipay_dict'):
                params['province_code_list'] = self.province_code_list.to_alipay_dict()
            else:
                params['province_code_list'] = self.province_code_list
        if self.shop_id_list:
            if isinstance(self.shop_id_list, list):
                for i in range(0, len(self.shop_id_list)):
                    element = self.shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_id_list, 'to_alipay_dict'):
                params['shop_id_list'] = self.shop_id_list.to_alipay_dict()
            else:
                params['shop_id_list'] = self.shop_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplatepriceDeleteModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'delete_calendar_price' in d:
            o.delete_calendar_price = d['delete_calendar_price']
        if 'district_code_list' in d:
            o.district_code_list = d['district_code_list']
        if 'province_code_list' in d:
            o.province_code_list = d['province_code_list']
        if 'shop_id_list' in d:
            o.shop_id_list = d['shop_id_list']
        return o


