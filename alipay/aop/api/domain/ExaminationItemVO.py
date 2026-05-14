#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationDiscount import ExaminationDiscount


class ExaminationItemVO(object):

    def __init__(self):
        self._amount_discount_amount = None
        self._amount_item = None
        self._consumable_amount = None
        self._discount = None
        self._drug_amount = None
        self._item_code = None
        self._price_sale = None
        self._quantity = None
        self._sku_id = None

    @property
    def amount_discount_amount(self):
        return self._amount_discount_amount

    @amount_discount_amount.setter
    def amount_discount_amount(self, value):
        self._amount_discount_amount = value
    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def consumable_amount(self):
        return self._consumable_amount

    @consumable_amount.setter
    def consumable_amount(self, value):
        self._consumable_amount = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, ExaminationDiscount):
            self._discount = value
        else:
            self._discount = ExaminationDiscount.from_alipay_dict(value)
    @property
    def drug_amount(self):
        return self._drug_amount

    @drug_amount.setter
    def drug_amount(self, value):
        self._drug_amount = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def price_sale(self):
        return self._price_sale

    @price_sale.setter
    def price_sale(self, value):
        self._price_sale = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.amount_discount_amount:
            if hasattr(self.amount_discount_amount, 'to_alipay_dict'):
                params['amount_discount_amount'] = self.amount_discount_amount.to_alipay_dict()
            else:
                params['amount_discount_amount'] = self.amount_discount_amount
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.consumable_amount:
            if hasattr(self.consumable_amount, 'to_alipay_dict'):
                params['consumable_amount'] = self.consumable_amount.to_alipay_dict()
            else:
                params['consumable_amount'] = self.consumable_amount
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.drug_amount:
            if hasattr(self.drug_amount, 'to_alipay_dict'):
                params['drug_amount'] = self.drug_amount.to_alipay_dict()
            else:
                params['drug_amount'] = self.drug_amount
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.price_sale:
            if hasattr(self.price_sale, 'to_alipay_dict'):
                params['price_sale'] = self.price_sale.to_alipay_dict()
            else:
                params['price_sale'] = self.price_sale
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationItemVO()
        if 'amount_discount_amount' in d:
            o.amount_discount_amount = d['amount_discount_amount']
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'consumable_amount' in d:
            o.consumable_amount = d['consumable_amount']
        if 'discount' in d:
            o.discount = d['discount']
        if 'drug_amount' in d:
            o.drug_amount = d['drug_amount']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'price_sale' in d:
            o.price_sale = d['price_sale']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


