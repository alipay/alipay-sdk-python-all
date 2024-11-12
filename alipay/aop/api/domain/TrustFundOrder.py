#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrustFundOrder(object):

    def __init__(self):
        self._amount = None
        self._channel_order_id = None
        self._fund_status = None
        self._pay_time = None
        self._payee_account_no = None
        self._payee_account_type = None
        self._payee_name = None
        self._payer_account_no = None
        self._payer_account_type = None
        self._payer_name = None
        self._remark = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.fund_status:
            if hasattr(self.fund_status, 'to_alipay_dict'):
                params['fund_status'] = self.fund_status.to_alipay_dict()
            else:
                params['fund_status'] = self.fund_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustFundOrder()
        if 'amount' in d:
            o.amount = d['amount']
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'fund_status' in d:
            o.fund_status = d['fund_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'remark' in d:
            o.remark = d['remark']
        return o


