#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcOrderLineResult(object):

    def __init__(self):
        self._logistics_status = None
        self._number = None
        self._order_id = None
        self._order_line_id = None
        self._order_line_status = None
        self._pay_fee = None
        self._product_id = None
        self._product_pic = None
        self._product_title = None
        self._sku_id = None
        self._sku_title = None

    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_line_id(self):
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, value):
        self._order_line_id = value
    @property
    def order_line_status(self):
        return self._order_line_status

    @order_line_status.setter
    def order_line_status(self, value):
        self._order_line_status = value
    @property
    def pay_fee(self):
        return self._pay_fee

    @pay_fee.setter
    def pay_fee(self, value):
        self._pay_fee = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_pic(self):
        return self._product_pic

    @product_pic.setter
    def product_pic(self, value):
        self._product_pic = value
    @property
    def product_title(self):
        return self._product_title

    @product_title.setter
    def product_title(self, value):
        self._product_title = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_title(self):
        return self._sku_title

    @sku_title.setter
    def sku_title(self, value):
        self._sku_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_line_id:
            if hasattr(self.order_line_id, 'to_alipay_dict'):
                params['order_line_id'] = self.order_line_id.to_alipay_dict()
            else:
                params['order_line_id'] = self.order_line_id
        if self.order_line_status:
            if hasattr(self.order_line_status, 'to_alipay_dict'):
                params['order_line_status'] = self.order_line_status.to_alipay_dict()
            else:
                params['order_line_status'] = self.order_line_status
        if self.pay_fee:
            if hasattr(self.pay_fee, 'to_alipay_dict'):
                params['pay_fee'] = self.pay_fee.to_alipay_dict()
            else:
                params['pay_fee'] = self.pay_fee
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_pic:
            if hasattr(self.product_pic, 'to_alipay_dict'):
                params['product_pic'] = self.product_pic.to_alipay_dict()
            else:
                params['product_pic'] = self.product_pic
        if self.product_title:
            if hasattr(self.product_title, 'to_alipay_dict'):
                params['product_title'] = self.product_title.to_alipay_dict()
            else:
                params['product_title'] = self.product_title
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_title:
            if hasattr(self.sku_title, 'to_alipay_dict'):
                params['sku_title'] = self.sku_title.to_alipay_dict()
            else:
                params['sku_title'] = self.sku_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcOrderLineResult()
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'number' in d:
            o.number = d['number']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_line_id' in d:
            o.order_line_id = d['order_line_id']
        if 'order_line_status' in d:
            o.order_line_status = d['order_line_status']
        if 'pay_fee' in d:
            o.pay_fee = d['pay_fee']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_pic' in d:
            o.product_pic = d['product_pic']
        if 'product_title' in d:
            o.product_title = d['product_title']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_title' in d:
            o.sku_title = d['sku_title']
        return o


