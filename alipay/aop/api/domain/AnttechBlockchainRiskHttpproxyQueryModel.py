#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainRiskHttpproxyQueryModel(object):

    def __init__(self):
        self._char_set = None
        self._content_type = None
        self._data = None
        self._headers = None
        self._http_method = None
        self._params = None
        self._url = None

    @property
    def char_set(self):
        return self._char_set

    @char_set.setter
    def char_set(self, value):
        self._char_set = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value
    @property
    def http_method(self):
        return self._http_method

    @http_method.setter
    def http_method(self, value):
        self._http_method = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.char_set:
            if hasattr(self.char_set, 'to_alipay_dict'):
                params['char_set'] = self.char_set.to_alipay_dict()
            else:
                params['char_set'] = self.char_set
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.headers:
            if hasattr(self.headers, 'to_alipay_dict'):
                params['headers'] = self.headers.to_alipay_dict()
            else:
                params['headers'] = self.headers
        if self.http_method:
            if hasattr(self.http_method, 'to_alipay_dict'):
                params['http_method'] = self.http_method.to_alipay_dict()
            else:
                params['http_method'] = self.http_method
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainRiskHttpproxyQueryModel()
        if 'char_set' in d:
            o.char_set = d['char_set']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'data' in d:
            o.data = d['data']
        if 'headers' in d:
            o.headers = d['headers']
        if 'http_method' in d:
            o.http_method = d['http_method']
        if 'params' in d:
            o.params = d['params']
        if 'url' in d:
            o.url = d['url']
        return o


