#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierReportDetail(object):

    def __init__(self):
        self._batch_code = None
        self._expire_date = None
        self._goods_code = None
        self._inventory_type = None
        self._price = None
        self._production_date = None
        self._quantity_diff = None
        self._report_type = None
        self._supplier_report_detail_id = None
        self._supplier_report_id = None

    @property
    def batch_code(self):
        return self._batch_code

    @batch_code.setter
    def batch_code(self, value):
        self._batch_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def inventory_type(self):
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, value):
        self._inventory_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def production_date(self):
        return self._production_date

    @production_date.setter
    def production_date(self, value):
        self._production_date = value
    @property
    def quantity_diff(self):
        return self._quantity_diff

    @quantity_diff.setter
    def quantity_diff(self, value):
        self._quantity_diff = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def supplier_report_detail_id(self):
        return self._supplier_report_detail_id

    @supplier_report_detail_id.setter
    def supplier_report_detail_id(self, value):
        self._supplier_report_detail_id = value
    @property
    def supplier_report_id(self):
        return self._supplier_report_id

    @supplier_report_id.setter
    def supplier_report_id(self, value):
        self._supplier_report_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_code:
            if hasattr(self.batch_code, 'to_alipay_dict'):
                params['batch_code'] = self.batch_code.to_alipay_dict()
            else:
                params['batch_code'] = self.batch_code
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.inventory_type:
            if hasattr(self.inventory_type, 'to_alipay_dict'):
                params['inventory_type'] = self.inventory_type.to_alipay_dict()
            else:
                params['inventory_type'] = self.inventory_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.production_date:
            if hasattr(self.production_date, 'to_alipay_dict'):
                params['production_date'] = self.production_date.to_alipay_dict()
            else:
                params['production_date'] = self.production_date
        if self.quantity_diff:
            if hasattr(self.quantity_diff, 'to_alipay_dict'):
                params['quantity_diff'] = self.quantity_diff.to_alipay_dict()
            else:
                params['quantity_diff'] = self.quantity_diff
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.supplier_report_detail_id:
            if hasattr(self.supplier_report_detail_id, 'to_alipay_dict'):
                params['supplier_report_detail_id'] = self.supplier_report_detail_id.to_alipay_dict()
            else:
                params['supplier_report_detail_id'] = self.supplier_report_detail_id
        if self.supplier_report_id:
            if hasattr(self.supplier_report_id, 'to_alipay_dict'):
                params['supplier_report_id'] = self.supplier_report_id.to_alipay_dict()
            else:
                params['supplier_report_id'] = self.supplier_report_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierReportDetail()
        if 'batch_code' in d:
            o.batch_code = d['batch_code']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'price' in d:
            o.price = d['price']
        if 'production_date' in d:
            o.production_date = d['production_date']
        if 'quantity_diff' in d:
            o.quantity_diff = d['quantity_diff']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'supplier_report_detail_id' in d:
            o.supplier_report_detail_id = d['supplier_report_detail_id']
        if 'supplier_report_id' in d:
            o.supplier_report_id = d['supplier_report_id']
        return o


