#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppAppcontentInternalQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._pid = None
        self._query_mode = None
        self._ref_app_id = None
        self._request_system = None
        self._service_code_list = None

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
    def query_mode(self):
        return self._query_mode

    @query_mode.setter
    def query_mode(self, value):
        self._query_mode = value
    @property
    def ref_app_id(self):
        return self._ref_app_id

    @ref_app_id.setter
    def ref_app_id(self, value):
        self._ref_app_id = value
    @property
    def request_system(self):
        return self._request_system

    @request_system.setter
    def request_system(self, value):
        self._request_system = value
    @property
    def service_code_list(self):
        return self._service_code_list

    @service_code_list.setter
    def service_code_list(self, value):
        if isinstance(value, list):
            self._service_code_list = list()
            for i in value:
                self._service_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
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
        if self.query_mode:
            if hasattr(self.query_mode, 'to_alipay_dict'):
                params['query_mode'] = self.query_mode.to_alipay_dict()
            else:
                params['query_mode'] = self.query_mode
        if self.ref_app_id:
            if hasattr(self.ref_app_id, 'to_alipay_dict'):
                params['ref_app_id'] = self.ref_app_id.to_alipay_dict()
            else:
                params['ref_app_id'] = self.ref_app_id
        if self.request_system:
            if hasattr(self.request_system, 'to_alipay_dict'):
                params['request_system'] = self.request_system.to_alipay_dict()
            else:
                params['request_system'] = self.request_system
        if self.service_code_list:
            if isinstance(self.service_code_list, list):
                for i in range(0, len(self.service_code_list)):
                    element = self.service_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_code_list[i] = element.to_alipay_dict()
            if hasattr(self.service_code_list, 'to_alipay_dict'):
                params['service_code_list'] = self.service_code_list.to_alipay_dict()
            else:
                params['service_code_list'] = self.service_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAppcontentInternalQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pid' in d:
            o.pid = d['pid']
        if 'query_mode' in d:
            o.query_mode = d['query_mode']
        if 'ref_app_id' in d:
            o.ref_app_id = d['ref_app_id']
        if 'request_system' in d:
            o.request_system = d['request_system']
        if 'service_code_list' in d:
            o.service_code_list = d['service_code_list']
        return o


