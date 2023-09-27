#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.PayerDetailVO import PayerDetailVO


class AnttechBlockchainDefinSaasPaymentPayModel(object):

    def __init__(self):
        self._order_pay_time = None
        self._out_order_id = None
        self._out_payee_id = None
        self._out_payer_id = None
        self._payer_detail = None
        self._platform_member_id = None

    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_payee_id(self):
        return self._out_payee_id

    @out_payee_id.setter
    def out_payee_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_payee_id = value
        else:
            self._out_payee_id = ReferenceId.from_alipay_dict(value)
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
    def payer_detail(self):
        return self._payer_detail

    @payer_detail.setter
    def payer_detail(self, value):
        if isinstance(value, PayerDetailVO):
            self._payer_detail = value
        else:
            self._payer_detail = PayerDetailVO.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_payee_id:
            if hasattr(self.out_payee_id, 'to_alipay_dict'):
                params['out_payee_id'] = self.out_payee_id.to_alipay_dict()
            else:
                params['out_payee_id'] = self.out_payee_id
        if self.out_payer_id:
            if hasattr(self.out_payer_id, 'to_alipay_dict'):
                params['out_payer_id'] = self.out_payer_id.to_alipay_dict()
            else:
                params['out_payer_id'] = self.out_payer_id
        if self.payer_detail:
            if hasattr(self.payer_detail, 'to_alipay_dict'):
                params['payer_detail'] = self.payer_detail.to_alipay_dict()
            else:
                params['payer_detail'] = self.payer_detail
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
        o = AnttechBlockchainDefinSaasPaymentPayModel()
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_payee_id' in d:
            o.out_payee_id = d['out_payee_id']
        if 'out_payer_id' in d:
            o.out_payer_id = d['out_payer_id']
        if 'payer_detail' in d:
            o.payer_detail = d['payer_detail']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


