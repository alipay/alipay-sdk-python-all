#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialStoretaskBatchqueryModel(object):

    def __init__(self):
        self._end_time = None
        self._mini_app_id = None
        self._page_num = None
        self._page_size = None
        self._pid = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
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
        o = AlipayContentCommercialStoretaskBatchqueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pid' in d:
            o.pid = d['pid']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


