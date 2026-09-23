#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayDelegationTaskModifyModel(object):

    def __init__(self):
        self._agent_id = None
        self._agreement_no = None
        self._delegation_id = None
        self._pre_max_total_amount = None
        self._target_max_total_amount = None
        self._times_limit = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def pre_max_total_amount(self):
        return self._pre_max_total_amount

    @pre_max_total_amount.setter
    def pre_max_total_amount(self, value):
        self._pre_max_total_amount = value
    @property
    def target_max_total_amount(self):
        return self._target_max_total_amount

    @target_max_total_amount.setter
    def target_max_total_amount(self, value):
        self._target_max_total_amount = value
    @property
    def times_limit(self):
        return self._times_limit

    @times_limit.setter
    def times_limit(self, value):
        self._times_limit = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.delegation_id:
            if hasattr(self.delegation_id, 'to_alipay_dict'):
                params['delegation_id'] = self.delegation_id.to_alipay_dict()
            else:
                params['delegation_id'] = self.delegation_id
        if self.pre_max_total_amount:
            if hasattr(self.pre_max_total_amount, 'to_alipay_dict'):
                params['pre_max_total_amount'] = self.pre_max_total_amount.to_alipay_dict()
            else:
                params['pre_max_total_amount'] = self.pre_max_total_amount
        if self.target_max_total_amount:
            if hasattr(self.target_max_total_amount, 'to_alipay_dict'):
                params['target_max_total_amount'] = self.target_max_total_amount.to_alipay_dict()
            else:
                params['target_max_total_amount'] = self.target_max_total_amount
        if self.times_limit:
            if hasattr(self.times_limit, 'to_alipay_dict'):
                params['times_limit'] = self.times_limit.to_alipay_dict()
            else:
                params['times_limit'] = self.times_limit
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayDelegationTaskModifyModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'delegation_id' in d:
            o.delegation_id = d['delegation_id']
        if 'pre_max_total_amount' in d:
            o.pre_max_total_amount = d['pre_max_total_amount']
        if 'target_max_total_amount' in d:
            o.target_max_total_amount = d['target_max_total_amount']
        if 'times_limit' in d:
            o.times_limit = d['times_limit']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


