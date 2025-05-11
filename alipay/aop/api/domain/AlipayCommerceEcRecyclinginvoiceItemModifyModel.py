#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceItemModifyModel(object):

    def __init__(self):
        self._company_item_id = None
        self._item_name = None
        self._item_spec = None
        self._item_unit = None
        self._product_id = None
        self._tax_no = None

    @property
    def company_item_id(self):
        return self._company_item_id

    @company_item_id.setter
    def company_item_id(self, value):
        self._company_item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_spec(self):
        return self._item_spec

    @item_spec.setter
    def item_spec(self, value):
        self._item_spec = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_item_id:
            if hasattr(self.company_item_id, 'to_alipay_dict'):
                params['company_item_id'] = self.company_item_id.to_alipay_dict()
            else:
                params['company_item_id'] = self.company_item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_spec:
            if hasattr(self.item_spec, 'to_alipay_dict'):
                params['item_spec'] = self.item_spec.to_alipay_dict()
            else:
                params['item_spec'] = self.item_spec
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceItemModifyModel()
        if 'company_item_id' in d:
            o.company_item_id = d['company_item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


