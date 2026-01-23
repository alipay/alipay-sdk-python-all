#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChceckReport(object):

    def __init__(self):
        self._create_time = None
        self._pdf_url = None
        self._test_name = None
        self._vendor_code = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def pdf_url(self):
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, value):
        self._pdf_url = value
    @property
    def test_name(self):
        return self._test_name

    @test_name.setter
    def test_name(self, value):
        self._test_name = value
    @property
    def vendor_code(self):
        return self._vendor_code

    @vendor_code.setter
    def vendor_code(self, value):
        self._vendor_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.pdf_url:
            if hasattr(self.pdf_url, 'to_alipay_dict'):
                params['pdf_url'] = self.pdf_url.to_alipay_dict()
            else:
                params['pdf_url'] = self.pdf_url
        if self.test_name:
            if hasattr(self.test_name, 'to_alipay_dict'):
                params['test_name'] = self.test_name.to_alipay_dict()
            else:
                params['test_name'] = self.test_name
        if self.vendor_code:
            if hasattr(self.vendor_code, 'to_alipay_dict'):
                params['vendor_code'] = self.vendor_code.to_alipay_dict()
            else:
                params['vendor_code'] = self.vendor_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChceckReport()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'pdf_url' in d:
            o.pdf_url = d['pdf_url']
        if 'test_name' in d:
            o.test_name = d['test_name']
        if 'vendor_code' in d:
            o.vendor_code = d['vendor_code']
        return o


