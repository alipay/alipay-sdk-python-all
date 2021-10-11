#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayerAccountDTO import PayerAccountDTO


class FundPlanDTO(object):

    def __init__(self):
        self._account_id = None
        self._amount = None
        self._calendar_type = None
        self._creator_id = None
        self._date = None
        self._fund_plan_id = None
        self._next_execution = None
        self._payer_account = None
        self._remark = None
        self._status = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, value):
        self._calendar_type = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def fund_plan_id(self):
        return self._fund_plan_id

    @fund_plan_id.setter
    def fund_plan_id(self, value):
        self._fund_plan_id = value
    @property
    def next_execution(self):
        return self._next_execution

    @next_execution.setter
    def next_execution(self, value):
        self._next_execution = value
    @property
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        if isinstance(value, PayerAccountDTO):
            self._payer_account = value
        else:
            self._payer_account = PayerAccountDTO.from_alipay_dict(value)
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


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.calendar_type:
            if hasattr(self.calendar_type, 'to_alipay_dict'):
                params['calendar_type'] = self.calendar_type.to_alipay_dict()
            else:
                params['calendar_type'] = self.calendar_type
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.fund_plan_id:
            if hasattr(self.fund_plan_id, 'to_alipay_dict'):
                params['fund_plan_id'] = self.fund_plan_id.to_alipay_dict()
            else:
                params['fund_plan_id'] = self.fund_plan_id
        if self.next_execution:
            if hasattr(self.next_execution, 'to_alipay_dict'):
                params['next_execution'] = self.next_execution.to_alipay_dict()
            else:
                params['next_execution'] = self.next_execution
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundPlanDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'calendar_type' in d:
            o.calendar_type = d['calendar_type']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'date' in d:
            o.date = d['date']
        if 'fund_plan_id' in d:
            o.fund_plan_id = d['fund_plan_id']
        if 'next_execution' in d:
            o.next_execution = d['next_execution']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        return o


