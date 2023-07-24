#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IntactChargeInfo(object):

    def __init__(self):
        self._actual_amount = None
        self._bill_type = None
        self._gmt_pay = None
        self._is_refund = None
        self._out_biz_no = None
        self._plan_amount = None
        self._product_name = None
        self._service_target = None
        self._service_type = None
        self._status = None
        self._target_account_no = None
        self._target_user_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def is_refund(self):
        return self._is_refund

    @is_refund.setter
    def is_refund(self, value):
        self._is_refund = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plan_amount(self):
        return self._plan_amount

    @plan_amount.setter
    def plan_amount(self, value):
        self._plan_amount = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def service_target(self):
        return self._service_target

    @service_target.setter
    def service_target(self, value):
        self._service_target = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_account_no(self):
        return self._target_account_no

    @target_account_no.setter
    def target_account_no(self, value):
        self._target_account_no = value
    @property
    def target_user_id(self):
        return self._target_user_id

    @target_user_id.setter
    def target_user_id(self, value):
        self._target_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.is_refund:
            if hasattr(self.is_refund, 'to_alipay_dict'):
                params['is_refund'] = self.is_refund.to_alipay_dict()
            else:
                params['is_refund'] = self.is_refund
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.plan_amount:
            if hasattr(self.plan_amount, 'to_alipay_dict'):
                params['plan_amount'] = self.plan_amount.to_alipay_dict()
            else:
                params['plan_amount'] = self.plan_amount
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.service_target:
            if hasattr(self.service_target, 'to_alipay_dict'):
                params['service_target'] = self.service_target.to_alipay_dict()
            else:
                params['service_target'] = self.service_target
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_account_no:
            if hasattr(self.target_account_no, 'to_alipay_dict'):
                params['target_account_no'] = self.target_account_no.to_alipay_dict()
            else:
                params['target_account_no'] = self.target_account_no
        if self.target_user_id:
            if hasattr(self.target_user_id, 'to_alipay_dict'):
                params['target_user_id'] = self.target_user_id.to_alipay_dict()
            else:
                params['target_user_id'] = self.target_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntactChargeInfo()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'is_refund' in d:
            o.is_refund = d['is_refund']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plan_amount' in d:
            o.plan_amount = d['plan_amount']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'service_target' in d:
            o.service_target = d['service_target']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'status' in d:
            o.status = d['status']
        if 'target_account_no' in d:
            o.target_account_no = d['target_account_no']
        if 'target_user_id' in d:
            o.target_user_id = d['target_user_id']
        return o


