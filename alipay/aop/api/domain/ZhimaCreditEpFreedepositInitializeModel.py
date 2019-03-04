#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpFreedepositInitializeModel(object):

    def __init__(self):
        self._biz_channel = None
        self._biz_source = None
        self._cert_no = None
        self._cert_type = None
        self._credit_category = None
        self._ep_cert_no = None
        self._ep_cert_type = None
        self._ep_name = None
        self._goto_url = None
        self._member_type = None
        self._merchant_order_no = None
        self._name = None
        self._out_request_no = None
        self._product_code = None
        self._request_id = None

    @property
    def biz_channel(self):
        return self._biz_channel

    @biz_channel.setter
    def biz_channel(self, value):
        self._biz_channel = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def credit_category(self):
        return self._credit_category

    @credit_category.setter
    def credit_category(self, value):
        self._credit_category = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_cert_type(self):
        return self._ep_cert_type

    @ep_cert_type.setter
    def ep_cert_type(self, value):
        self._ep_cert_type = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value
    @property
    def member_type(self):
        return self._member_type

    @member_type.setter
    def member_type(self, value):
        self._member_type = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_channel:
            if hasattr(self.biz_channel, 'to_alipay_dict'):
                params['biz_channel'] = self.biz_channel.to_alipay_dict()
            else:
                params['biz_channel'] = self.biz_channel
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.credit_category:
            if hasattr(self.credit_category, 'to_alipay_dict'):
                params['credit_category'] = self.credit_category.to_alipay_dict()
            else:
                params['credit_category'] = self.credit_category
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_cert_type:
            if hasattr(self.ep_cert_type, 'to_alipay_dict'):
                params['ep_cert_type'] = self.ep_cert_type.to_alipay_dict()
            else:
                params['ep_cert_type'] = self.ep_cert_type
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = self.goto_url.to_alipay_dict()
            else:
                params['goto_url'] = self.goto_url
        if self.member_type:
            if hasattr(self.member_type, 'to_alipay_dict'):
                params['member_type'] = self.member_type.to_alipay_dict()
            else:
                params['member_type'] = self.member_type
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpFreedepositInitializeModel()
        if 'biz_channel' in d:
            o.biz_channel = d['biz_channel']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'credit_category' in d:
            o.credit_category = d['credit_category']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_cert_type' in d:
            o.ep_cert_type = d['ep_cert_type']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'goto_url' in d:
            o.goto_url = d['goto_url']
        if 'member_type' in d:
            o.member_type = d['member_type']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'name' in d:
            o.name = d['name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


