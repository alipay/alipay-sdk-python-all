#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CouponUseProduct import CouponUseProduct


class CouponDetail(object):

    def __init__(self):
        self._activity_code = None
        self._amount = None
        self._coupon_code = None
        self._coupon_desc = None
        self._coupon_title = None
        self._coupon_type = None
        self._coupon_use_products = None
        self._discount = None
        self._end_time = None
        self._purchase_max_num = None
        self._purchase_min_num = None
        self._start_time = None
        self._status = None
        self._use_threshold = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def coupon_code(self):
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, value):
        self._coupon_code = value
    @property
    def coupon_desc(self):
        return self._coupon_desc

    @coupon_desc.setter
    def coupon_desc(self, value):
        self._coupon_desc = value
    @property
    def coupon_title(self):
        return self._coupon_title

    @coupon_title.setter
    def coupon_title(self, value):
        self._coupon_title = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def coupon_use_products(self):
        return self._coupon_use_products

    @coupon_use_products.setter
    def coupon_use_products(self, value):
        if isinstance(value, list):
            self._coupon_use_products = list()
            for i in value:
                if isinstance(i, CouponUseProduct):
                    self._coupon_use_products.append(i)
                else:
                    self._coupon_use_products.append(CouponUseProduct.from_alipay_dict(i))
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def purchase_max_num(self):
        return self._purchase_max_num

    @purchase_max_num.setter
    def purchase_max_num(self, value):
        self._purchase_max_num = value
    @property
    def purchase_min_num(self):
        return self._purchase_min_num

    @purchase_min_num.setter
    def purchase_min_num(self, value):
        self._purchase_min_num = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use_threshold(self):
        return self._use_threshold

    @use_threshold.setter
    def use_threshold(self, value):
        self._use_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.coupon_code:
            if hasattr(self.coupon_code, 'to_alipay_dict'):
                params['coupon_code'] = self.coupon_code.to_alipay_dict()
            else:
                params['coupon_code'] = self.coupon_code
        if self.coupon_desc:
            if hasattr(self.coupon_desc, 'to_alipay_dict'):
                params['coupon_desc'] = self.coupon_desc.to_alipay_dict()
            else:
                params['coupon_desc'] = self.coupon_desc
        if self.coupon_title:
            if hasattr(self.coupon_title, 'to_alipay_dict'):
                params['coupon_title'] = self.coupon_title.to_alipay_dict()
            else:
                params['coupon_title'] = self.coupon_title
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.coupon_use_products:
            if isinstance(self.coupon_use_products, list):
                for i in range(0, len(self.coupon_use_products)):
                    element = self.coupon_use_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupon_use_products[i] = element.to_alipay_dict()
            if hasattr(self.coupon_use_products, 'to_alipay_dict'):
                params['coupon_use_products'] = self.coupon_use_products.to_alipay_dict()
            else:
                params['coupon_use_products'] = self.coupon_use_products
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.purchase_max_num:
            if hasattr(self.purchase_max_num, 'to_alipay_dict'):
                params['purchase_max_num'] = self.purchase_max_num.to_alipay_dict()
            else:
                params['purchase_max_num'] = self.purchase_max_num
        if self.purchase_min_num:
            if hasattr(self.purchase_min_num, 'to_alipay_dict'):
                params['purchase_min_num'] = self.purchase_min_num.to_alipay_dict()
            else:
                params['purchase_min_num'] = self.purchase_min_num
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.use_threshold:
            if hasattr(self.use_threshold, 'to_alipay_dict'):
                params['use_threshold'] = self.use_threshold.to_alipay_dict()
            else:
                params['use_threshold'] = self.use_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponDetail()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'amount' in d:
            o.amount = d['amount']
        if 'coupon_code' in d:
            o.coupon_code = d['coupon_code']
        if 'coupon_desc' in d:
            o.coupon_desc = d['coupon_desc']
        if 'coupon_title' in d:
            o.coupon_title = d['coupon_title']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_use_products' in d:
            o.coupon_use_products = d['coupon_use_products']
        if 'discount' in d:
            o.discount = d['discount']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'purchase_max_num' in d:
            o.purchase_max_num = d['purchase_max_num']
        if 'purchase_min_num' in d:
            o.purchase_min_num = d['purchase_min_num']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'use_threshold' in d:
            o.use_threshold = d['use_threshold']
        return o


