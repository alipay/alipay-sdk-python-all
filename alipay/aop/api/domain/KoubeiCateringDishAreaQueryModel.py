#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishAreaQueryModel(object):

    def __init__(self):
        self._area_id = None
        self._area_name = None
        self._merchant_id = None
        self._shop_id = None
        self._status = None
        self._tab_id = None

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
    def tab_id(self):
        return self._tab_id

    @tab_id.setter
    def tab_id(self, value):
        self._tab_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.tab_id:
            if hasattr(self.tab_id, 'to_alipay_dict'):
                params['tab_id'] = self.tab_id.to_alipay_dict()
            else:
                params['tab_id'] = self.tab_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishAreaQueryModel()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'tab_id' in d:
            o.tab_id = d['tab_id']
        return o


