#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalBookInfoSyncModel(object):

    def __init__(self):
        self._book_time = None
        self._open_id = None
        self._out_order_no = None
        self._user_id = None

    @property
    def book_time(self):
        return self._book_time

    @book_time.setter
    def book_time(self, value):
        self._book_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_time:
            if hasattr(self.book_time, 'to_alipay_dict'):
                params['book_time'] = self.book_time.to_alipay_dict()
            else:
                params['book_time'] = self.book_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalBookInfoSyncModel()
        if 'book_time' in d:
            o.book_time = d['book_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


