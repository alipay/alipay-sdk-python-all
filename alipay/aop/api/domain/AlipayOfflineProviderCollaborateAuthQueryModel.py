#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateAuthQueryModel(object):

    def __init__(self):
        self._auth_order_id = None
        self._out_biz_no = None

    @property
    def auth_order_id(self):
        return self._auth_order_id

    @auth_order_id.setter
    def auth_order_id(self, value):
        self._auth_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_order_id:
            if hasattr(self.auth_order_id, 'to_alipay_dict'):
                params['auth_order_id'] = self.auth_order_id.to_alipay_dict()
            else:
                params['auth_order_id'] = self.auth_order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateAuthQueryModel()
        if 'auth_order_id' in d:
            o.auth_order_id = d['auth_order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


