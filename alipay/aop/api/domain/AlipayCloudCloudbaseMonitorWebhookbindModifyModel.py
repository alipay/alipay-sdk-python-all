#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseMonitorWebhookbindModifyModel(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._open = None
        self._request_body = None
        self._request_headers = None
        self._request_type = None
        self._request_url = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
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
        o = AlipayCloudCloudbaseMonitorWebhookbindModifyModel()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'open' in d:
            o.open = d['open']
        if 'request_body' in d:
            o.request_body = d['request_body']
        if 'request_headers' in d:
            o.request_headers = d['request_headers']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'request_url' in d:
            o.request_url = d['request_url']
        return o


