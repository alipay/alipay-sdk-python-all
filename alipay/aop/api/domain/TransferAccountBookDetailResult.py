#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferAccountBookDetailResult(object):

    def __init__(self):
        self._account = None
        self._amount = None
        self._biz_desc = None
        self._fund_desc = None
        self._instruction_id = None
        self._memo = None
        self._order_no = None
        self._service_fee = None
        self._status = None
        self._sub_type_desc = None
        self._trans_dt = None
        self._type_desc = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def fund_desc(self):
        return self._fund_desc

    @fund_desc.setter
    def fund_desc(self, value):
        self._fund_desc = value
    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, value):
        self._service_fee = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_type_desc(self):
        return self._sub_type_desc

    @sub_type_desc.setter
    def sub_type_desc(self, value):
        self._sub_type_desc = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def type_desc(self):
        return self._type_desc

    @type_desc.setter
    def type_desc(self, value):
        self._type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_desc:
            if hasattr(self.biz_desc, 'to_alipay_dict'):
                params['biz_desc'] = self.biz_desc.to_alipay_dict()
            else:
                params['biz_desc'] = self.biz_desc
        if self.fund_desc:
            if hasattr(self.fund_desc, 'to_alipay_dict'):
                params['fund_desc'] = self.fund_desc.to_alipay_dict()
            else:
                params['fund_desc'] = self.fund_desc
        if self.instruction_id:
            if hasattr(self.instruction_id, 'to_alipay_dict'):
                params['instruction_id'] = self.instruction_id.to_alipay_dict()
            else:
                params['instruction_id'] = self.instruction_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.service_fee:
            if hasattr(self.service_fee, 'to_alipay_dict'):
                params['service_fee'] = self.service_fee.to_alipay_dict()
            else:
                params['service_fee'] = self.service_fee
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_type_desc:
            if hasattr(self.sub_type_desc, 'to_alipay_dict'):
                params['sub_type_desc'] = self.sub_type_desc.to_alipay_dict()
            else:
                params['sub_type_desc'] = self.sub_type_desc
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        if self.type_desc:
            if hasattr(self.type_desc, 'to_alipay_dict'):
                params['type_desc'] = self.type_desc.to_alipay_dict()
            else:
                params['type_desc'] = self.type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferAccountBookDetailResult()
        if 'account' in d:
            o.account = d['account']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_desc' in d:
            o.biz_desc = d['biz_desc']
        if 'fund_desc' in d:
            o.fund_desc = d['fund_desc']
        if 'instruction_id' in d:
            o.instruction_id = d['instruction_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'service_fee' in d:
            o.service_fee = d['service_fee']
        if 'status' in d:
            o.status = d['status']
        if 'sub_type_desc' in d:
            o.sub_type_desc = d['sub_type_desc']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'type_desc' in d:
            o.type_desc = d['type_desc']
        return o


