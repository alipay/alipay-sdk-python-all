#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignFileOpenApiDTO(object):

    def __init__(self):
        self._file_name = None
        self._http_oss_url = None
        self._oss_url = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def http_oss_url(self):
        return self._http_oss_url

    @http_oss_url.setter
    def http_oss_url(self, value):
        self._http_oss_url = value
    @property
    def oss_url(self):
        return self._oss_url

    @oss_url.setter
    def oss_url(self, value):
        self._oss_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.http_oss_url:
            if hasattr(self.http_oss_url, 'to_alipay_dict'):
                params['http_oss_url'] = self.http_oss_url.to_alipay_dict()
            else:
                params['http_oss_url'] = self.http_oss_url
        if self.oss_url:
            if hasattr(self.oss_url, 'to_alipay_dict'):
                params['oss_url'] = self.oss_url.to_alipay_dict()
            else:
                params['oss_url'] = self.oss_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignFileOpenApiDTO()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'http_oss_url' in d:
            o.http_oss_url = d['http_oss_url']
        if 'oss_url' in d:
            o.oss_url = d['oss_url']
        return o


