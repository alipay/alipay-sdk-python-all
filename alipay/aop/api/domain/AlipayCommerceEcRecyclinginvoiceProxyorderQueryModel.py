#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceProxyorderQueryModel(object):

    def __init__(self):
        self._out_request_no = None
        self._proxy_order_id = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def proxy_order_id(self):
        return self._proxy_order_id

    @proxy_order_id.setter
    def proxy_order_id(self, value):
        self._proxy_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.proxy_order_id:
            if hasattr(self.proxy_order_id, 'to_alipay_dict'):
                params['proxy_order_id'] = self.proxy_order_id.to_alipay_dict()
            else:
                params['proxy_order_id'] = self.proxy_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceProxyorderQueryModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'proxy_order_id' in d:
            o.proxy_order_id = d['proxy_order_id']
        return o


