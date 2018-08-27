#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishAreaFreeInfo(object):

    def __init__(self):
        self._area_id = None
        self._count = None
        self._dish_id = None
        self._dish_sku_id = None
        self._status = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_sku_id(self):
        return self._dish_sku_id

    @dish_sku_id.setter
    def dish_sku_id(self, value):
        self._dish_sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_sku_id:
            if hasattr(self.dish_sku_id, 'to_alipay_dict'):
                params['dish_sku_id'] = self.dish_sku_id.to_alipay_dict()
            else:
                params['dish_sku_id'] = self.dish_sku_id
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
        o = KbdishAreaFreeInfo()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'count' in d:
            o.count = d['count']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_sku_id' in d:
            o.dish_sku_id = d['dish_sku_id']
        if 'status' in d:
            o.status = d['status']
        return o


