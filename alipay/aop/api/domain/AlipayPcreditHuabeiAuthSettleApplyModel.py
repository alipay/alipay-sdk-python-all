#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtraParams import ExtraParams


class AlipayPcreditHuabeiAuthSettleApplyModel(object):

    def __init__(self):
        self._action_type = None
        self._agreement_no = None
        self._alipay_user_id = None
        self._extend_params = None
        self._need_terminated = None
        self._out_request_no = None
        self._pay_amount = None
        self._seller_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtraParams):
            self._extend_params = value
        else:
            self._extend_params = ExtraParams.from_alipay_dict(value)
    @property
    def need_terminated(self):
        return self._need_terminated

    @need_terminated.setter
    def need_terminated(self, value):
        self._need_terminated = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.need_terminated:
            if hasattr(self.need_terminated, 'to_alipay_dict'):
                params['need_terminated'] = self.need_terminated.to_alipay_dict()
            else:
                params['need_terminated'] = self.need_terminated
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAuthSettleApplyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'need_terminated' in d:
            o.need_terminated = d['need_terminated']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


