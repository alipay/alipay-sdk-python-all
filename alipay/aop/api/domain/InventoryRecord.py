#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InventoryRecord(object):

    def __init__(self):
        self._after_modify_lock_quantity = None
        self._after_modify_quantity = None
        self._batch_code = None
        self._before_modify_lock_quantity = None
        self._before_modify_quantity = None
        self._diff_lock_quantity = None
        self._diff_quantity = None
        self._expire_date = None
        self._gmt_create = None
        self._gmt_modified = None
        self._goods_code = None
        self._inventory_type = None
        self._operate_type = None
        self._out_biz_id = None
        self._product_date = None
        self._remark = None
        self._warehouse_code = None

    @property
    def after_modify_lock_quantity(self):
        return self._after_modify_lock_quantity

    @after_modify_lock_quantity.setter
    def after_modify_lock_quantity(self, value):
        self._after_modify_lock_quantity = value
    @property
    def after_modify_quantity(self):
        return self._after_modify_quantity

    @after_modify_quantity.setter
    def after_modify_quantity(self, value):
        self._after_modify_quantity = value
    @property
    def batch_code(self):
        return self._batch_code

    @batch_code.setter
    def batch_code(self, value):
        self._batch_code = value
    @property
    def before_modify_lock_quantity(self):
        return self._before_modify_lock_quantity

    @before_modify_lock_quantity.setter
    def before_modify_lock_quantity(self, value):
        self._before_modify_lock_quantity = value
    @property
    def before_modify_quantity(self):
        return self._before_modify_quantity

    @before_modify_quantity.setter
    def before_modify_quantity(self, value):
        self._before_modify_quantity = value
    @property
    def diff_lock_quantity(self):
        return self._diff_lock_quantity

    @diff_lock_quantity.setter
    def diff_lock_quantity(self, value):
        self._diff_lock_quantity = value
    @property
    def diff_quantity(self):
        return self._diff_quantity

    @diff_quantity.setter
    def diff_quantity(self, value):
        self._diff_quantity = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
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
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def product_date(self):
        return self._product_date

    @product_date.setter
    def product_date(self, value):
        self._product_date = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_modify_lock_quantity:
            if hasattr(self.after_modify_lock_quantity, 'to_alipay_dict'):
                params['after_modify_lock_quantity'] = self.after_modify_lock_quantity.to_alipay_dict()
            else:
                params['after_modify_lock_quantity'] = self.after_modify_lock_quantity
        if self.after_modify_quantity:
            if hasattr(self.after_modify_quantity, 'to_alipay_dict'):
                params['after_modify_quantity'] = self.after_modify_quantity.to_alipay_dict()
            else:
                params['after_modify_quantity'] = self.after_modify_quantity
        if self.batch_code:
            if hasattr(self.batch_code, 'to_alipay_dict'):
                params['batch_code'] = self.batch_code.to_alipay_dict()
            else:
                params['batch_code'] = self.batch_code
        if self.before_modify_lock_quantity:
            if hasattr(self.before_modify_lock_quantity, 'to_alipay_dict'):
                params['before_modify_lock_quantity'] = self.before_modify_lock_quantity.to_alipay_dict()
            else:
                params['before_modify_lock_quantity'] = self.before_modify_lock_quantity
        if self.before_modify_quantity:
            if hasattr(self.before_modify_quantity, 'to_alipay_dict'):
                params['before_modify_quantity'] = self.before_modify_quantity.to_alipay_dict()
            else:
                params['before_modify_quantity'] = self.before_modify_quantity
        if self.diff_lock_quantity:
            if hasattr(self.diff_lock_quantity, 'to_alipay_dict'):
                params['diff_lock_quantity'] = self.diff_lock_quantity.to_alipay_dict()
            else:
                params['diff_lock_quantity'] = self.diff_lock_quantity
        if self.diff_quantity:
            if hasattr(self.diff_quantity, 'to_alipay_dict'):
                params['diff_quantity'] = self.diff_quantity.to_alipay_dict()
            else:
                params['diff_quantity'] = self.diff_quantity
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
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
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.product_date:
            if hasattr(self.product_date, 'to_alipay_dict'):
                params['product_date'] = self.product_date.to_alipay_dict()
            else:
                params['product_date'] = self.product_date
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InventoryRecord()
        if 'after_modify_lock_quantity' in d:
            o.after_modify_lock_quantity = d['after_modify_lock_quantity']
        if 'after_modify_quantity' in d:
            o.after_modify_quantity = d['after_modify_quantity']
        if 'batch_code' in d:
            o.batch_code = d['batch_code']
        if 'before_modify_lock_quantity' in d:
            o.before_modify_lock_quantity = d['before_modify_lock_quantity']
        if 'before_modify_quantity' in d:
            o.before_modify_quantity = d['before_modify_quantity']
        if 'diff_lock_quantity' in d:
            o.diff_lock_quantity = d['diff_lock_quantity']
        if 'diff_quantity' in d:
            o.diff_quantity = d['diff_quantity']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'remark' in d:
            o.remark = d['remark']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


