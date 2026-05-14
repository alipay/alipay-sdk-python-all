#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._farmer_id = None
        self._proxy_cert_no = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value
    @property
    def proxy_cert_no(self):
        return self._proxy_cert_no

    @proxy_cert_no.setter
    def proxy_cert_no(self, value):
        self._proxy_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.farmer_id:
            if hasattr(self.farmer_id, 'to_alipay_dict'):
                params['farmer_id'] = self.farmer_id.to_alipay_dict()
            else:
                params['farmer_id'] = self.farmer_id
        if self.proxy_cert_no:
            if hasattr(self.proxy_cert_no, 'to_alipay_dict'):
                params['proxy_cert_no'] = self.proxy_cert_no.to_alipay_dict()
            else:
                params['proxy_cert_no'] = self.proxy_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'farmer_id' in d:
            o.farmer_id = d['farmer_id']
        if 'proxy_cert_no' in d:
            o.proxy_cert_no = d['proxy_cert_no']
        return o


