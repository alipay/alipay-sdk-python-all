#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookOrderVO(object):

    def __init__(self):
        self._create_time = None
        self._out_order_no = None
        self._status = None
        self._store_code = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookOrderVO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'status' in d:
            o.status = d['status']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


