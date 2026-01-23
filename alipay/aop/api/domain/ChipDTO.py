#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Kv import Kv


class ChipDTO(object):

    def __init__(self):
        self._amount = None
        self._begin_time = None
        self._campaign_code = None
        self._campaign_id = None
        self._chip_id = None
        self._end_time = None
        self._exchange_status = None
        self._issue_time = None
        self._param = None
        self._trigger_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def campaign_code(self):
        return self._campaign_code

    @campaign_code.setter
    def campaign_code(self, value):
        self._campaign_code = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def chip_id(self):
        return self._chip_id

    @chip_id.setter
    def chip_id(self, value):
        self._chip_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exchange_status(self):
        return self._exchange_status

    @exchange_status.setter
    def exchange_status(self, value):
        self._exchange_status = value
    @property
    def issue_time(self):
        return self._issue_time

    @issue_time.setter
    def issue_time(self, value):
        self._issue_time = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        if isinstance(value, Kv):
            self._param = value
        else:
            self._param = Kv.from_alipay_dict(value)
    @property
    def trigger_time(self):
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, value):
        self._trigger_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.campaign_code:
            if hasattr(self.campaign_code, 'to_alipay_dict'):
                params['campaign_code'] = self.campaign_code.to_alipay_dict()
            else:
                params['campaign_code'] = self.campaign_code
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.chip_id:
            if hasattr(self.chip_id, 'to_alipay_dict'):
                params['chip_id'] = self.chip_id.to_alipay_dict()
            else:
                params['chip_id'] = self.chip_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.exchange_status:
            if hasattr(self.exchange_status, 'to_alipay_dict'):
                params['exchange_status'] = self.exchange_status.to_alipay_dict()
            else:
                params['exchange_status'] = self.exchange_status
        if self.issue_time:
            if hasattr(self.issue_time, 'to_alipay_dict'):
                params['issue_time'] = self.issue_time.to_alipay_dict()
            else:
                params['issue_time'] = self.issue_time
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.trigger_time:
            if hasattr(self.trigger_time, 'to_alipay_dict'):
                params['trigger_time'] = self.trigger_time.to_alipay_dict()
            else:
                params['trigger_time'] = self.trigger_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChipDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'campaign_code' in d:
            o.campaign_code = d['campaign_code']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'chip_id' in d:
            o.chip_id = d['chip_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exchange_status' in d:
            o.exchange_status = d['exchange_status']
        if 'issue_time' in d:
            o.issue_time = d['issue_time']
        if 'param' in d:
            o.param = d['param']
        if 'trigger_time' in d:
            o.trigger_time = d['trigger_time']
        return o


