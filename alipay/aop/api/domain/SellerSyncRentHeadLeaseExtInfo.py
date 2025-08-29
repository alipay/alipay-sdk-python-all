#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellerSyncRentHeadLeaseExtInfo(object):

    def __init__(self):
        self._head_lease_after_coupon_price = None
        self._head_lease_buyout_price = None
        self._head_lease_max_overdue_count = None
        self._head_lease_max_overdue_days = None
        self._head_lease_order_id = None
        self._head_lease_pre_coupon_price = None

    @property
    def head_lease_after_coupon_price(self):
        return self._head_lease_after_coupon_price

    @head_lease_after_coupon_price.setter
    def head_lease_after_coupon_price(self, value):
        self._head_lease_after_coupon_price = value
    @property
    def head_lease_buyout_price(self):
        return self._head_lease_buyout_price

    @head_lease_buyout_price.setter
    def head_lease_buyout_price(self, value):
        self._head_lease_buyout_price = value
    @property
    def head_lease_max_overdue_count(self):
        return self._head_lease_max_overdue_count

    @head_lease_max_overdue_count.setter
    def head_lease_max_overdue_count(self, value):
        self._head_lease_max_overdue_count = value
    @property
    def head_lease_max_overdue_days(self):
        return self._head_lease_max_overdue_days

    @head_lease_max_overdue_days.setter
    def head_lease_max_overdue_days(self, value):
        self._head_lease_max_overdue_days = value
    @property
    def head_lease_order_id(self):
        return self._head_lease_order_id

    @head_lease_order_id.setter
    def head_lease_order_id(self, value):
        self._head_lease_order_id = value
    @property
    def head_lease_pre_coupon_price(self):
        return self._head_lease_pre_coupon_price

    @head_lease_pre_coupon_price.setter
    def head_lease_pre_coupon_price(self, value):
        self._head_lease_pre_coupon_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.head_lease_after_coupon_price:
            if hasattr(self.head_lease_after_coupon_price, 'to_alipay_dict'):
                params['head_lease_after_coupon_price'] = self.head_lease_after_coupon_price.to_alipay_dict()
            else:
                params['head_lease_after_coupon_price'] = self.head_lease_after_coupon_price
        if self.head_lease_buyout_price:
            if hasattr(self.head_lease_buyout_price, 'to_alipay_dict'):
                params['head_lease_buyout_price'] = self.head_lease_buyout_price.to_alipay_dict()
            else:
                params['head_lease_buyout_price'] = self.head_lease_buyout_price
        if self.head_lease_max_overdue_count:
            if hasattr(self.head_lease_max_overdue_count, 'to_alipay_dict'):
                params['head_lease_max_overdue_count'] = self.head_lease_max_overdue_count.to_alipay_dict()
            else:
                params['head_lease_max_overdue_count'] = self.head_lease_max_overdue_count
        if self.head_lease_max_overdue_days:
            if hasattr(self.head_lease_max_overdue_days, 'to_alipay_dict'):
                params['head_lease_max_overdue_days'] = self.head_lease_max_overdue_days.to_alipay_dict()
            else:
                params['head_lease_max_overdue_days'] = self.head_lease_max_overdue_days
        if self.head_lease_order_id:
            if hasattr(self.head_lease_order_id, 'to_alipay_dict'):
                params['head_lease_order_id'] = self.head_lease_order_id.to_alipay_dict()
            else:
                params['head_lease_order_id'] = self.head_lease_order_id
        if self.head_lease_pre_coupon_price:
            if hasattr(self.head_lease_pre_coupon_price, 'to_alipay_dict'):
                params['head_lease_pre_coupon_price'] = self.head_lease_pre_coupon_price.to_alipay_dict()
            else:
                params['head_lease_pre_coupon_price'] = self.head_lease_pre_coupon_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellerSyncRentHeadLeaseExtInfo()
        if 'head_lease_after_coupon_price' in d:
            o.head_lease_after_coupon_price = d['head_lease_after_coupon_price']
        if 'head_lease_buyout_price' in d:
            o.head_lease_buyout_price = d['head_lease_buyout_price']
        if 'head_lease_max_overdue_count' in d:
            o.head_lease_max_overdue_count = d['head_lease_max_overdue_count']
        if 'head_lease_max_overdue_days' in d:
            o.head_lease_max_overdue_days = d['head_lease_max_overdue_days']
        if 'head_lease_order_id' in d:
            o.head_lease_order_id = d['head_lease_order_id']
        if 'head_lease_pre_coupon_price' in d:
            o.head_lease_pre_coupon_price = d['head_lease_pre_coupon_price']
        return o


