#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleExtraParams import SettleExtraParams


class ZhimaCreditPeZmgoSettleApplyModel(object):

    def __init__(self):
        self._action_type = None
        self._agreement_id = None
        self._alipay_user_id = None
        self._out_request_no = None
        self._partner_id = None
        self._pay_amount = None
        self._settle_extend_params = None
        self._total_discount_amount = None
        self._total_real_pay_amount = None
        self._total_task_count = None
        self._withhold_plan_no = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def settle_extend_params(self):
        return self._settle_extend_params

    @settle_extend_params.setter
    def settle_extend_params(self, value):
        if isinstance(value, SettleExtraParams):
            self._settle_extend_params = value
        else:
            self._settle_extend_params = SettleExtraParams.from_alipay_dict(value)
    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, value):
        self._total_discount_amount = value
    @property
    def total_real_pay_amount(self):
        return self._total_real_pay_amount

    @total_real_pay_amount.setter
    def total_real_pay_amount(self, value):
        self._total_real_pay_amount = value
    @property
    def total_task_count(self):
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, value):
        self._total_task_count = value
    @property
    def withhold_plan_no(self):
        return self._withhold_plan_no

    @withhold_plan_no.setter
    def withhold_plan_no(self, value):
        self._withhold_plan_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.settle_extend_params:
            if hasattr(self.settle_extend_params, 'to_alipay_dict'):
                params['settle_extend_params'] = self.settle_extend_params.to_alipay_dict()
            else:
                params['settle_extend_params'] = self.settle_extend_params
        if self.total_discount_amount:
            if hasattr(self.total_discount_amount, 'to_alipay_dict'):
                params['total_discount_amount'] = self.total_discount_amount.to_alipay_dict()
            else:
                params['total_discount_amount'] = self.total_discount_amount
        if self.total_real_pay_amount:
            if hasattr(self.total_real_pay_amount, 'to_alipay_dict'):
                params['total_real_pay_amount'] = self.total_real_pay_amount.to_alipay_dict()
            else:
                params['total_real_pay_amount'] = self.total_real_pay_amount
        if self.total_task_count:
            if hasattr(self.total_task_count, 'to_alipay_dict'):
                params['total_task_count'] = self.total_task_count.to_alipay_dict()
            else:
                params['total_task_count'] = self.total_task_count
        if self.withhold_plan_no:
            if hasattr(self.withhold_plan_no, 'to_alipay_dict'):
                params['withhold_plan_no'] = self.withhold_plan_no.to_alipay_dict()
            else:
                params['withhold_plan_no'] = self.withhold_plan_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoSettleApplyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'settle_extend_params' in d:
            o.settle_extend_params = d['settle_extend_params']
        if 'total_discount_amount' in d:
            o.total_discount_amount = d['total_discount_amount']
        if 'total_real_pay_amount' in d:
            o.total_real_pay_amount = d['total_real_pay_amount']
        if 'total_task_count' in d:
            o.total_task_count = d['total_task_count']
        if 'withhold_plan_no' in d:
            o.withhold_plan_no = d['withhold_plan_no']
        return o


