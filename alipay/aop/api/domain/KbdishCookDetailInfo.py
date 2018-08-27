#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCookPriceInfo import KbdishCookPriceInfo


class KbdishCookDetailInfo(object):

    def __init__(self):
        self._catetory_big_id = None
        self._catetory_small_id = None
        self._cook_id = None
        self._dish_id = None
        self._flag = None
        self._kb_cook_sku_price_list = None
        self._sort = None
        self._status = None

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
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value
    @property
    def kb_cook_sku_price_list(self):
        return self._kb_cook_sku_price_list

    @kb_cook_sku_price_list.setter
    def kb_cook_sku_price_list(self, value):
        if isinstance(value, list):
            self._kb_cook_sku_price_list = list()
            for i in value:
                if isinstance(i, KbdishCookPriceInfo):
                    self._kb_cook_sku_price_list.append(i)
                else:
                    self._kb_cook_sku_price_list.append(KbdishCookPriceInfo.from_alipay_dict(i))
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


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
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.flag:
            if hasattr(self.flag, 'to_alipay_dict'):
                params['flag'] = self.flag.to_alipay_dict()
            else:
                params['flag'] = self.flag
        if self.kb_cook_sku_price_list:
            if isinstance(self.kb_cook_sku_price_list, list):
                for i in range(0, len(self.kb_cook_sku_price_list)):
                    element = self.kb_cook_sku_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kb_cook_sku_price_list[i] = element.to_alipay_dict()
            if hasattr(self.kb_cook_sku_price_list, 'to_alipay_dict'):
                params['kb_cook_sku_price_list'] = self.kb_cook_sku_price_list.to_alipay_dict()
            else:
                params['kb_cook_sku_price_list'] = self.kb_cook_sku_price_list
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
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
        o = KbdishCookDetailInfo()
        if 'catetory_big_id' in d:
            o.catetory_big_id = d['catetory_big_id']
        if 'catetory_small_id' in d:
            o.catetory_small_id = d['catetory_small_id']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'flag' in d:
            o.flag = d['flag']
        if 'kb_cook_sku_price_list' in d:
            o.kb_cook_sku_price_list = d['kb_cook_sku_price_list']
        if 'sort' in d:
            o.sort = d['sort']
        if 'status' in d:
            o.status = d['status']
        return o


