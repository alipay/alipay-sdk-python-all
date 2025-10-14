#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorLoanBatchqueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel_customer_id = None
        self._current_page = None
        self._open_id = None
        self._out_trace_id = None
        self._page_size = None
        self._product_code = None
        self._request_source = None
        self._status = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trace_id(self):
        return self._out_trace_id

    @out_trace_id.setter
    def out_trace_id(self, value):
        self._out_trace_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trace_id:
            if hasattr(self.out_trace_id, 'to_alipay_dict'):
                params['out_trace_id'] = self.out_trace_id.to_alipay_dict()
            else:
                params['out_trace_id'] = self.out_trace_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorLoanBatchqueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_source' in d:
            o.request_source = d['request_source']
        if 'status' in d:
            o.status = d['status']
        return o


