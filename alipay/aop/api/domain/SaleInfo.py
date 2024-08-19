#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleInfo(object):

    def __init__(self):
        self._item_num = None
        self._month = None
        self._sales_amount = None
        self._sales_amount_mom = None
        self._sales_amount_yoy = None
        self._sales_volume = None

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
    def sales_amount(self):
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        self._sales_amount = value
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
    @property
    def sales_volume(self):
        return self._sales_volume

    @sales_volume.setter
    def sales_volume(self, value):
        self._sales_volume = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.sales_amount:
            if hasattr(self.sales_amount, 'to_alipay_dict'):
                params['sales_amount'] = self.sales_amount.to_alipay_dict()
            else:
                params['sales_amount'] = self.sales_amount
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
        if self.sales_volume:
            if hasattr(self.sales_volume, 'to_alipay_dict'):
                params['sales_volume'] = self.sales_volume.to_alipay_dict()
            else:
                params['sales_volume'] = self.sales_volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleInfo()
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'month' in d:
            o.month = d['month']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        if 'sales_amount_mom' in d:
            o.sales_amount_mom = d['sales_amount_mom']
        if 'sales_amount_yoy' in d:
            o.sales_amount_yoy = d['sales_amount_yoy']
        if 'sales_volume' in d:
            o.sales_volume = d['sales_volume']
        return o


