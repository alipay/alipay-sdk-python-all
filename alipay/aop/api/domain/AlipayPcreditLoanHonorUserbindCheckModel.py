#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorUserbindCheckModel(object):

    def __init__(self):
        self._channel_customer_id = None
        self._ctf_code = None
        self._mobile_no = None
        self._out_trace_id = None
        self._product_code = None
        self._real_name = None
        self._request_source = None

    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def ctf_code(self):
        return self._ctf_code

    @ctf_code.setter
    def ctf_code(self, value):
        self._ctf_code = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def out_trace_id(self):
        return self._out_trace_id

    @out_trace_id.setter
    def out_trace_id(self, value):
        self._out_trace_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.ctf_code:
            if hasattr(self.ctf_code, 'to_alipay_dict'):
                params['ctf_code'] = self.ctf_code.to_alipay_dict()
            else:
                params['ctf_code'] = self.ctf_code
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.out_trace_id:
            if hasattr(self.out_trace_id, 'to_alipay_dict'):
                params['out_trace_id'] = self.out_trace_id.to_alipay_dict()
            else:
                params['out_trace_id'] = self.out_trace_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorUserbindCheckModel()
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'ctf_code' in d:
            o.ctf_code = d['ctf_code']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'request_source' in d:
            o.request_source = d['request_source']
        return o


