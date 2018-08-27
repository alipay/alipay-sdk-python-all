#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopDiscountInfo(object):

    def __init__(self):
        self._cover = None
        self._description = None
        self._is_all = None
        self._item_id = None
        self._promo_sub_type = None
        self._promotion_type = None
        self._purchase_mode = None
        self._sales_quantity = None
        self._subject = None

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def is_all(self):
        return self._is_all

    @is_all.setter
    def is_all(self, value):
        self._is_all = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def promo_sub_type(self):
        return self._promo_sub_type

    @promo_sub_type.setter
    def promo_sub_type(self, value):
        self._promo_sub_type = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
    @property
    def sales_quantity(self):
        return self._sales_quantity

    @sales_quantity.setter
    def sales_quantity(self, value):
        self._sales_quantity = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.is_all:
            if hasattr(self.is_all, 'to_alipay_dict'):
                params['is_all'] = self.is_all.to_alipay_dict()
            else:
                params['is_all'] = self.is_all
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.promo_sub_type:
            if hasattr(self.promo_sub_type, 'to_alipay_dict'):
                params['promo_sub_type'] = self.promo_sub_type.to_alipay_dict()
            else:
                params['promo_sub_type'] = self.promo_sub_type
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.purchase_mode:
            if hasattr(self.purchase_mode, 'to_alipay_dict'):
                params['purchase_mode'] = self.purchase_mode.to_alipay_dict()
            else:
                params['purchase_mode'] = self.purchase_mode
        if self.sales_quantity:
            if hasattr(self.sales_quantity, 'to_alipay_dict'):
                params['sales_quantity'] = self.sales_quantity.to_alipay_dict()
            else:
                params['sales_quantity'] = self.sales_quantity
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopDiscountInfo()
        if 'cover' in d:
            o.cover = d['cover']
        if 'description' in d:
            o.description = d['description']
        if 'is_all' in d:
            o.is_all = d['is_all']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'promo_sub_type' in d:
            o.promo_sub_type = d['promo_sub_type']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'purchase_mode' in d:
            o.purchase_mode = d['purchase_mode']
        if 'sales_quantity' in d:
            o.sales_quantity = d['sales_quantity']
        if 'subject' in d:
            o.subject = d['subject']
        return o


