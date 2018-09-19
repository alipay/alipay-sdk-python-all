#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishAreaFreeInfo import KbdishAreaFreeInfo
from alipay.aop.api.domain.KbdishTabInfo import KbdishTabInfo


class KbdishAreaInfo(object):

    def __init__(self):
        self._area_free_list = None
        self._area_id = None
        self._area_name = None
        self._area_sort = None
        self._create_user = None
        self._fee_price = None
        self._merchant_id = None
        self._shop_id = None
        self._status = None
        self._tab_count = None
        self._tab_list = None
        self._update_user = None

    @property
    def area_free_list(self):
        return self._area_free_list

    @area_free_list.setter
    def area_free_list(self, value):
        if isinstance(value, list):
            self._area_free_list = list()
            for i in value:
                if isinstance(i, KbdishAreaFreeInfo):
                    self._area_free_list.append(i)
                else:
                    self._area_free_list.append(KbdishAreaFreeInfo.from_alipay_dict(i))
    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def area_sort(self):
        return self._area_sort

    @area_sort.setter
    def area_sort(self, value):
        self._area_sort = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def fee_price(self):
        return self._fee_price

    @fee_price.setter
    def fee_price(self, value):
        self._fee_price = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tab_count(self):
        return self._tab_count

    @tab_count.setter
    def tab_count(self, value):
        self._tab_count = value
    @property
    def tab_list(self):
        return self._tab_list

    @tab_list.setter
    def tab_list(self, value):
        if isinstance(value, list):
            self._tab_list = list()
            for i in value:
                if isinstance(i, KbdishTabInfo):
                    self._tab_list.append(i)
                else:
                    self._tab_list.append(KbdishTabInfo.from_alipay_dict(i))
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_free_list:
            if isinstance(self.area_free_list, list):
                for i in range(0, len(self.area_free_list)):
                    element = self.area_free_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.area_free_list[i] = element.to_alipay_dict()
            if hasattr(self.area_free_list, 'to_alipay_dict'):
                params['area_free_list'] = self.area_free_list.to_alipay_dict()
            else:
                params['area_free_list'] = self.area_free_list
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.area_sort:
            if hasattr(self.area_sort, 'to_alipay_dict'):
                params['area_sort'] = self.area_sort.to_alipay_dict()
            else:
                params['area_sort'] = self.area_sort
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.fee_price:
            if hasattr(self.fee_price, 'to_alipay_dict'):
                params['fee_price'] = self.fee_price.to_alipay_dict()
            else:
                params['fee_price'] = self.fee_price
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tab_count:
            if hasattr(self.tab_count, 'to_alipay_dict'):
                params['tab_count'] = self.tab_count.to_alipay_dict()
            else:
                params['tab_count'] = self.tab_count
        if self.tab_list:
            if isinstance(self.tab_list, list):
                for i in range(0, len(self.tab_list)):
                    element = self.tab_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tab_list[i] = element.to_alipay_dict()
            if hasattr(self.tab_list, 'to_alipay_dict'):
                params['tab_list'] = self.tab_list.to_alipay_dict()
            else:
                params['tab_list'] = self.tab_list
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishAreaInfo()
        if 'area_free_list' in d:
            o.area_free_list = d['area_free_list']
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'area_sort' in d:
            o.area_sort = d['area_sort']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'fee_price' in d:
            o.fee_price = d['fee_price']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'tab_count' in d:
            o.tab_count = d['tab_count']
        if 'tab_list' in d:
            o.tab_list = d['tab_list']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


