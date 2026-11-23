#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasBankverifyCreateModel(object):

    def __init__(self):
        self._out_request_no = None
        self._out_return_url = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_return_url(self):
        return self._out_return_url

    @out_return_url.setter
    def out_return_url(self, value):
        self._out_return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_return_url:
            if hasattr(self.out_return_url, 'to_alipay_dict'):
                params['out_return_url'] = self.out_return_url.to_alipay_dict()
            else:
                params['out_return_url'] = self.out_return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasBankverifyCreateModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_return_url' in d:
            o.out_return_url = d['out_return_url']
        return o


