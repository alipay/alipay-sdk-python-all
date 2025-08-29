#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaoInvoiceDetail(object):

    def __init__(self):
        self._acceptance_count = None
        self._acceptance_date = None
        self._acceptance_status = None
        self._commodity_code = None
        self._commodity_count = None
        self._commodity_name = None
        self._first_year_warranty_end_date = None
        self._first_year_warranty_start_date = None
        self._invoice_no = None
        self._name = None
        self._node_count = None
        self._price = None
        self._product_category = None
        self._product_name = None
        self._selling_unit = None
        self._sku_name = None
        self._sku_no = None
        self._tax_rate = None
        self._years_count = None

    @property
    def acceptance_count(self):
        return self._acceptance_count

    @acceptance_count.setter
    def acceptance_count(self, value):
        self._acceptance_count = value
    @property
    def acceptance_date(self):
        return self._acceptance_date

    @acceptance_date.setter
    def acceptance_date(self, value):
        self._acceptance_date = value
    @property
    def acceptance_status(self):
        return self._acceptance_status

    @acceptance_status.setter
    def acceptance_status(self, value):
        self._acceptance_status = value
    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def commodity_count(self):
        return self._commodity_count

    @commodity_count.setter
    def commodity_count(self, value):
        self._commodity_count = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def first_year_warranty_end_date(self):
        return self._first_year_warranty_end_date

    @first_year_warranty_end_date.setter
    def first_year_warranty_end_date(self, value):
        self._first_year_warranty_end_date = value
    @property
    def first_year_warranty_start_date(self):
        return self._first_year_warranty_start_date

    @first_year_warranty_start_date.setter
    def first_year_warranty_start_date(self, value):
        self._first_year_warranty_start_date = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_count(self):
        return self._node_count

    @node_count.setter
    def node_count(self, value):
        self._node_count = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self, value):
        self._product_category = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def selling_unit(self):
        return self._selling_unit

    @selling_unit.setter
    def selling_unit(self, value):
        self._selling_unit = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def years_count(self):
        return self._years_count

    @years_count.setter
    def years_count(self, value):
        self._years_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_count:
            if hasattr(self.acceptance_count, 'to_alipay_dict'):
                params['acceptance_count'] = self.acceptance_count.to_alipay_dict()
            else:
                params['acceptance_count'] = self.acceptance_count
        if self.acceptance_date:
            if hasattr(self.acceptance_date, 'to_alipay_dict'):
                params['acceptance_date'] = self.acceptance_date.to_alipay_dict()
            else:
                params['acceptance_date'] = self.acceptance_date
        if self.acceptance_status:
            if hasattr(self.acceptance_status, 'to_alipay_dict'):
                params['acceptance_status'] = self.acceptance_status.to_alipay_dict()
            else:
                params['acceptance_status'] = self.acceptance_status
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.commodity_count:
            if hasattr(self.commodity_count, 'to_alipay_dict'):
                params['commodity_count'] = self.commodity_count.to_alipay_dict()
            else:
                params['commodity_count'] = self.commodity_count
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.first_year_warranty_end_date:
            if hasattr(self.first_year_warranty_end_date, 'to_alipay_dict'):
                params['first_year_warranty_end_date'] = self.first_year_warranty_end_date.to_alipay_dict()
            else:
                params['first_year_warranty_end_date'] = self.first_year_warranty_end_date
        if self.first_year_warranty_start_date:
            if hasattr(self.first_year_warranty_start_date, 'to_alipay_dict'):
                params['first_year_warranty_start_date'] = self.first_year_warranty_start_date.to_alipay_dict()
            else:
                params['first_year_warranty_start_date'] = self.first_year_warranty_start_date
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_count:
            if hasattr(self.node_count, 'to_alipay_dict'):
                params['node_count'] = self.node_count.to_alipay_dict()
            else:
                params['node_count'] = self.node_count
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_category:
            if hasattr(self.product_category, 'to_alipay_dict'):
                params['product_category'] = self.product_category.to_alipay_dict()
            else:
                params['product_category'] = self.product_category
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.selling_unit:
            if hasattr(self.selling_unit, 'to_alipay_dict'):
                params['selling_unit'] = self.selling_unit.to_alipay_dict()
            else:
                params['selling_unit'] = self.selling_unit
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.years_count:
            if hasattr(self.years_count, 'to_alipay_dict'):
                params['years_count'] = self.years_count.to_alipay_dict()
            else:
                params['years_count'] = self.years_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaoInvoiceDetail()
        if 'acceptance_count' in d:
            o.acceptance_count = d['acceptance_count']
        if 'acceptance_date' in d:
            o.acceptance_date = d['acceptance_date']
        if 'acceptance_status' in d:
            o.acceptance_status = d['acceptance_status']
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'commodity_count' in d:
            o.commodity_count = d['commodity_count']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'first_year_warranty_end_date' in d:
            o.first_year_warranty_end_date = d['first_year_warranty_end_date']
        if 'first_year_warranty_start_date' in d:
            o.first_year_warranty_start_date = d['first_year_warranty_start_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'name' in d:
            o.name = d['name']
        if 'node_count' in d:
            o.node_count = d['node_count']
        if 'price' in d:
            o.price = d['price']
        if 'product_category' in d:
            o.product_category = d['product_category']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'selling_unit' in d:
            o.selling_unit = d['selling_unit']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'years_count' in d:
            o.years_count = d['years_count']
        return o


