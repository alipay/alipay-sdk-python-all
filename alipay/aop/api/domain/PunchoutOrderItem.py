#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PunchoutOrderItem(object):

    def __init__(self):
        self._contract_id = None
        self._currency_code = None
        self._item_description = None
        self._item_id = None
        self._item_name = None
        self._mall_category_id = None
        self._quantity = None
        self._sku_id = None
        self._sub_pur_req_id = None
        self._supplier_id = None
        self._tax_rate = None
        self._unit_price = None
        self._uom = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value
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
    def mall_category_id(self):
        return self._mall_category_id

    @mall_category_id.setter
    def mall_category_id(self, value):
        self._mall_category_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sub_pur_req_id(self):
        return self._sub_pur_req_id

    @sub_pur_req_id.setter
    def sub_pur_req_id(self, value):
        self._sub_pur_req_id = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
    @property
    def uom(self):
        return self._uom

    @uom.setter
    def uom(self, value):
        self._uom = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.item_description:
            if hasattr(self.item_description, 'to_alipay_dict'):
                params['item_description'] = self.item_description.to_alipay_dict()
            else:
                params['item_description'] = self.item_description
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
        if self.mall_category_id:
            if hasattr(self.mall_category_id, 'to_alipay_dict'):
                params['mall_category_id'] = self.mall_category_id.to_alipay_dict()
            else:
                params['mall_category_id'] = self.mall_category_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sub_pur_req_id:
            if hasattr(self.sub_pur_req_id, 'to_alipay_dict'):
                params['sub_pur_req_id'] = self.sub_pur_req_id.to_alipay_dict()
            else:
                params['sub_pur_req_id'] = self.sub_pur_req_id
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        if self.uom:
            if hasattr(self.uom, 'to_alipay_dict'):
                params['uom'] = self.uom.to_alipay_dict()
            else:
                params['uom'] = self.uom
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PunchoutOrderItem()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'item_description' in d:
            o.item_description = d['item_description']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'mall_category_id' in d:
            o.mall_category_id = d['mall_category_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sub_pur_req_id' in d:
            o.sub_pur_req_id = d['sub_pur_req_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        if 'uom' in d:
            o.uom = d['uom']
        return o


