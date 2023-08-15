#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseFunctionLogQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._desc = None
        self._end = None
        self._function_name = None
        self._page_index = None
        self._page_size = None
        self._show_system_log = None
        self._start = None
        self._trace_id = None
        self._user_query = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def show_system_log(self):
        return self._show_system_log

    @show_system_log.setter
    def show_system_log(self, value):
        self._show_system_log = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_query(self):
        return self._user_query

    @user_query.setter
    def user_query(self, value):
        self._user_query = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.show_system_log:
            if hasattr(self.show_system_log, 'to_alipay_dict'):
                params['show_system_log'] = self.show_system_log.to_alipay_dict()
            else:
                params['show_system_log'] = self.show_system_log
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.user_query:
            if hasattr(self.user_query, 'to_alipay_dict'):
                params['user_query'] = self.user_query.to_alipay_dict()
            else:
                params['user_query'] = self.user_query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionLogQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end' in d:
            o.end = d['end']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'show_system_log' in d:
            o.show_system_log = d['show_system_log']
        if 'start' in d:
            o.start = d['start']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_query' in d:
            o.user_query = d['user_query']
        return o


