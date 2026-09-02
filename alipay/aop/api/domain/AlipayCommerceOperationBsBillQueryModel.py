#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationBsBillQueryModel(object):

    def __init__(self):
        self._cursor = None
        self._end_time = None
        self._need_count = None
        self._page_size = None
        self._plan_id = None
        self._start_time = None

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def need_count(self):
        return self._need_count

    @need_count.setter
    def need_count(self, value):
        self._need_count = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cursor:
            if hasattr(self.cursor, 'to_alipay_dict'):
                params['cursor'] = self.cursor.to_alipay_dict()
            else:
                params['cursor'] = self.cursor
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.need_count:
            if hasattr(self.need_count, 'to_alipay_dict'):
                params['need_count'] = self.need_count.to_alipay_dict()
            else:
                params['need_count'] = self.need_count
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBsBillQueryModel()
        if 'cursor' in d:
            o.cursor = d['cursor']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'need_count' in d:
            o.need_count = d['need_count']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


