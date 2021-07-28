#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueueInfo(object):

    def __init__(self):
        self._current_num = None
        self._dining_num = None
        self._queue_num = None
        self._still_wait_time = None
        self._table_type = None
        self._wait_num = None
        self._waiting_time = None

    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
    @property
    def dining_num(self):
        return self._dining_num

    @dining_num.setter
    def dining_num(self, value):
        self._dining_num = value
    @property
    def queue_num(self):
        return self._queue_num

    @queue_num.setter
    def queue_num(self, value):
        self._queue_num = value
    @property
    def still_wait_time(self):
        return self._still_wait_time

    @still_wait_time.setter
    def still_wait_time(self, value):
        self._still_wait_time = value
    @property
    def table_type(self):
        return self._table_type

    @table_type.setter
    def table_type(self, value):
        self._table_type = value
    @property
    def wait_num(self):
        return self._wait_num

    @wait_num.setter
    def wait_num(self, value):
        self._wait_num = value
    @property
    def waiting_time(self):
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, value):
        self._waiting_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
        if self.dining_num:
            if hasattr(self.dining_num, 'to_alipay_dict'):
                params['dining_num'] = self.dining_num.to_alipay_dict()
            else:
                params['dining_num'] = self.dining_num
        if self.queue_num:
            if hasattr(self.queue_num, 'to_alipay_dict'):
                params['queue_num'] = self.queue_num.to_alipay_dict()
            else:
                params['queue_num'] = self.queue_num
        if self.still_wait_time:
            if hasattr(self.still_wait_time, 'to_alipay_dict'):
                params['still_wait_time'] = self.still_wait_time.to_alipay_dict()
            else:
                params['still_wait_time'] = self.still_wait_time
        if self.table_type:
            if hasattr(self.table_type, 'to_alipay_dict'):
                params['table_type'] = self.table_type.to_alipay_dict()
            else:
                params['table_type'] = self.table_type
        if self.wait_num:
            if hasattr(self.wait_num, 'to_alipay_dict'):
                params['wait_num'] = self.wait_num.to_alipay_dict()
            else:
                params['wait_num'] = self.wait_num
        if self.waiting_time:
            if hasattr(self.waiting_time, 'to_alipay_dict'):
                params['waiting_time'] = self.waiting_time.to_alipay_dict()
            else:
                params['waiting_time'] = self.waiting_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueueInfo()
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'dining_num' in d:
            o.dining_num = d['dining_num']
        if 'queue_num' in d:
            o.queue_num = d['queue_num']
        if 'still_wait_time' in d:
            o.still_wait_time = d['still_wait_time']
        if 'table_type' in d:
            o.table_type = d['table_type']
        if 'wait_num' in d:
            o.wait_num = d['wait_num']
        if 'waiting_time' in d:
            o.waiting_time = d['waiting_time']
        return o


