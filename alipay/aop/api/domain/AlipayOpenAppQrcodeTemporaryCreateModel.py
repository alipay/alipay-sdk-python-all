#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppQrcodeTemporaryCreateModel(object):

    def __init__(self):
        self._color = None
        self._qrcode_type = None
        self._query_param = None
        self._timeout = None
        self._url_param = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def qrcode_type(self):
        return self._qrcode_type

    @qrcode_type.setter
    def qrcode_type(self, value):
        self._qrcode_type = value
    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, value):
        self._query_param = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def url_param(self):
        return self._url_param

    @url_param.setter
    def url_param(self, value):
        self._url_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.qrcode_type:
            if hasattr(self.qrcode_type, 'to_alipay_dict'):
                params['qrcode_type'] = self.qrcode_type.to_alipay_dict()
            else:
                params['qrcode_type'] = self.qrcode_type
        if self.query_param:
            if hasattr(self.query_param, 'to_alipay_dict'):
                params['query_param'] = self.query_param.to_alipay_dict()
            else:
                params['query_param'] = self.query_param
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        if self.url_param:
            if hasattr(self.url_param, 'to_alipay_dict'):
                params['url_param'] = self.url_param.to_alipay_dict()
            else:
                params['url_param'] = self.url_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppQrcodeTemporaryCreateModel()
        if 'color' in d:
            o.color = d['color']
        if 'qrcode_type' in d:
            o.qrcode_type = d['qrcode_type']
        if 'query_param' in d:
            o.query_param = d['query_param']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'url_param' in d:
            o.url_param = d['url_param']
        return o


