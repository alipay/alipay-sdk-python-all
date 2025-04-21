#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityBean(object):

    def __init__(self):
        self._activity_id = None
        self._amt = None
        self._discount_sku_id = None
        self._id_value = None
        self._item_id = None
        self._origin_sku_id = None
        self._show_amt = None
        self._type = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        self._amt = value
    @property
    def discount_sku_id(self):
        return self._discount_sku_id

    @discount_sku_id.setter
    def discount_sku_id(self, value):
        self._discount_sku_id = value
    @property
    def id_value(self):
        return self._id_value

    @id_value.setter
    def id_value(self, value):
        self._id_value = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def origin_sku_id(self):
        return self._origin_sku_id

    @origin_sku_id.setter
    def origin_sku_id(self, value):
        self._origin_sku_id = value
    @property
    def show_amt(self):
        return self._show_amt

    @show_amt.setter
    def show_amt(self, value):
        self._show_amt = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.discount_sku_id:
            if hasattr(self.discount_sku_id, 'to_alipay_dict'):
                params['discount_sku_id'] = self.discount_sku_id.to_alipay_dict()
            else:
                params['discount_sku_id'] = self.discount_sku_id
        if self.id_value:
            if hasattr(self.id_value, 'to_alipay_dict'):
                params['id_value'] = self.id_value.to_alipay_dict()
            else:
                params['id_value'] = self.id_value
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.origin_sku_id:
            if hasattr(self.origin_sku_id, 'to_alipay_dict'):
                params['origin_sku_id'] = self.origin_sku_id.to_alipay_dict()
            else:
                params['origin_sku_id'] = self.origin_sku_id
        if self.show_amt:
            if hasattr(self.show_amt, 'to_alipay_dict'):
                params['show_amt'] = self.show_amt.to_alipay_dict()
            else:
                params['show_amt'] = self.show_amt
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityBean()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'amt' in d:
            o.amt = d['amt']
        if 'discount_sku_id' in d:
            o.discount_sku_id = d['discount_sku_id']
        if 'id_value' in d:
            o.id_value = d['id_value']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'origin_sku_id' in d:
            o.origin_sku_id = d['origin_sku_id']
        if 'show_amt' in d:
            o.show_amt = d['show_amt']
        if 'type' in d:
            o.type = d['type']
        return o


