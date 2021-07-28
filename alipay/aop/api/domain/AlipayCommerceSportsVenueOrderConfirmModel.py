#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductGroup import ProductGroup


class AlipayCommerceSportsVenueOrderConfirmModel(object):

    def __init__(self):
        self._confirm_desc = None
        self._confirm_status = None
        self._order_id = None
        self._out_order_id = None
        self._product_group_list = None
        self._total_amount = None

    @property
    def confirm_desc(self):
        return self._confirm_desc

    @confirm_desc.setter
    def confirm_desc(self, value):
        self._confirm_desc = value
    @property
    def confirm_status(self):
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, value):
        self._confirm_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def product_group_list(self):
        return self._product_group_list

    @product_group_list.setter
    def product_group_list(self, value):
        if isinstance(value, list):
            self._product_group_list = list()
            for i in value:
                if isinstance(i, ProductGroup):
                    self._product_group_list.append(i)
                else:
                    self._product_group_list.append(ProductGroup.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_desc:
            if hasattr(self.confirm_desc, 'to_alipay_dict'):
                params['confirm_desc'] = self.confirm_desc.to_alipay_dict()
            else:
                params['confirm_desc'] = self.confirm_desc
        if self.confirm_status:
            if hasattr(self.confirm_status, 'to_alipay_dict'):
                params['confirm_status'] = self.confirm_status.to_alipay_dict()
            else:
                params['confirm_status'] = self.confirm_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.product_group_list:
            if isinstance(self.product_group_list, list):
                for i in range(0, len(self.product_group_list)):
                    element = self.product_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_group_list[i] = element.to_alipay_dict()
            if hasattr(self.product_group_list, 'to_alipay_dict'):
                params['product_group_list'] = self.product_group_list.to_alipay_dict()
            else:
                params['product_group_list'] = self.product_group_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVenueOrderConfirmModel()
        if 'confirm_desc' in d:
            o.confirm_desc = d['confirm_desc']
        if 'confirm_status' in d:
            o.confirm_status = d['confirm_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'product_group_list' in d:
            o.product_group_list = d['product_group_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


