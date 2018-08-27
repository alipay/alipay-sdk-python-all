#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingEncodeShortlinkCreateModel(object):

    def __init__(self):
        self._biz_identifier = None
        self._encode_url = None
        self._timeout = None

    @property
    def biz_identifier(self):
        return self._biz_identifier

    @biz_identifier.setter
    def biz_identifier(self, value):
        self._biz_identifier = value
    @property
    def encode_url(self):
        return self._encode_url

    @encode_url.setter
    def encode_url(self, value):
        self._encode_url = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identifier:
            if hasattr(self.biz_identifier, 'to_alipay_dict'):
                params['biz_identifier'] = self.biz_identifier.to_alipay_dict()
            else:
                params['biz_identifier'] = self.biz_identifier
        if self.encode_url:
            if hasattr(self.encode_url, 'to_alipay_dict'):
                params['encode_url'] = self.encode_url.to_alipay_dict()
            else:
                params['encode_url'] = self.encode_url
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingEncodeShortlinkCreateModel()
        if 'biz_identifier' in d:
            o.biz_identifier = d['biz_identifier']
        if 'encode_url' in d:
            o.encode_url = d['encode_url']
        if 'timeout' in d:
            o.timeout = d['timeout']
        return o


