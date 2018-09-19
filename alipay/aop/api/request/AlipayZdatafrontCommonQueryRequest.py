#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayZdatafrontCommonQueryRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._cache_interval = None
        self._query_conditions = None
        self._service_name = None
        self._visit_biz = None
        self._visit_biz_line = None
        self._visit_domain = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def cache_interval(self):
        return self._cache_interval

    @cache_interval.setter
    def cache_interval(self, value):
        self._cache_interval = value
    @property
    def query_conditions(self):
        return self._query_conditions

    @query_conditions.setter
    def query_conditions(self, value):
        self._query_conditions = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def visit_biz(self):
        return self._visit_biz

    @visit_biz.setter
    def visit_biz(self, value):
        self._visit_biz = value
    @property
    def visit_biz_line(self):
        return self._visit_biz_line

    @visit_biz_line.setter
    def visit_biz_line(self, value):
        self._visit_biz_line = value
    @property
    def visit_domain(self):
        return self._visit_domain

    @visit_domain.setter
    def visit_domain(self, value):
        self._visit_domain = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.zdatafront.common.query'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.cache_interval:
            if hasattr(self.cache_interval, 'to_alipay_dict'):
                params['cache_interval'] = json.dumps(obj=self.cache_interval.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['cache_interval'] = self.cache_interval
        if self.query_conditions:
            if hasattr(self.query_conditions, 'to_alipay_dict'):
                params['query_conditions'] = json.dumps(obj=self.query_conditions.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['query_conditions'] = self.query_conditions
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = json.dumps(obj=self.service_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['service_name'] = self.service_name
        if self.visit_biz:
            if hasattr(self.visit_biz, 'to_alipay_dict'):
                params['visit_biz'] = json.dumps(obj=self.visit_biz.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['visit_biz'] = self.visit_biz
        if self.visit_biz_line:
            if hasattr(self.visit_biz_line, 'to_alipay_dict'):
                params['visit_biz_line'] = json.dumps(obj=self.visit_biz_line.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['visit_biz_line'] = self.visit_biz_line
        if self.visit_domain:
            if hasattr(self.visit_domain, 'to_alipay_dict'):
                params['visit_domain'] = json.dumps(obj=self.visit_domain.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['visit_domain'] = self.visit_domain
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
