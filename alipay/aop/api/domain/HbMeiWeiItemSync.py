#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbMeiWeiItemSync(object):

    def __init__(self):
        self._amount_rights = None
        self._biz_item_id = None
        self._inventory = None
        self._price = None
        self._sale_count = None
        self._status = None
        self._uv_count = None

    @property
    def amount_rights(self):
        return self._amount_rights

    @amount_rights.setter
    def amount_rights(self, value):
        self._amount_rights = value
    @property
    def biz_item_id(self):
        return self._biz_item_id

    @biz_item_id.setter
    def biz_item_id(self, value):
        self._biz_item_id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sale_count(self):
        return self._sale_count

    @sale_count.setter
    def sale_count(self, value):
        self._sale_count = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def uv_count(self):
        return self._uv_count

    @uv_count.setter
    def uv_count(self, value):
        self._uv_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_rights:
            if hasattr(self.amount_rights, 'to_alipay_dict'):
                params['amount_rights'] = self.amount_rights.to_alipay_dict()
            else:
                params['amount_rights'] = self.amount_rights
        if self.biz_item_id:
            if hasattr(self.biz_item_id, 'to_alipay_dict'):
                params['biz_item_id'] = self.biz_item_id.to_alipay_dict()
            else:
                params['biz_item_id'] = self.biz_item_id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sale_count:
            if hasattr(self.sale_count, 'to_alipay_dict'):
                params['sale_count'] = self.sale_count.to_alipay_dict()
            else:
                params['sale_count'] = self.sale_count
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.uv_count:
            if hasattr(self.uv_count, 'to_alipay_dict'):
                params['uv_count'] = self.uv_count.to_alipay_dict()
            else:
                params['uv_count'] = self.uv_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbMeiWeiItemSync()
        if 'amount_rights' in d:
            o.amount_rights = d['amount_rights']
        if 'biz_item_id' in d:
            o.biz_item_id = d['biz_item_id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'price' in d:
            o.price = d['price']
        if 'sale_count' in d:
            o.sale_count = d['sale_count']
        if 'status' in d:
            o.status = d['status']
        if 'uv_count' in d:
            o.uv_count = d['uv_count']
        return o


