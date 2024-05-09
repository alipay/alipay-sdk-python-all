#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarOrdermodifyApplyModel(object):

    def __init__(self):
        self._modified_end_time = None
        self._modified_start_time = None
        self._open_id = None
        self._parent_out_order_no = None
        self._total_amount = None
        self._user_id = None

    @property
    def modified_end_time(self):
        return self._modified_end_time

    @modified_end_time.setter
    def modified_end_time(self, value):
        self._modified_end_time = value
    @property
    def modified_start_time(self):
        return self._modified_start_time

    @modified_start_time.setter
    def modified_start_time(self, value):
        self._modified_start_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def parent_out_order_no(self):
        return self._parent_out_order_no

    @parent_out_order_no.setter
    def parent_out_order_no(self, value):
        self._parent_out_order_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.modified_end_time:
            if hasattr(self.modified_end_time, 'to_alipay_dict'):
                params['modified_end_time'] = self.modified_end_time.to_alipay_dict()
            else:
                params['modified_end_time'] = self.modified_end_time
        if self.modified_start_time:
            if hasattr(self.modified_start_time, 'to_alipay_dict'):
                params['modified_start_time'] = self.modified_start_time.to_alipay_dict()
            else:
                params['modified_start_time'] = self.modified_start_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.parent_out_order_no:
            if hasattr(self.parent_out_order_no, 'to_alipay_dict'):
                params['parent_out_order_no'] = self.parent_out_order_no.to_alipay_dict()
            else:
                params['parent_out_order_no'] = self.parent_out_order_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = AlipayEcoMycarRentcarOrdermodifyApplyModel()
        if 'modified_end_time' in d:
            o.modified_end_time = d['modified_end_time']
        if 'modified_start_time' in d:
            o.modified_start_time = d['modified_start_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'parent_out_order_no' in d:
            o.parent_out_order_no = d['parent_out_order_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


