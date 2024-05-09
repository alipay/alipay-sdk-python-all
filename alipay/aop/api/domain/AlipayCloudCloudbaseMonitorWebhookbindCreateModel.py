#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseMonitorWebhookbindCreateModel(object):

    def __init__(self):
        self._name = None
        self._request_body = None
        self._request_headers = None
        self._request_type = None
        self._request_url = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value
    @property
    def request_headers(self):
        return self._request_headers

    @request_headers.setter
    def request_headers(self, value):
        self._request_headers = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def request_url(self):
        return self._request_url

    @request_url.setter
    def request_url(self, value):
        self._request_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.request_body:
            if hasattr(self.request_body, 'to_alipay_dict'):
                params['request_body'] = self.request_body.to_alipay_dict()
            else:
                params['request_body'] = self.request_body
        if self.request_headers:
            if hasattr(self.request_headers, 'to_alipay_dict'):
                params['request_headers'] = self.request_headers.to_alipay_dict()
            else:
                params['request_headers'] = self.request_headers
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.request_url:
            if hasattr(self.request_url, 'to_alipay_dict'):
                params['request_url'] = self.request_url.to_alipay_dict()
            else:
                params['request_url'] = self.request_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseMonitorWebhookbindCreateModel()
        if 'name' in d:
            o.name = d['name']
        if 'request_body' in d:
            o.request_body = d['request_body']
        if 'request_headers' in d:
            o.request_headers = d['request_headers']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'request_url' in d:
            o.request_url = d['request_url']
        return o


