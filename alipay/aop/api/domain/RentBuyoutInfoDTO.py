#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentBuyoutInfoDTO(object):

    def __init__(self):
        self._buyout_installment_no = None
        self._origin_order_id = None
        self._pay_notify_url = None
        self._sync_pay = None

    @property
    def buyout_installment_no(self):
        return self._buyout_installment_no

    @buyout_installment_no.setter
    def buyout_installment_no(self, value):
        self._buyout_installment_no = value
    @property
    def origin_order_id(self):
        return self._origin_order_id

    @origin_order_id.setter
    def origin_order_id(self, value):
        self._origin_order_id = value
    @property
    def pay_notify_url(self):
        return self._pay_notify_url

    @pay_notify_url.setter
    def pay_notify_url(self, value):
        self._pay_notify_url = value
    @property
    def sync_pay(self):
        return self._sync_pay

    @sync_pay.setter
    def sync_pay(self, value):
        self._sync_pay = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyout_installment_no:
            if hasattr(self.buyout_installment_no, 'to_alipay_dict'):
                params['buyout_installment_no'] = self.buyout_installment_no.to_alipay_dict()
            else:
                params['buyout_installment_no'] = self.buyout_installment_no
        if self.origin_order_id:
            if hasattr(self.origin_order_id, 'to_alipay_dict'):
                params['origin_order_id'] = self.origin_order_id.to_alipay_dict()
            else:
                params['origin_order_id'] = self.origin_order_id
        if self.pay_notify_url:
            if hasattr(self.pay_notify_url, 'to_alipay_dict'):
                params['pay_notify_url'] = self.pay_notify_url.to_alipay_dict()
            else:
                params['pay_notify_url'] = self.pay_notify_url
        if self.sync_pay:
            if hasattr(self.sync_pay, 'to_alipay_dict'):
                params['sync_pay'] = self.sync_pay.to_alipay_dict()
            else:
                params['sync_pay'] = self.sync_pay
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentBuyoutInfoDTO()
        if 'buyout_installment_no' in d:
            o.buyout_installment_no = d['buyout_installment_no']
        if 'origin_order_id' in d:
            o.origin_order_id = d['origin_order_id']
        if 'pay_notify_url' in d:
            o.pay_notify_url = d['pay_notify_url']
        if 'sync_pay' in d:
            o.sync_pay = d['sync_pay']
        return o


