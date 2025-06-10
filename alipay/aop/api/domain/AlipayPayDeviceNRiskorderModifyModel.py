#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayDeviceNRiskorderModifyModel(object):

    def __init__(self):
        self._completion_days = None
        self._handler_id = None
        self._handler_name = None
        self._notes = None
        self._order_no = None
        self._out_order_no = None
        self._process_time = None
        self._solution_code = None

    @property
    def completion_days(self):
        return self._completion_days

    @completion_days.setter
    def completion_days(self, value):
        self._completion_days = value
    @property
    def handler_id(self):
        return self._handler_id

    @handler_id.setter
    def handler_id(self, value):
        self._handler_id = value
    @property
    def handler_name(self):
        return self._handler_name

    @handler_name.setter
    def handler_name(self, value):
        self._handler_name = value
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.completion_days:
            if hasattr(self.completion_days, 'to_alipay_dict'):
                params['completion_days'] = self.completion_days.to_alipay_dict()
            else:
                params['completion_days'] = self.completion_days
        if self.handler_id:
            if hasattr(self.handler_id, 'to_alipay_dict'):
                params['handler_id'] = self.handler_id.to_alipay_dict()
            else:
                params['handler_id'] = self.handler_id
        if self.handler_name:
            if hasattr(self.handler_name, 'to_alipay_dict'):
                params['handler_name'] = self.handler_name.to_alipay_dict()
            else:
                params['handler_name'] = self.handler_name
        if self.notes:
            if hasattr(self.notes, 'to_alipay_dict'):
                params['notes'] = self.notes.to_alipay_dict()
            else:
                params['notes'] = self.notes
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.process_time:
            if hasattr(self.process_time, 'to_alipay_dict'):
                params['process_time'] = self.process_time.to_alipay_dict()
            else:
                params['process_time'] = self.process_time
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayDeviceNRiskorderModifyModel()
        if 'completion_days' in d:
            o.completion_days = d['completion_days']
        if 'handler_id' in d:
            o.handler_id = d['handler_id']
        if 'handler_name' in d:
            o.handler_name = d['handler_name']
        if 'notes' in d:
            o.notes = d['notes']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'process_time' in d:
            o.process_time = d['process_time']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


