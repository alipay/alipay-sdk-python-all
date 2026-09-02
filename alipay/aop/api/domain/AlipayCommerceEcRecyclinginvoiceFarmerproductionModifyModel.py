#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerproductionModifyModel(object):

    def __init__(self):
        self._farmer_item_id = None
        self._item_num = None
        self._item_unit = None
        self._sale_end_date = None
        self._sale_start_date = None

    @property
    def farmer_item_id(self):
        return self._farmer_item_id

    @farmer_item_id.setter
    def farmer_item_id(self, value):
        self._farmer_item_id = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
    @property
    def sale_end_date(self):
        return self._sale_end_date

    @sale_end_date.setter
    def sale_end_date(self, value):
        self._sale_end_date = value
    @property
    def sale_start_date(self):
        return self._sale_start_date

    @sale_start_date.setter
    def sale_start_date(self, value):
        self._sale_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.farmer_item_id:
            if hasattr(self.farmer_item_id, 'to_alipay_dict'):
                params['farmer_item_id'] = self.farmer_item_id.to_alipay_dict()
            else:
                params['farmer_item_id'] = self.farmer_item_id
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        if self.sale_end_date:
            if hasattr(self.sale_end_date, 'to_alipay_dict'):
                params['sale_end_date'] = self.sale_end_date.to_alipay_dict()
            else:
                params['sale_end_date'] = self.sale_end_date
        if self.sale_start_date:
            if hasattr(self.sale_start_date, 'to_alipay_dict'):
                params['sale_start_date'] = self.sale_start_date.to_alipay_dict()
            else:
                params['sale_start_date'] = self.sale_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerproductionModifyModel()
        if 'farmer_item_id' in d:
            o.farmer_item_id = d['farmer_item_id']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'sale_end_date' in d:
            o.sale_end_date = d['sale_end_date']
        if 'sale_start_date' in d:
            o.sale_start_date = d['sale_start_date']
        return o


