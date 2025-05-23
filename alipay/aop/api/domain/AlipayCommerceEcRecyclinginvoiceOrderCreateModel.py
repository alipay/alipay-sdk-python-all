#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclinginvoiceOrderCreateItem import RecyclinginvoiceOrderCreateItem


class AlipayCommerceEcRecyclinginvoiceOrderCreateModel(object):

    def __init__(self):
        self._company_clerk_id = None
        self._company_supplier_id = None
        self._memo = None
        self._order_item_list = None
        self._outer_order_id = None
        self._personal_tax_project = None
        self._product_id = None
        self._tax_no = None

    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def company_supplier_id(self):
        return self._company_supplier_id

    @company_supplier_id.setter
    def company_supplier_id(self, value):
        self._company_supplier_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, value):
        if isinstance(value, list):
            self._order_item_list = list()
            for i in value:
                if isinstance(i, RecyclinginvoiceOrderCreateItem):
                    self._order_item_list.append(i)
                else:
                    self._order_item_list.append(RecyclinginvoiceOrderCreateItem.from_alipay_dict(i))
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def personal_tax_project(self):
        return self._personal_tax_project

    @personal_tax_project.setter
    def personal_tax_project(self, value):
        self._personal_tax_project = value
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
        if self.company_clerk_id:
            if hasattr(self.company_clerk_id, 'to_alipay_dict'):
                params['company_clerk_id'] = self.company_clerk_id.to_alipay_dict()
            else:
                params['company_clerk_id'] = self.company_clerk_id
        if self.company_supplier_id:
            if hasattr(self.company_supplier_id, 'to_alipay_dict'):
                params['company_supplier_id'] = self.company_supplier_id.to_alipay_dict()
            else:
                params['company_supplier_id'] = self.company_supplier_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_item_list:
            if isinstance(self.order_item_list, list):
                for i in range(0, len(self.order_item_list)):
                    element = self.order_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_item_list[i] = element.to_alipay_dict()
            if hasattr(self.order_item_list, 'to_alipay_dict'):
                params['order_item_list'] = self.order_item_list.to_alipay_dict()
            else:
                params['order_item_list'] = self.order_item_list
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.personal_tax_project:
            if hasattr(self.personal_tax_project, 'to_alipay_dict'):
                params['personal_tax_project'] = self.personal_tax_project.to_alipay_dict()
            else:
                params['personal_tax_project'] = self.personal_tax_project
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
        o = AlipayCommerceEcRecyclinginvoiceOrderCreateModel()
        if 'company_clerk_id' in d:
            o.company_clerk_id = d['company_clerk_id']
        if 'company_supplier_id' in d:
            o.company_supplier_id = d['company_supplier_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_item_list' in d:
            o.order_item_list = d['order_item_list']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'personal_tax_project' in d:
            o.personal_tax_project = d['personal_tax_project']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


