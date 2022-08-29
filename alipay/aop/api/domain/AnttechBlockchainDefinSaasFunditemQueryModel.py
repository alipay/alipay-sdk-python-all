#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasFunditemQueryModel(object):

    def __init__(self):
        self._fund_type = None
        self._out_order_id = None
        self._out_payer_id = None
        self._out_request_id = None
        self._platform_member_id = None

    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_payer_id(self):
        return self._out_payer_id

    @out_payer_id.setter
    def out_payer_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_payer_id = value
        else:
            self._out_payer_id = ReferenceId.from_alipay_dict(value)
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_payer_id:
            if hasattr(self.out_payer_id, 'to_alipay_dict'):
                params['out_payer_id'] = self.out_payer_id.to_alipay_dict()
            else:
                params['out_payer_id'] = self.out_payer_id
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasFunditemQueryModel()
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_payer_id' in d:
            o.out_payer_id = d['out_payer_id']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


