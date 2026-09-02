#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclinginvoiceOrderCreateItem import RecyclinginvoiceOrderCreateItem


class AlipayCommerceEcRecyclinginvoiceOrderCreateModel(object):

    def __init__(self):
        self._company_clerk_id = None
        self._company_supplier_id = None
        self._invoice_kind = None
        self._memo = None
        self._order_item_list = None
        self._outer_order_id = None
        self._personal_tax_project = None
        self._product_id = None
        self._product_origin_code = None
        self._proxy_seller_cert_no = None
        self._received_method = None
        self._tax_no = None
        self._tax_rate = None

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
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
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
    def product_origin_code(self):
        return self._product_origin_code

    @product_origin_code.setter
    def product_origin_code(self, value):
        self._product_origin_code = value
    @property
    def proxy_seller_cert_no(self):
        return self._proxy_seller_cert_no

    @proxy_seller_cert_no.setter
    def proxy_seller_cert_no(self, value):
        self._proxy_seller_cert_no = value
    @property
    def received_method(self):
        return self._received_method

    @received_method.setter
    def received_method(self, value):
        self._received_method = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


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
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
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
        if self.product_origin_code:
            if hasattr(self.product_origin_code, 'to_alipay_dict'):
                params['product_origin_code'] = self.product_origin_code.to_alipay_dict()
            else:
                params['product_origin_code'] = self.product_origin_code
        if self.proxy_seller_cert_no:
            if hasattr(self.proxy_seller_cert_no, 'to_alipay_dict'):
                params['proxy_seller_cert_no'] = self.proxy_seller_cert_no.to_alipay_dict()
            else:
                params['proxy_seller_cert_no'] = self.proxy_seller_cert_no
        if self.received_method:
            if hasattr(self.received_method, 'to_alipay_dict'):
                params['received_method'] = self.received_method.to_alipay_dict()
            else:
                params['received_method'] = self.received_method
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
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
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
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
        if 'product_origin_code' in d:
            o.product_origin_code = d['product_origin_code']
        if 'proxy_seller_cert_no' in d:
            o.proxy_seller_cert_no = d['proxy_seller_cert_no']
        if 'received_method' in d:
            o.received_method = d['received_method']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


