#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishConditionBatchqueryModel(object):

    def __init__(self):
        self._catetory_big_id = None
        self._catetory_small_id = None
        self._dish_id = None
        self._dish_name = None
        self._merchant_id = None
        self._page_no = None
        self._page_size = None
        self._shop_id = None

    @property
    def catetory_big_id(self):
        return self._catetory_big_id

    @catetory_big_id.setter
    def catetory_big_id(self, value):
        self._catetory_big_id = value
    @property
    def catetory_small_id(self):
        return self._catetory_small_id

    @catetory_small_id.setter
    def catetory_small_id(self, value):
        self._catetory_small_id = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_big_id:
            if hasattr(self.catetory_big_id, 'to_alipay_dict'):
                params['catetory_big_id'] = self.catetory_big_id.to_alipay_dict()
            else:
                params['catetory_big_id'] = self.catetory_big_id
        if self.catetory_small_id:
            if hasattr(self.catetory_small_id, 'to_alipay_dict'):
                params['catetory_small_id'] = self.catetory_small_id.to_alipay_dict()
            else:
                params['catetory_small_id'] = self.catetory_small_id
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishConditionBatchqueryModel()
        if 'catetory_big_id' in d:
            o.catetory_big_id = d['catetory_big_id']
        if 'catetory_small_id' in d:
            o.catetory_small_id = d['catetory_small_id']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


