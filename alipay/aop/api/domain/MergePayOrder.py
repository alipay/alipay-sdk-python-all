#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MergePayOrder(object):

    def __init__(self):
        self._amount = None
        self._fail_reason = None
        self._fee = None
        self._order_id = None
        self._out_biz_no = None
        self._payee_display_account = None
        self._payee_display_name = None
        self._payee_inst_id = None
        self._payee_inst_name = None
        self._payee_portrait_id = None
        self._payee_type = None
        self._remark = None
        self._status = None
        self._withdraw_delay = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_display_account(self):
        return self._payee_display_account

    @payee_display_account.setter
    def payee_display_account(self, value):
        self._payee_display_account = value
    @property
    def payee_display_name(self):
        return self._payee_display_name

    @payee_display_name.setter
    def payee_display_name(self, value):
        self._payee_display_name = value
    @property
    def payee_inst_id(self):
        return self._payee_inst_id

    @payee_inst_id.setter
    def payee_inst_id(self, value):
        self._payee_inst_id = value
    @property
    def payee_inst_name(self):
        return self._payee_inst_name

    @payee_inst_name.setter
    def payee_inst_name(self, value):
        self._payee_inst_name = value
    @property
    def payee_portrait_id(self):
        return self._payee_portrait_id

    @payee_portrait_id.setter
    def payee_portrait_id(self, value):
        self._payee_portrait_id = value
    @property
    def payee_type(self):
        return self._payee_type

    @payee_type.setter
    def payee_type(self, value):
        self._payee_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def withdraw_delay(self):
        return self._withdraw_delay

    @withdraw_delay.setter
    def withdraw_delay(self, value):
        self._withdraw_delay = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_display_account:
            if hasattr(self.payee_display_account, 'to_alipay_dict'):
                params['payee_display_account'] = self.payee_display_account.to_alipay_dict()
            else:
                params['payee_display_account'] = self.payee_display_account
        if self.payee_display_name:
            if hasattr(self.payee_display_name, 'to_alipay_dict'):
                params['payee_display_name'] = self.payee_display_name.to_alipay_dict()
            else:
                params['payee_display_name'] = self.payee_display_name
        if self.payee_inst_id:
            if hasattr(self.payee_inst_id, 'to_alipay_dict'):
                params['payee_inst_id'] = self.payee_inst_id.to_alipay_dict()
            else:
                params['payee_inst_id'] = self.payee_inst_id
        if self.payee_inst_name:
            if hasattr(self.payee_inst_name, 'to_alipay_dict'):
                params['payee_inst_name'] = self.payee_inst_name.to_alipay_dict()
            else:
                params['payee_inst_name'] = self.payee_inst_name
        if self.payee_portrait_id:
            if hasattr(self.payee_portrait_id, 'to_alipay_dict'):
                params['payee_portrait_id'] = self.payee_portrait_id.to_alipay_dict()
            else:
                params['payee_portrait_id'] = self.payee_portrait_id
        if self.payee_type:
            if hasattr(self.payee_type, 'to_alipay_dict'):
                params['payee_type'] = self.payee_type.to_alipay_dict()
            else:
                params['payee_type'] = self.payee_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.withdraw_delay:
            if hasattr(self.withdraw_delay, 'to_alipay_dict'):
                params['withdraw_delay'] = self.withdraw_delay.to_alipay_dict()
            else:
                params['withdraw_delay'] = self.withdraw_delay
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MergePayOrder()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'fee' in d:
            o.fee = d['fee']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_display_account' in d:
            o.payee_display_account = d['payee_display_account']
        if 'payee_display_name' in d:
            o.payee_display_name = d['payee_display_name']
        if 'payee_inst_id' in d:
            o.payee_inst_id = d['payee_inst_id']
        if 'payee_inst_name' in d:
            o.payee_inst_name = d['payee_inst_name']
        if 'payee_portrait_id' in d:
            o.payee_portrait_id = d['payee_portrait_id']
        if 'payee_type' in d:
            o.payee_type = d['payee_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'withdraw_delay' in d:
            o.withdraw_delay = d['withdraw_delay']
        return o


