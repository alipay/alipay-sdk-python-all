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
        self._creator_open_id = None
        self._date = None
        self._end_date = None
        self._fund_plan_id = None
        self._incremental_amount = None
        self._initial_amount = None
        self._next_execution = None
        self._out_biz_no = None
        self._payer_account = None
        self._plan_mode = None
        self._plan_times = None
        self._remark = None
        self._start_date = None
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
    def creator_open_id(self):
        return self._creator_open_id

    @creator_open_id.setter
    def creator_open_id(self, value):
        self._creator_open_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def fund_plan_id(self):
        return self._fund_plan_id

    @fund_plan_id.setter
    def fund_plan_id(self, value):
        self._fund_plan_id = value
    @property
    def incremental_amount(self):
        return self._incremental_amount

    @incremental_amount.setter
    def incremental_amount(self, value):
        self._incremental_amount = value
    @property
    def initial_amount(self):
        return self._initial_amount

    @initial_amount.setter
    def initial_amount(self, value):
        self._initial_amount = value
    @property
    def next_execution(self):
        return self._next_execution

    @next_execution.setter
    def next_execution(self, value):
        self._next_execution = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
    def plan_mode(self):
        return self._plan_mode

    @plan_mode.setter
    def plan_mode(self, value):
        self._plan_mode = value
    @property
    def plan_times(self):
        return self._plan_times

    @plan_times.setter
    def plan_times(self, value):
        self._plan_times = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
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
        if self.creator_open_id:
            if hasattr(self.creator_open_id, 'to_alipay_dict'):
                params['creator_open_id'] = self.creator_open_id.to_alipay_dict()
            else:
                params['creator_open_id'] = self.creator_open_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.fund_plan_id:
            if hasattr(self.fund_plan_id, 'to_alipay_dict'):
                params['fund_plan_id'] = self.fund_plan_id.to_alipay_dict()
            else:
                params['fund_plan_id'] = self.fund_plan_id
        if self.incremental_amount:
            if hasattr(self.incremental_amount, 'to_alipay_dict'):
                params['incremental_amount'] = self.incremental_amount.to_alipay_dict()
            else:
                params['incremental_amount'] = self.incremental_amount
        if self.initial_amount:
            if hasattr(self.initial_amount, 'to_alipay_dict'):
                params['initial_amount'] = self.initial_amount.to_alipay_dict()
            else:
                params['initial_amount'] = self.initial_amount
        if self.next_execution:
            if hasattr(self.next_execution, 'to_alipay_dict'):
                params['next_execution'] = self.next_execution.to_alipay_dict()
            else:
                params['next_execution'] = self.next_execution
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
        if self.plan_mode:
            if hasattr(self.plan_mode, 'to_alipay_dict'):
                params['plan_mode'] = self.plan_mode.to_alipay_dict()
            else:
                params['plan_mode'] = self.plan_mode
        if self.plan_times:
            if hasattr(self.plan_times, 'to_alipay_dict'):
                params['plan_times'] = self.plan_times.to_alipay_dict()
            else:
                params['plan_times'] = self.plan_times
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
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
        if 'creator_open_id' in d:
            o.creator_open_id = d['creator_open_id']
        if 'date' in d:
            o.date = d['date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'fund_plan_id' in d:
            o.fund_plan_id = d['fund_plan_id']
        if 'incremental_amount' in d:
            o.incremental_amount = d['incremental_amount']
        if 'initial_amount' in d:
            o.initial_amount = d['initial_amount']
        if 'next_execution' in d:
            o.next_execution = d['next_execution']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'plan_mode' in d:
            o.plan_mode = d['plan_mode']
        if 'plan_times' in d:
            o.plan_times = d['plan_times']
        if 'remark' in d:
            o.remark = d['remark']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


