#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppPdeductAsyncPayModel(object):

    def __init__(self):
        self._agent_channel = None
        self._agent_code = None
        self._agreement_id = None
        self._bill_date = None
        self._bill_key = None
        self._extend_field = None
        self._fine_amount = None
        self._memo = None
        self._out_order_no = None
        self._pay_amount = None
        self._pid = None
        self._user_id = None

    @property
    def agent_channel(self):
        return self._agent_channel

    @agent_channel.setter
    def agent_channel(self, value):
        self._agent_channel = value
    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def fine_amount(self):
        return self._fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self._fine_amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_channel:
            if hasattr(self.agent_channel, 'to_alipay_dict'):
                params['agent_channel'] = self.agent_channel.to_alipay_dict()
            else:
                params['agent_channel'] = self.agent_channel
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.fine_amount:
            if hasattr(self.fine_amount, 'to_alipay_dict'):
                params['fine_amount'] = self.fine_amount.to_alipay_dict()
            else:
                params['fine_amount'] = self.fine_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppPdeductAsyncPayModel()
        if 'agent_channel' in d:
            o.agent_channel = d['agent_channel']
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'fine_amount' in d:
            o.fine_amount = d['fine_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pid' in d:
            o.pid = d['pid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


