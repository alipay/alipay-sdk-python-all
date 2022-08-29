#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasPaymentCheckModel(object):

    def __init__(self):
        self._fund_mode = None
        self._order_type = None
        self._payee_out_member_id = None
        self._payer_out_member_id = None
        self._platform_member_id = None

    @property
    def fund_mode(self):
        return self._fund_mode

    @fund_mode.setter
    def fund_mode(self, value):
        self._fund_mode = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def payee_out_member_id(self):
        return self._payee_out_member_id

    @payee_out_member_id.setter
    def payee_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._payee_out_member_id = value
        else:
            self._payee_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def payer_out_member_id(self):
        return self._payer_out_member_id

    @payer_out_member_id.setter
    def payer_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._payer_out_member_id = value
        else:
            self._payer_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_mode:
            if hasattr(self.fund_mode, 'to_alipay_dict'):
                params['fund_mode'] = self.fund_mode.to_alipay_dict()
            else:
                params['fund_mode'] = self.fund_mode
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.payee_out_member_id:
            if hasattr(self.payee_out_member_id, 'to_alipay_dict'):
                params['payee_out_member_id'] = self.payee_out_member_id.to_alipay_dict()
            else:
                params['payee_out_member_id'] = self.payee_out_member_id
        if self.payer_out_member_id:
            if hasattr(self.payer_out_member_id, 'to_alipay_dict'):
                params['payer_out_member_id'] = self.payer_out_member_id.to_alipay_dict()
            else:
                params['payer_out_member_id'] = self.payer_out_member_id
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
        o = AnttechBlockchainDefinSaasPaymentCheckModel()
        if 'fund_mode' in d:
            o.fund_mode = d['fund_mode']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'payee_out_member_id' in d:
            o.payee_out_member_id = d['payee_out_member_id']
        if 'payer_out_member_id' in d:
            o.payer_out_member_id = d['payer_out_member_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


