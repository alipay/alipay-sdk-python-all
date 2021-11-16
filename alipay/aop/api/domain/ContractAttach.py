#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractAttach(object):

    def __init__(self):
        self._biz_status = None
        self._file_location = None
        self._file_name = None
        self._file_type = None
        self._file_url = None
        self._type_is_http = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def file_location(self):
        return self._file_location

    @file_location.setter
    def file_location(self, value):
        self._file_location = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def type_is_http(self):
        return self._type_is_http

    @type_is_http.setter
    def type_is_http(self, value):
        self._type_is_http = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.file_location:
            if hasattr(self.file_location, 'to_alipay_dict'):
                params['file_location'] = self.file_location.to_alipay_dict()
            else:
                params['file_location'] = self.file_location
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.type_is_http:
            if hasattr(self.type_is_http, 'to_alipay_dict'):
                params['type_is_http'] = self.type_is_http.to_alipay_dict()
            else:
                params['type_is_http'] = self.type_is_http
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractAttach()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'file_location' in d:
            o.file_location = d['file_location']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'type_is_http' in d:
            o.type_is_http = d['type_is_http']
        return o


