#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BudgetLibResult(object):

    def __init__(self):
        self._alert_money = None
        self._alert_status = None
        self._auto_delay = None
        self._balance = None
        self._budget_code = None
        self._budget_name = None
        self._contract_pid = None
        self._create_time = None
        self._delay_notice = None
        self._end_time = None
        self._fund_source = None
        self._memo = None
        self._operate_channel = None
        self._operator = None
        self._point_lib_id = None
        self._product_code = None
        self._start_time = None
        self._status = None
        self._status_code = None
        self._total_amount = None

    @property
    def alert_money(self):
        return self._alert_money

    @alert_money.setter
    def alert_money(self, value):
        self._alert_money = value
    @property
    def alert_status(self):
        return self._alert_status

    @alert_status.setter
    def alert_status(self, value):
        self._alert_status = value
    @property
    def auto_delay(self):
        return self._auto_delay

    @auto_delay.setter
    def auto_delay(self, value):
        self._auto_delay = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def budget_name(self):
        return self._budget_name

    @budget_name.setter
    def budget_name(self, value):
        self._budget_name = value
    @property
    def contract_pid(self):
        return self._contract_pid

    @contract_pid.setter
    def contract_pid(self, value):
        self._contract_pid = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def delay_notice(self):
        return self._delay_notice

    @delay_notice.setter
    def delay_notice(self, value):
        self._delay_notice = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fund_source(self):
        return self._fund_source

    @fund_source.setter
    def fund_source(self, value):
        self._fund_source = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operate_channel(self):
        return self._operate_channel

    @operate_channel.setter
    def operate_channel(self, value):
        self._operate_channel = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def point_lib_id(self):
        return self._point_lib_id

    @point_lib_id.setter
    def point_lib_id(self, value):
        self._point_lib_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_money:
            if hasattr(self.alert_money, 'to_alipay_dict'):
                params['alert_money'] = self.alert_money.to_alipay_dict()
            else:
                params['alert_money'] = self.alert_money
        if self.alert_status:
            if hasattr(self.alert_status, 'to_alipay_dict'):
                params['alert_status'] = self.alert_status.to_alipay_dict()
            else:
                params['alert_status'] = self.alert_status
        if self.auto_delay:
            if hasattr(self.auto_delay, 'to_alipay_dict'):
                params['auto_delay'] = self.auto_delay.to_alipay_dict()
            else:
                params['auto_delay'] = self.auto_delay
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.budget_code:
            if hasattr(self.budget_code, 'to_alipay_dict'):
                params['budget_code'] = self.budget_code.to_alipay_dict()
            else:
                params['budget_code'] = self.budget_code
        if self.budget_name:
            if hasattr(self.budget_name, 'to_alipay_dict'):
                params['budget_name'] = self.budget_name.to_alipay_dict()
            else:
                params['budget_name'] = self.budget_name
        if self.contract_pid:
            if hasattr(self.contract_pid, 'to_alipay_dict'):
                params['contract_pid'] = self.contract_pid.to_alipay_dict()
            else:
                params['contract_pid'] = self.contract_pid
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.delay_notice:
            if hasattr(self.delay_notice, 'to_alipay_dict'):
                params['delay_notice'] = self.delay_notice.to_alipay_dict()
            else:
                params['delay_notice'] = self.delay_notice
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fund_source:
            if hasattr(self.fund_source, 'to_alipay_dict'):
                params['fund_source'] = self.fund_source.to_alipay_dict()
            else:
                params['fund_source'] = self.fund_source
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operate_channel:
            if hasattr(self.operate_channel, 'to_alipay_dict'):
                params['operate_channel'] = self.operate_channel.to_alipay_dict()
            else:
                params['operate_channel'] = self.operate_channel
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.point_lib_id:
            if hasattr(self.point_lib_id, 'to_alipay_dict'):
                params['point_lib_id'] = self.point_lib_id.to_alipay_dict()
            else:
                params['point_lib_id'] = self.point_lib_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BudgetLibResult()
        if 'alert_money' in d:
            o.alert_money = d['alert_money']
        if 'alert_status' in d:
            o.alert_status = d['alert_status']
        if 'auto_delay' in d:
            o.auto_delay = d['auto_delay']
        if 'balance' in d:
            o.balance = d['balance']
        if 'budget_code' in d:
            o.budget_code = d['budget_code']
        if 'budget_name' in d:
            o.budget_name = d['budget_name']
        if 'contract_pid' in d:
            o.contract_pid = d['contract_pid']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'delay_notice' in d:
            o.delay_notice = d['delay_notice']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fund_source' in d:
            o.fund_source = d['fund_source']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operate_channel' in d:
            o.operate_channel = d['operate_channel']
        if 'operator' in d:
            o.operator = d['operator']
        if 'point_lib_id' in d:
            o.point_lib_id = d['point_lib_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


