#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointPointprodBudgetlibCreateModel(object):

    def __init__(self):
        self._amount = None
        self._budget_name = None
        self._contract_pid = None
        self._end_time = None
        self._fund_source = None
        self._memo = None
        self._operate_channel = None
        self._operator = None
        self._order_no = None
        self._point_lib_id = None
        self._start_time = None
        self._use_settle_tool = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def point_lib_id(self):
        return self._point_lib_id

    @point_lib_id.setter
    def point_lib_id(self, value):
        self._point_lib_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def use_settle_tool(self):
        return self._use_settle_tool

    @use_settle_tool.setter
    def use_settle_tool(self, value):
        self._use_settle_tool = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
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
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.point_lib_id:
            if hasattr(self.point_lib_id, 'to_alipay_dict'):
                params['point_lib_id'] = self.point_lib_id.to_alipay_dict()
            else:
                params['point_lib_id'] = self.point_lib_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.use_settle_tool:
            if hasattr(self.use_settle_tool, 'to_alipay_dict'):
                params['use_settle_tool'] = self.use_settle_tool.to_alipay_dict()
            else:
                params['use_settle_tool'] = self.use_settle_tool
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointPointprodBudgetlibCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'budget_name' in d:
            o.budget_name = d['budget_name']
        if 'contract_pid' in d:
            o.contract_pid = d['contract_pid']
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
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'point_lib_id' in d:
            o.point_lib_id = d['point_lib_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'use_settle_tool' in d:
            o.use_settle_tool = d['use_settle_tool']
        return o


