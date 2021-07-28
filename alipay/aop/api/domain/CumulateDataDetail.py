#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CumulateDataDetail(object):

    def __init__(self):
        self._action_type = None
        self._biz_time = None
        self._data_type = None
        self._discount_amount = None
        self._discount_desc = None
        self._out_biz_no = None
        self._refer_out_biz_no = None
        self._sub_data_type = None
        self._task_amount = None
        self._task_desc = None
        self._task_times = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def refer_out_biz_no(self):
        return self._refer_out_biz_no

    @refer_out_biz_no.setter
    def refer_out_biz_no(self, value):
        self._refer_out_biz_no = value
    @property
    def sub_data_type(self):
        return self._sub_data_type

    @sub_data_type.setter
    def sub_data_type(self, value):
        self._sub_data_type = value
    @property
    def task_amount(self):
        return self._task_amount

    @task_amount.setter
    def task_amount(self, value):
        self._task_amount = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_times(self):
        return self._task_times

    @task_times.setter
    def task_times(self, value):
        self._task_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.refer_out_biz_no:
            if hasattr(self.refer_out_biz_no, 'to_alipay_dict'):
                params['refer_out_biz_no'] = self.refer_out_biz_no.to_alipay_dict()
            else:
                params['refer_out_biz_no'] = self.refer_out_biz_no
        if self.sub_data_type:
            if hasattr(self.sub_data_type, 'to_alipay_dict'):
                params['sub_data_type'] = self.sub_data_type.to_alipay_dict()
            else:
                params['sub_data_type'] = self.sub_data_type
        if self.task_amount:
            if hasattr(self.task_amount, 'to_alipay_dict'):
                params['task_amount'] = self.task_amount.to_alipay_dict()
            else:
                params['task_amount'] = self.task_amount
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_times:
            if hasattr(self.task_times, 'to_alipay_dict'):
                params['task_times'] = self.task_times.to_alipay_dict()
            else:
                params['task_times'] = self.task_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CumulateDataDetail()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'refer_out_biz_no' in d:
            o.refer_out_biz_no = d['refer_out_biz_no']
        if 'sub_data_type' in d:
            o.sub_data_type = d['sub_data_type']
        if 'task_amount' in d:
            o.task_amount = d['task_amount']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_times' in d:
            o.task_times = d['task_times']
        return o


