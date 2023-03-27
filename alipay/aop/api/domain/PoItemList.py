#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoItemList(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._po_item_id = None
        self._po_item_num = None
        self._pr_item_id = None
        self._pr_number = None
        self._quantity = None
        self._receiver_address = None
        self._receiver_name = None
        self._receiver_phone = None
        self._source_product_id = None
        self._source_sku_id = None
        self._unit_price = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def po_item_id(self):
        return self._po_item_id

    @po_item_id.setter
    def po_item_id(self, value):
        self._po_item_id = value
    @property
    def po_item_num(self):
        return self._po_item_num

    @po_item_num.setter
    def po_item_num(self, value):
        self._po_item_num = value
    @property
    def pr_item_id(self):
        return self._pr_item_id

    @pr_item_id.setter
    def pr_item_id(self, value):
        self._pr_item_id = value
    @property
    def pr_number(self):
        return self._pr_number

    @pr_number.setter
    def pr_number(self, value):
        self._pr_number = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def source_product_id(self):
        return self._source_product_id

    @source_product_id.setter
    def source_product_id(self, value):
        self._source_product_id = value
    @property
    def source_sku_id(self):
        return self._source_sku_id

    @source_sku_id.setter
    def source_sku_id(self, value):
        self._source_sku_id = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.po_item_id:
            if hasattr(self.po_item_id, 'to_alipay_dict'):
                params['po_item_id'] = self.po_item_id.to_alipay_dict()
            else:
                params['po_item_id'] = self.po_item_id
        if self.po_item_num:
            if hasattr(self.po_item_num, 'to_alipay_dict'):
                params['po_item_num'] = self.po_item_num.to_alipay_dict()
            else:
                params['po_item_num'] = self.po_item_num
        if self.pr_item_id:
            if hasattr(self.pr_item_id, 'to_alipay_dict'):
                params['pr_item_id'] = self.pr_item_id.to_alipay_dict()
            else:
                params['pr_item_id'] = self.pr_item_id
        if self.pr_number:
            if hasattr(self.pr_number, 'to_alipay_dict'):
                params['pr_number'] = self.pr_number.to_alipay_dict()
            else:
                params['pr_number'] = self.pr_number
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.source_product_id:
            if hasattr(self.source_product_id, 'to_alipay_dict'):
                params['source_product_id'] = self.source_product_id.to_alipay_dict()
            else:
                params['source_product_id'] = self.source_product_id
        if self.source_sku_id:
            if hasattr(self.source_sku_id, 'to_alipay_dict'):
                params['source_sku_id'] = self.source_sku_id.to_alipay_dict()
            else:
                params['source_sku_id'] = self.source_sku_id
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
        o = PoItemList()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'po_item_id' in d:
            o.po_item_id = d['po_item_id']
        if 'po_item_num' in d:
            o.po_item_num = d['po_item_num']
        if 'pr_item_id' in d:
            o.pr_item_id = d['pr_item_id']
        if 'pr_number' in d:
            o.pr_number = d['pr_number']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'source_product_id' in d:
            o.source_product_id = d['source_product_id']
        if 'source_sku_id' in d:
            o.source_sku_id = d['source_sku_id']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


