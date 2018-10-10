#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerAuthMutualviewApplyModel(object):

    def __init__(self):
        self._biz_type = None
        self._callback_url = None
        self._ext_biz_param = None
        self._identity_param = None
        self._product_param = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def ext_biz_param(self):
        return self._ext_biz_param

    @ext_biz_param.setter
    def ext_biz_param(self, value):
        self._ext_biz_param = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value
    @property
    def product_param(self):
        return self._product_param

    @product_param.setter
    def product_param(self, value):
        self._product_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.ext_biz_param:
            if hasattr(self.ext_biz_param, 'to_alipay_dict'):
                params['ext_biz_param'] = self.ext_biz_param.to_alipay_dict()
            else:
                params['ext_biz_param'] = self.ext_biz_param
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.product_param:
            if hasattr(self.product_param, 'to_alipay_dict'):
                params['product_param'] = self.product_param.to_alipay_dict()
            else:
                params['product_param'] = self.product_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerAuthMutualviewApplyModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'ext_biz_param' in d:
            o.ext_biz_param = d['ext_biz_param']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'product_param' in d:
            o.product_param = d['product_param']
        return o


