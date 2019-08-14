#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InventoryItem(object):

    def __init__(self):
        self._available_qty = None
        self._ext_info = None
        self._on_hand_qty = None
        self._sku_no = None
        self._total_qty = None
        self._warehouse_code = None

    @property
    def available_qty(self):
        return self._available_qty

    @available_qty.setter
    def available_qty(self, value):
        self._available_qty = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def on_hand_qty(self):
        return self._on_hand_qty

    @on_hand_qty.setter
    def on_hand_qty(self, value):
        self._on_hand_qty = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value
    @property
    def total_qty(self):
        return self._total_qty

    @total_qty.setter
    def total_qty(self, value):
        self._total_qty = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_qty:
            if hasattr(self.available_qty, 'to_alipay_dict'):
                params['available_qty'] = self.available_qty.to_alipay_dict()
            else:
                params['available_qty'] = self.available_qty
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.on_hand_qty:
            if hasattr(self.on_hand_qty, 'to_alipay_dict'):
                params['on_hand_qty'] = self.on_hand_qty.to_alipay_dict()
            else:
                params['on_hand_qty'] = self.on_hand_qty
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        if self.total_qty:
            if hasattr(self.total_qty, 'to_alipay_dict'):
                params['total_qty'] = self.total_qty.to_alipay_dict()
            else:
                params['total_qty'] = self.total_qty
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
        o = InventoryItem()
        if 'available_qty' in d:
            o.available_qty = d['available_qty']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'on_hand_qty' in d:
            o.on_hand_qty = d['on_hand_qty']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        if 'total_qty' in d:
            o.total_qty = d['total_qty']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


