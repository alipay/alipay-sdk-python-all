#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthDiscountInfo import HealthDiscountInfo


class OrderBizInfo(object):

    def __init__(self):
        self._amount_discount = None
        self._amount_original = None
        self._discount_info = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_no = None
        self._order_status = None
        self._pay_expire_time = None

    @property
    def amount_discount(self):
        return self._amount_discount

    @amount_discount.setter
    def amount_discount(self, value):
        self._amount_discount = value
    @property
    def amount_original(self):
        return self._amount_original

    @amount_original.setter
    def amount_original(self, value):
        self._amount_original = value
    @property
    def discount_info(self):
        return self._discount_info

    @discount_info.setter
    def discount_info(self, value):
        if isinstance(value, list):
            self._discount_info = list()
            for i in value:
                if isinstance(i, HealthDiscountInfo):
                    self._discount_info.append(i)
                else:
                    self._discount_info.append(HealthDiscountInfo.from_alipay_dict(i))
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_expire_time(self):
        return self._pay_expire_time

    @pay_expire_time.setter
    def pay_expire_time(self, value):
        self._pay_expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_discount:
            if hasattr(self.amount_discount, 'to_alipay_dict'):
                params['amount_discount'] = self.amount_discount.to_alipay_dict()
            else:
                params['amount_discount'] = self.amount_discount
        if self.amount_original:
            if hasattr(self.amount_original, 'to_alipay_dict'):
                params['amount_original'] = self.amount_original.to_alipay_dict()
            else:
                params['amount_original'] = self.amount_original
        if self.discount_info:
            if isinstance(self.discount_info, list):
                for i in range(0, len(self.discount_info)):
                    element = self.discount_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_info[i] = element.to_alipay_dict()
            if hasattr(self.discount_info, 'to_alipay_dict'):
                params['discount_info'] = self.discount_info.to_alipay_dict()
            else:
                params['discount_info'] = self.discount_info
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_expire_time:
            if hasattr(self.pay_expire_time, 'to_alipay_dict'):
                params['pay_expire_time'] = self.pay_expire_time.to_alipay_dict()
            else:
                params['pay_expire_time'] = self.pay_expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBizInfo()
        if 'amount_discount' in d:
            o.amount_discount = d['amount_discount']
        if 'amount_original' in d:
            o.amount_original = d['amount_original']
        if 'discount_info' in d:
            o.discount_info = d['discount_info']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_expire_time' in d:
            o.pay_expire_time = d['pay_expire_time']
        return o


