#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SinglePayDetail(object):

    def __init__(self):
        self._alipay_order_no = None
        self._amount = None
        self._create_time = None
        self._modified_time = None
        self._pay_url = None
        self._receive_user_id = None
        self._transfer_order_no = None
        self._transfer_out_order_no = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def receive_user_id(self):
        return self._receive_user_id

    @receive_user_id.setter
    def receive_user_id(self, value):
        self._receive_user_id = value
    @property
    def transfer_order_no(self):
        return self._transfer_order_no

    @transfer_order_no.setter
    def transfer_order_no(self, value):
        self._transfer_order_no = value
    @property
    def transfer_out_order_no(self):
        return self._transfer_out_order_no

    @transfer_out_order_no.setter
    def transfer_out_order_no(self, value):
        self._transfer_out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.pay_url:
            if hasattr(self.pay_url, 'to_alipay_dict'):
                params['pay_url'] = self.pay_url.to_alipay_dict()
            else:
                params['pay_url'] = self.pay_url
        if self.receive_user_id:
            if hasattr(self.receive_user_id, 'to_alipay_dict'):
                params['receive_user_id'] = self.receive_user_id.to_alipay_dict()
            else:
                params['receive_user_id'] = self.receive_user_id
        if self.transfer_order_no:
            if hasattr(self.transfer_order_no, 'to_alipay_dict'):
                params['transfer_order_no'] = self.transfer_order_no.to_alipay_dict()
            else:
                params['transfer_order_no'] = self.transfer_order_no
        if self.transfer_out_order_no:
            if hasattr(self.transfer_out_order_no, 'to_alipay_dict'):
                params['transfer_out_order_no'] = self.transfer_out_order_no.to_alipay_dict()
            else:
                params['transfer_out_order_no'] = self.transfer_out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SinglePayDetail()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'pay_url' in d:
            o.pay_url = d['pay_url']
        if 'receive_user_id' in d:
            o.receive_user_id = d['receive_user_id']
        if 'transfer_order_no' in d:
            o.transfer_order_no = d['transfer_order_no']
        if 'transfer_out_order_no' in d:
            o.transfer_out_order_no = d['transfer_out_order_no']
        return o


