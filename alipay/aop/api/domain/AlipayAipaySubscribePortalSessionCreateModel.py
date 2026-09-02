#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipaySubscribePortalSessionCreateModel(object):

    def __init__(self):
        self._customer_id = None
        self._portal_code = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def portal_code(self):
        return self._portal_code

    @portal_code.setter
    def portal_code(self, value):
        self._portal_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.portal_code:
            if hasattr(self.portal_code, 'to_alipay_dict'):
                params['portal_code'] = self.portal_code.to_alipay_dict()
            else:
                params['portal_code'] = self.portal_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipaySubscribePortalSessionCreateModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'portal_code' in d:
            o.portal_code = d['portal_code']
        return o


