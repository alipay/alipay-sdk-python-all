#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpBasicinfoAlterSubscribeModel(object):

    def __init__(self):
        self._ep_cert_no = None
        self._listen_group_id = None
        self._product_code = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def listen_group_id(self):
        return self._listen_group_id

    @listen_group_id.setter
    def listen_group_id(self, value):
        self._listen_group_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.listen_group_id:
            if hasattr(self.listen_group_id, 'to_alipay_dict'):
                params['listen_group_id'] = self.listen_group_id.to_alipay_dict()
            else:
                params['listen_group_id'] = self.listen_group_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpBasicinfoAlterSubscribeModel()
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'listen_group_id' in d:
            o.listen_group_id = d['listen_group_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


