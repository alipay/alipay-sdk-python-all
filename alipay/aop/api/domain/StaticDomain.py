#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ErrorPageSetting import ErrorPageSetting


class StaticDomain(object):

    def __init__(self):
        self._cname = None
        self._domain_name = None
        self._domain_type = None
        self._enable_https = None
        self._error_page = None
        self._index_file = None
        self._status = None

    @property
    def cname(self):
        return self._cname

    @cname.setter
    def cname(self, value):
        self._cname = value
    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value
    @property
    def domain_type(self):
        return self._domain_type

    @domain_type.setter
    def domain_type(self, value):
        self._domain_type = value
    @property
    def enable_https(self):
        return self._enable_https

    @enable_https.setter
    def enable_https(self, value):
        self._enable_https = value
    @property
    def error_page(self):
        return self._error_page

    @error_page.setter
    def error_page(self, value):
        if isinstance(value, ErrorPageSetting):
            self._error_page = value
        else:
            self._error_page = ErrorPageSetting.from_alipay_dict(value)
    @property
    def index_file(self):
        return self._index_file

    @index_file.setter
    def index_file(self, value):
        self._index_file = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cname:
            if hasattr(self.cname, 'to_alipay_dict'):
                params['cname'] = self.cname.to_alipay_dict()
            else:
                params['cname'] = self.cname
        if self.domain_name:
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
        if self.domain_type:
            if hasattr(self.domain_type, 'to_alipay_dict'):
                params['domain_type'] = self.domain_type.to_alipay_dict()
            else:
                params['domain_type'] = self.domain_type
        if self.enable_https:
            if hasattr(self.enable_https, 'to_alipay_dict'):
                params['enable_https'] = self.enable_https.to_alipay_dict()
            else:
                params['enable_https'] = self.enable_https
        if self.error_page:
            if hasattr(self.error_page, 'to_alipay_dict'):
                params['error_page'] = self.error_page.to_alipay_dict()
            else:
                params['error_page'] = self.error_page
        if self.index_file:
            if hasattr(self.index_file, 'to_alipay_dict'):
                params['index_file'] = self.index_file.to_alipay_dict()
            else:
                params['index_file'] = self.index_file
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StaticDomain()
        if 'cname' in d:
            o.cname = d['cname']
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        if 'domain_type' in d:
            o.domain_type = d['domain_type']
        if 'enable_https' in d:
            o.enable_https = d['enable_https']
        if 'error_page' in d:
            o.error_page = d['error_page']
        if 'index_file' in d:
            o.index_file = d['index_file']
        if 'status' in d:
            o.status = d['status']
        return o


