#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcOrderVO(object):

    def __init__(self):
        self._mpc_order_code = None
        self._url = None

    @property
    def mpc_order_code(self):
        return self._mpc_order_code

    @mpc_order_code.setter
    def mpc_order_code(self, value):
        self._mpc_order_code = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.mpc_order_code:
            if hasattr(self.mpc_order_code, 'to_alipay_dict'):
                params['mpc_order_code'] = self.mpc_order_code.to_alipay_dict()
            else:
                params['mpc_order_code'] = self.mpc_order_code
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcOrderVO()
        if 'mpc_order_code' in d:
            o.mpc_order_code = d['mpc_order_code']
        if 'url' in d:
            o.url = d['url']
        return o


