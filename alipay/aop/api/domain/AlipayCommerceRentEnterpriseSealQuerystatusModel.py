#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentEnterpriseSealQuerystatusModel(object):

    def __init__(self):
        self._biz_no = None
        self._sign_flow_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.sign_flow_id:
            if hasattr(self.sign_flow_id, 'to_alipay_dict'):
                params['sign_flow_id'] = self.sign_flow_id.to_alipay_dict()
            else:
                params['sign_flow_id'] = self.sign_flow_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentEnterpriseSealQuerystatusModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'sign_flow_id' in d:
            o.sign_flow_id = d['sign_flow_id']
        return o


