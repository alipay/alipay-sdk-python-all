#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountTypeData import AmountTypeData
from alipay.aop.api.domain.TaskTypeData import TaskTypeData


class ZhimaCreditPeZmgoCumulationSyncModel(object):

    def __init__(self):
        self._agreement_no = None
        self._amount_type_data = None
        self._biz_action = None
        self._biz_time = None
        self._cumulate_data_type = None
        self._ext_info = None
        self._has_alipay_trade = None
        self._out_biz_no = None
        self._partner_id = None
        self._pay_out_biz_no = None
        self._request_from = None
        self._task_type_data = None
        self._user_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def amount_type_data(self):
        return self._amount_type_data

    @amount_type_data.setter
    def amount_type_data(self, value):
        if isinstance(value, AmountTypeData):
            self._amount_type_data = value
        else:
            self._amount_type_data = AmountTypeData.from_alipay_dict(value)
    @property
    def biz_action(self):
        return self._biz_action

    @biz_action.setter
    def biz_action(self, value):
        self._biz_action = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def cumulate_data_type(self):
        return self._cumulate_data_type

    @cumulate_data_type.setter
    def cumulate_data_type(self, value):
        self._cumulate_data_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def has_alipay_trade(self):
        return self._has_alipay_trade

    @has_alipay_trade.setter
    def has_alipay_trade(self, value):
        self._has_alipay_trade = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_out_biz_no(self):
        return self._pay_out_biz_no

    @pay_out_biz_no.setter
    def pay_out_biz_no(self, value):
        self._pay_out_biz_no = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def task_type_data(self):
        return self._task_type_data

    @task_type_data.setter
    def task_type_data(self, value):
        if isinstance(value, TaskTypeData):
            self._task_type_data = value
        else:
            self._task_type_data = TaskTypeData.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.amount_type_data:
            if hasattr(self.amount_type_data, 'to_alipay_dict'):
                params['amount_type_data'] = self.amount_type_data.to_alipay_dict()
            else:
                params['amount_type_data'] = self.amount_type_data
        if self.biz_action:
            if hasattr(self.biz_action, 'to_alipay_dict'):
                params['biz_action'] = self.biz_action.to_alipay_dict()
            else:
                params['biz_action'] = self.biz_action
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.cumulate_data_type:
            if hasattr(self.cumulate_data_type, 'to_alipay_dict'):
                params['cumulate_data_type'] = self.cumulate_data_type.to_alipay_dict()
            else:
                params['cumulate_data_type'] = self.cumulate_data_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.has_alipay_trade:
            if hasattr(self.has_alipay_trade, 'to_alipay_dict'):
                params['has_alipay_trade'] = self.has_alipay_trade.to_alipay_dict()
            else:
                params['has_alipay_trade'] = self.has_alipay_trade
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_out_biz_no:
            if hasattr(self.pay_out_biz_no, 'to_alipay_dict'):
                params['pay_out_biz_no'] = self.pay_out_biz_no.to_alipay_dict()
            else:
                params['pay_out_biz_no'] = self.pay_out_biz_no
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.task_type_data:
            if hasattr(self.task_type_data, 'to_alipay_dict'):
                params['task_type_data'] = self.task_type_data.to_alipay_dict()
            else:
                params['task_type_data'] = self.task_type_data
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
        o = ZhimaCreditPeZmgoCumulationSyncModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount_type_data' in d:
            o.amount_type_data = d['amount_type_data']
        if 'biz_action' in d:
            o.biz_action = d['biz_action']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'cumulate_data_type' in d:
            o.cumulate_data_type = d['cumulate_data_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'has_alipay_trade' in d:
            o.has_alipay_trade = d['has_alipay_trade']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_out_biz_no' in d:
            o.pay_out_biz_no = d['pay_out_biz_no']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'task_type_data' in d:
            o.task_type_data = d['task_type_data']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


