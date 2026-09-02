#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalItemPic import ExternalItemPic
from alipay.aop.api.domain.ExternalItemPropery import ExternalItemPropery


class ExternalSKU(object):

    def __init__(self):
        self._merchant_sku_bar_code = None
        self._merchant_sku_code = None
        self._original_price = None
        self._pic_list = None
        self._sale_price = None
        self._sale_property_list = None
        self._sku_id = None
        self._sku_name = None
        self._status = None

    @property
    def merchant_sku_bar_code(self):
        return self._merchant_sku_bar_code

    @merchant_sku_bar_code.setter
    def merchant_sku_bar_code(self, value):
        self._merchant_sku_bar_code = value
    @property
    def merchant_sku_code(self):
        return self._merchant_sku_code

    @merchant_sku_code.setter
    def merchant_sku_code(self, value):
        self._merchant_sku_code = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def pic_list(self):
        return self._pic_list

    @pic_list.setter
    def pic_list(self, value):
        if isinstance(value, list):
            self._pic_list = list()
            for i in value:
                if isinstance(i, ExternalItemPic):
                    self._pic_list.append(i)
                else:
                    self._pic_list.append(ExternalItemPic.from_alipay_dict(i))
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_property_list(self):
        return self._sale_property_list

    @sale_property_list.setter
    def sale_property_list(self, value):
        if isinstance(value, list):
            self._sale_property_list = list()
            for i in value:
                if isinstance(i, ExternalItemPropery):
                    self._sale_property_list.append(i)
                else:
                    self._sale_property_list.append(ExternalItemPropery.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_sku_bar_code:
            if hasattr(self.merchant_sku_bar_code, 'to_alipay_dict'):
                params['merchant_sku_bar_code'] = self.merchant_sku_bar_code.to_alipay_dict()
            else:
                params['merchant_sku_bar_code'] = self.merchant_sku_bar_code
        if self.merchant_sku_code:
            if hasattr(self.merchant_sku_code, 'to_alipay_dict'):
                params['merchant_sku_code'] = self.merchant_sku_code.to_alipay_dict()
            else:
                params['merchant_sku_code'] = self.merchant_sku_code
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.pic_list:
            if isinstance(self.pic_list, list):
                for i in range(0, len(self.pic_list)):
                    element = self.pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_list[i] = element.to_alipay_dict()
            if hasattr(self.pic_list, 'to_alipay_dict'):
                params['pic_list'] = self.pic_list.to_alipay_dict()
            else:
                params['pic_list'] = self.pic_list
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_property_list:
            if isinstance(self.sale_property_list, list):
                for i in range(0, len(self.sale_property_list)):
                    element = self.sale_property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_property_list[i] = element.to_alipay_dict()
            if hasattr(self.sale_property_list, 'to_alipay_dict'):
                params['sale_property_list'] = self.sale_property_list.to_alipay_dict()
            else:
                params['sale_property_list'] = self.sale_property_list
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
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
        o = ExternalSKU()
        if 'merchant_sku_bar_code' in d:
            o.merchant_sku_bar_code = d['merchant_sku_bar_code']
        if 'merchant_sku_code' in d:
            o.merchant_sku_code = d['merchant_sku_code']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'pic_list' in d:
            o.pic_list = d['pic_list']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_property_list' in d:
            o.sale_property_list = d['sale_property_list']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'status' in d:
            o.status = d['status']
        return o


