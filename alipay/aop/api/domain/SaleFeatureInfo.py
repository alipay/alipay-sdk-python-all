#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleFeatureInfo(object):

    def __init__(self):
        self._is_sales_amount_a = None
        self._is_sales_amount_b = None
        self._is_sales_amount_c = None
        self._is_sales_amount_d = None
        self._is_sales_volume_a = None
        self._is_sales_volume_b = None
        self._is_sales_volume_c = None
        self._is_sales_volume_d = None
        self._item_num = None
        self._month = None
        self._sales_amount_mom = None
        self._sales_amount_yoy = None

    @property
    def is_sales_amount_a(self):
        return self._is_sales_amount_a

    @is_sales_amount_a.setter
    def is_sales_amount_a(self, value):
        self._is_sales_amount_a = value
    @property
    def is_sales_amount_b(self):
        return self._is_sales_amount_b

    @is_sales_amount_b.setter
    def is_sales_amount_b(self, value):
        self._is_sales_amount_b = value
    @property
    def is_sales_amount_c(self):
        return self._is_sales_amount_c

    @is_sales_amount_c.setter
    def is_sales_amount_c(self, value):
        self._is_sales_amount_c = value
    @property
    def is_sales_amount_d(self):
        return self._is_sales_amount_d

    @is_sales_amount_d.setter
    def is_sales_amount_d(self, value):
        self._is_sales_amount_d = value
    @property
    def is_sales_volume_a(self):
        return self._is_sales_volume_a

    @is_sales_volume_a.setter
    def is_sales_volume_a(self, value):
        self._is_sales_volume_a = value
    @property
    def is_sales_volume_b(self):
        return self._is_sales_volume_b

    @is_sales_volume_b.setter
    def is_sales_volume_b(self, value):
        self._is_sales_volume_b = value
    @property
    def is_sales_volume_c(self):
        return self._is_sales_volume_c

    @is_sales_volume_c.setter
    def is_sales_volume_c(self, value):
        self._is_sales_volume_c = value
    @property
    def is_sales_volume_d(self):
        return self._is_sales_volume_d

    @is_sales_volume_d.setter
    def is_sales_volume_d(self, value):
        self._is_sales_volume_d = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def sales_amount_mom(self):
        return self._sales_amount_mom

    @sales_amount_mom.setter
    def sales_amount_mom(self, value):
        self._sales_amount_mom = value
    @property
    def sales_amount_yoy(self):
        return self._sales_amount_yoy

    @sales_amount_yoy.setter
    def sales_amount_yoy(self, value):
        self._sales_amount_yoy = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_sales_amount_a:
            if hasattr(self.is_sales_amount_a, 'to_alipay_dict'):
                params['is_sales_amount_a'] = self.is_sales_amount_a.to_alipay_dict()
            else:
                params['is_sales_amount_a'] = self.is_sales_amount_a
        if self.is_sales_amount_b:
            if hasattr(self.is_sales_amount_b, 'to_alipay_dict'):
                params['is_sales_amount_b'] = self.is_sales_amount_b.to_alipay_dict()
            else:
                params['is_sales_amount_b'] = self.is_sales_amount_b
        if self.is_sales_amount_c:
            if hasattr(self.is_sales_amount_c, 'to_alipay_dict'):
                params['is_sales_amount_c'] = self.is_sales_amount_c.to_alipay_dict()
            else:
                params['is_sales_amount_c'] = self.is_sales_amount_c
        if self.is_sales_amount_d:
            if hasattr(self.is_sales_amount_d, 'to_alipay_dict'):
                params['is_sales_amount_d'] = self.is_sales_amount_d.to_alipay_dict()
            else:
                params['is_sales_amount_d'] = self.is_sales_amount_d
        if self.is_sales_volume_a:
            if hasattr(self.is_sales_volume_a, 'to_alipay_dict'):
                params['is_sales_volume_a'] = self.is_sales_volume_a.to_alipay_dict()
            else:
                params['is_sales_volume_a'] = self.is_sales_volume_a
        if self.is_sales_volume_b:
            if hasattr(self.is_sales_volume_b, 'to_alipay_dict'):
                params['is_sales_volume_b'] = self.is_sales_volume_b.to_alipay_dict()
            else:
                params['is_sales_volume_b'] = self.is_sales_volume_b
        if self.is_sales_volume_c:
            if hasattr(self.is_sales_volume_c, 'to_alipay_dict'):
                params['is_sales_volume_c'] = self.is_sales_volume_c.to_alipay_dict()
            else:
                params['is_sales_volume_c'] = self.is_sales_volume_c
        if self.is_sales_volume_d:
            if hasattr(self.is_sales_volume_d, 'to_alipay_dict'):
                params['is_sales_volume_d'] = self.is_sales_volume_d.to_alipay_dict()
            else:
                params['is_sales_volume_d'] = self.is_sales_volume_d
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.sales_amount_mom:
            if hasattr(self.sales_amount_mom, 'to_alipay_dict'):
                params['sales_amount_mom'] = self.sales_amount_mom.to_alipay_dict()
            else:
                params['sales_amount_mom'] = self.sales_amount_mom
        if self.sales_amount_yoy:
            if hasattr(self.sales_amount_yoy, 'to_alipay_dict'):
                params['sales_amount_yoy'] = self.sales_amount_yoy.to_alipay_dict()
            else:
                params['sales_amount_yoy'] = self.sales_amount_yoy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleFeatureInfo()
        if 'is_sales_amount_a' in d:
            o.is_sales_amount_a = d['is_sales_amount_a']
        if 'is_sales_amount_b' in d:
            o.is_sales_amount_b = d['is_sales_amount_b']
        if 'is_sales_amount_c' in d:
            o.is_sales_amount_c = d['is_sales_amount_c']
        if 'is_sales_amount_d' in d:
            o.is_sales_amount_d = d['is_sales_amount_d']
        if 'is_sales_volume_a' in d:
            o.is_sales_volume_a = d['is_sales_volume_a']
        if 'is_sales_volume_b' in d:
            o.is_sales_volume_b = d['is_sales_volume_b']
        if 'is_sales_volume_c' in d:
            o.is_sales_volume_c = d['is_sales_volume_c']
        if 'is_sales_volume_d' in d:
            o.is_sales_volume_d = d['is_sales_volume_d']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'month' in d:
            o.month = d['month']
        if 'sales_amount_mom' in d:
            o.sales_amount_mom = d['sales_amount_mom']
        if 'sales_amount_yoy' in d:
            o.sales_amount_yoy = d['sales_amount_yoy']
        return o


