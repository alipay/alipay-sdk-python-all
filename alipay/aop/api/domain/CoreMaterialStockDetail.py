#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CoreMaterialStockDetail(object):

    def __init__(self):
        self._biz_date = None
        self._core_material_stock_id = None
        self._material_id = None
        self._material_name = None
        self._memo = None
        self._move_amount = None
        self._move_type = None
        self._out_biz_no = None
        self._stock_type = None
        self._warehouse_id = None
        self._warehouse_name = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def core_material_stock_id(self):
        return self._core_material_stock_id

    @core_material_stock_id.setter
    def core_material_stock_id(self, value):
        self._core_material_stock_id = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def move_amount(self):
        return self._move_amount

    @move_amount.setter
    def move_amount(self, value):
        self._move_amount = value
    @property
    def move_type(self):
        return self._move_type

    @move_type.setter
    def move_type(self, value):
        self._move_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def stock_type(self):
        return self._stock_type

    @stock_type.setter
    def stock_type(self, value):
        self._stock_type = value
    @property
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value
    @property
    def warehouse_name(self):
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, value):
        self._warehouse_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.core_material_stock_id:
            if hasattr(self.core_material_stock_id, 'to_alipay_dict'):
                params['core_material_stock_id'] = self.core_material_stock_id.to_alipay_dict()
            else:
                params['core_material_stock_id'] = self.core_material_stock_id
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.move_amount:
            if hasattr(self.move_amount, 'to_alipay_dict'):
                params['move_amount'] = self.move_amount.to_alipay_dict()
            else:
                params['move_amount'] = self.move_amount
        if self.move_type:
            if hasattr(self.move_type, 'to_alipay_dict'):
                params['move_type'] = self.move_type.to_alipay_dict()
            else:
                params['move_type'] = self.move_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.stock_type:
            if hasattr(self.stock_type, 'to_alipay_dict'):
                params['stock_type'] = self.stock_type.to_alipay_dict()
            else:
                params['stock_type'] = self.stock_type
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        if self.warehouse_name:
            if hasattr(self.warehouse_name, 'to_alipay_dict'):
                params['warehouse_name'] = self.warehouse_name.to_alipay_dict()
            else:
                params['warehouse_name'] = self.warehouse_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CoreMaterialStockDetail()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'core_material_stock_id' in d:
            o.core_material_stock_id = d['core_material_stock_id']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'move_amount' in d:
            o.move_amount = d['move_amount']
        if 'move_type' in d:
            o.move_type = d['move_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'stock_type' in d:
            o.stock_type = d['stock_type']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        if 'warehouse_name' in d:
            o.warehouse_name = d['warehouse_name']
        return o


