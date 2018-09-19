#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MicroPayOrderDetail(object):

    def __init__(self):
        self._alipay_order_no = None
        self._alipay_user_id = None
        self._available_amount = None
        self._create_time = None
        self._expire_time = None
        self._freeze_amount = None
        self._memo = None
        self._merchant_order_no = None
        self._modified_time = None
        self._order_status = None
        self._pay_amount = None
        self._pay_confirm = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_confirm(self):
        return self._pay_confirm

    @pay_confirm.setter
    def pay_confirm(self, value):
        self._pay_confirm = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_confirm:
            if hasattr(self.pay_confirm, 'to_alipay_dict'):
                params['pay_confirm'] = self.pay_confirm.to_alipay_dict()
            else:
                params['pay_confirm'] = self.pay_confirm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MicroPayOrderDetail()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_confirm' in d:
            o.pay_confirm = d['pay_confirm']
        return o


