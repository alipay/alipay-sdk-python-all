#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemOrderOpenData(object):

    def __init__(self):
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._item_id = None
        self._item_name = None
        self._item_order_id = None
        self._order_id = None
        self._quantity = None
        self._real_amount = None
        self._sku_id = None
        self._snapshot_id = None
        self._status = None
        self._subsidy_amount = None
        self._unit_price = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_order_id(self):
        return self._item_order_id

    @item_order_id.setter
    def item_order_id(self, value):
        self._item_order_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subsidy_amount(self):
        return self._subsidy_amount

    @subsidy_amount.setter
    def subsidy_amount(self, value):
        self._subsidy_amount = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_order_id:
            if hasattr(self.item_order_id, 'to_alipay_dict'):
                params['item_order_id'] = self.item_order_id.to_alipay_dict()
            else:
                params['item_order_id'] = self.item_order_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.snapshot_id:
            if hasattr(self.snapshot_id, 'to_alipay_dict'):
                params['snapshot_id'] = self.snapshot_id.to_alipay_dict()
            else:
                params['snapshot_id'] = self.snapshot_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subsidy_amount:
            if hasattr(self.subsidy_amount, 'to_alipay_dict'):
                params['subsidy_amount'] = self.subsidy_amount.to_alipay_dict()
            else:
                params['subsidy_amount'] = self.subsidy_amount
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemOrderOpenData()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_order_id' in d:
            o.item_order_id = d['item_order_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'snapshot_id' in d:
            o.snapshot_id = d['snapshot_id']
        if 'status' in d:
            o.status = d['status']
        if 'subsidy_amount' in d:
            o.subsidy_amount = d['subsidy_amount']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


