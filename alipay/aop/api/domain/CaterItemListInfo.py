#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaterItemListInfo(object):

    def __init__(self):
        self._gmt_modified = None
        self._inventory = None
        self._item_id = None
        self._item_status = None
        self._original_price = None
        self._price = None
        self._reject_reason = None
        self._subject = None
        self._validity_period = None

    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        self._validity_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.validity_period:
            if hasattr(self.validity_period, 'to_alipay_dict'):
                params['validity_period'] = self.validity_period.to_alipay_dict()
            else:
                params['validity_period'] = self.validity_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaterItemListInfo()
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_status' in d:
            o.item_status = d['item_status']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'subject' in d:
            o.subject = d['subject']
        if 'validity_period' in d:
            o.validity_period = d['validity_period']
        return o


