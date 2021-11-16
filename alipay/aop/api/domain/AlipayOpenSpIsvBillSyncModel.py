#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpIsvBillSyncModel(object):

    def __init__(self):
        self._end_time = None
        self._generate_time = None
        self._item_code = None
        self._out_biz_no = None
        self._pay_time = None
        self._price = None
        self._promotor_pid = None
        self._start_time = None
        self._status = None
        self._sub_promotor_pid = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def generate_time(self):
        return self._generate_time

    @generate_time.setter
    def generate_time(self, value):
        self._generate_time = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def promotor_pid(self):
        return self._promotor_pid

    @promotor_pid.setter
    def promotor_pid(self, value):
        self._promotor_pid = value
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
    def sub_promotor_pid(self):
        return self._sub_promotor_pid

    @sub_promotor_pid.setter
    def sub_promotor_pid(self, value):
        self._sub_promotor_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.generate_time:
            if hasattr(self.generate_time, 'to_alipay_dict'):
                params['generate_time'] = self.generate_time.to_alipay_dict()
            else:
                params['generate_time'] = self.generate_time
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.promotor_pid:
            if hasattr(self.promotor_pid, 'to_alipay_dict'):
                params['promotor_pid'] = self.promotor_pid.to_alipay_dict()
            else:
                params['promotor_pid'] = self.promotor_pid
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
        if self.sub_promotor_pid:
            if hasattr(self.sub_promotor_pid, 'to_alipay_dict'):
                params['sub_promotor_pid'] = self.sub_promotor_pid.to_alipay_dict()
            else:
                params['sub_promotor_pid'] = self.sub_promotor_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpIsvBillSyncModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'generate_time' in d:
            o.generate_time = d['generate_time']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'price' in d:
            o.price = d['price']
        if 'promotor_pid' in d:
            o.promotor_pid = d['promotor_pid']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_promotor_pid' in d:
            o.sub_promotor_pid = d['sub_promotor_pid']
        return o


