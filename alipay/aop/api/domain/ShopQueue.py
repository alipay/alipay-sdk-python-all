#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopQueue(object):

    def __init__(self):
        self._max_queue_num = None
        self._min_queue_num = None
        self._queue_desc = None
        self._queue_id = None
        self._queue_name = None
        self._queue_option = None
        self._queue_prefix = None

    @property
    def max_queue_num(self):
        return self._max_queue_num

    @max_queue_num.setter
    def max_queue_num(self, value):
        self._max_queue_num = value
    @property
    def min_queue_num(self):
        return self._min_queue_num

    @min_queue_num.setter
    def min_queue_num(self, value):
        self._min_queue_num = value
    @property
    def queue_desc(self):
        return self._queue_desc

    @queue_desc.setter
    def queue_desc(self, value):
        self._queue_desc = value
    @property
    def queue_id(self):
        return self._queue_id

    @queue_id.setter
    def queue_id(self, value):
        self._queue_id = value
    @property
    def queue_name(self):
        return self._queue_name

    @queue_name.setter
    def queue_name(self, value):
        self._queue_name = value
    @property
    def queue_option(self):
        return self._queue_option

    @queue_option.setter
    def queue_option(self, value):
        self._queue_option = value
    @property
    def queue_prefix(self):
        return self._queue_prefix

    @queue_prefix.setter
    def queue_prefix(self, value):
        self._queue_prefix = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_queue_num:
            if hasattr(self.max_queue_num, 'to_alipay_dict'):
                params['max_queue_num'] = self.max_queue_num.to_alipay_dict()
            else:
                params['max_queue_num'] = self.max_queue_num
        if self.min_queue_num:
            if hasattr(self.min_queue_num, 'to_alipay_dict'):
                params['min_queue_num'] = self.min_queue_num.to_alipay_dict()
            else:
                params['min_queue_num'] = self.min_queue_num
        if self.queue_desc:
            if hasattr(self.queue_desc, 'to_alipay_dict'):
                params['queue_desc'] = self.queue_desc.to_alipay_dict()
            else:
                params['queue_desc'] = self.queue_desc
        if self.queue_id:
            if hasattr(self.queue_id, 'to_alipay_dict'):
                params['queue_id'] = self.queue_id.to_alipay_dict()
            else:
                params['queue_id'] = self.queue_id
        if self.queue_name:
            if hasattr(self.queue_name, 'to_alipay_dict'):
                params['queue_name'] = self.queue_name.to_alipay_dict()
            else:
                params['queue_name'] = self.queue_name
        if self.queue_option:
            if hasattr(self.queue_option, 'to_alipay_dict'):
                params['queue_option'] = self.queue_option.to_alipay_dict()
            else:
                params['queue_option'] = self.queue_option
        if self.queue_prefix:
            if hasattr(self.queue_prefix, 'to_alipay_dict'):
                params['queue_prefix'] = self.queue_prefix.to_alipay_dict()
            else:
                params['queue_prefix'] = self.queue_prefix
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopQueue()
        if 'max_queue_num' in d:
            o.max_queue_num = d['max_queue_num']
        if 'min_queue_num' in d:
            o.min_queue_num = d['min_queue_num']
        if 'queue_desc' in d:
            o.queue_desc = d['queue_desc']
        if 'queue_id' in d:
            o.queue_id = d['queue_id']
        if 'queue_name' in d:
            o.queue_name = d['queue_name']
        if 'queue_option' in d:
            o.queue_option = d['queue_option']
        if 'queue_prefix' in d:
            o.queue_prefix = d['queue_prefix']
        return o


