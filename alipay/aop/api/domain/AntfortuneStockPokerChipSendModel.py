#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Kv import Kv


class AntfortuneStockPokerChipSendModel(object):

    def __init__(self):
        self._amount = None
        self._campaign_id = None
        self._chip_code = None
        self._open_id = None
        self._out_biz_no = None
        self._param = None
        self._trigger_time = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def chip_code(self):
        return self._chip_code

    @chip_code.setter
    def chip_code(self, value):
        self._chip_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        if isinstance(value, list):
            self._param = list()
            for i in value:
                if isinstance(i, Kv):
                    self._param.append(i)
                else:
                    self._param.append(Kv.from_alipay_dict(i))
    @property
    def trigger_time(self):
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, value):
        self._trigger_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.chip_code:
            if hasattr(self.chip_code, 'to_alipay_dict'):
                params['chip_code'] = self.chip_code.to_alipay_dict()
            else:
                params['chip_code'] = self.chip_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.param:
            if isinstance(self.param, list):
                for i in range(0, len(self.param)):
                    element = self.param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param[i] = element.to_alipay_dict()
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.trigger_time:
            if hasattr(self.trigger_time, 'to_alipay_dict'):
                params['trigger_time'] = self.trigger_time.to_alipay_dict()
            else:
                params['trigger_time'] = self.trigger_time
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
        o = AntfortuneStockPokerChipSendModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'chip_code' in d:
            o.chip_code = d['chip_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'param' in d:
            o.param = d['param']
        if 'trigger_time' in d:
            o.trigger_time = d['trigger_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


