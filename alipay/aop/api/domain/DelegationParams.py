#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DelegationParams(object):

    def __init__(self):
        self._delegation_desc = None
        self._delegation_tag = None
        self._external_delegation_id = None
        self._max_total_amount = None
        self._times_limit = None
        self._times_timit = None
        self._validity_end_time = None
        self._validity_start_time = None

    @property
    def delegation_desc(self):
        return self._delegation_desc

    @delegation_desc.setter
    def delegation_desc(self, value):
        self._delegation_desc = value
    @property
    def delegation_tag(self):
        return self._delegation_tag

    @delegation_tag.setter
    def delegation_tag(self, value):
        self._delegation_tag = value
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value
    @property
    def max_total_amount(self):
        return self._max_total_amount

    @max_total_amount.setter
    def max_total_amount(self, value):
        self._max_total_amount = value
    @property
    def times_limit(self):
        return self._times_limit

    @times_limit.setter
    def times_limit(self, value):
        self._times_limit = value
    @property
    def times_timit(self):
        return self._times_timit

    @times_timit.setter
    def times_timit(self, value):
        self._times_timit = value
    @property
    def validity_end_time(self):
        return self._validity_end_time

    @validity_end_time.setter
    def validity_end_time(self, value):
        self._validity_end_time = value
    @property
    def validity_start_time(self):
        return self._validity_start_time

    @validity_start_time.setter
    def validity_start_time(self, value):
        self._validity_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.delegation_desc:
            if hasattr(self.delegation_desc, 'to_alipay_dict'):
                params['delegation_desc'] = self.delegation_desc.to_alipay_dict()
            else:
                params['delegation_desc'] = self.delegation_desc
        if self.delegation_tag:
            if hasattr(self.delegation_tag, 'to_alipay_dict'):
                params['delegation_tag'] = self.delegation_tag.to_alipay_dict()
            else:
                params['delegation_tag'] = self.delegation_tag
        if self.external_delegation_id:
            if hasattr(self.external_delegation_id, 'to_alipay_dict'):
                params['external_delegation_id'] = self.external_delegation_id.to_alipay_dict()
            else:
                params['external_delegation_id'] = self.external_delegation_id
        if self.max_total_amount:
            if hasattr(self.max_total_amount, 'to_alipay_dict'):
                params['max_total_amount'] = self.max_total_amount.to_alipay_dict()
            else:
                params['max_total_amount'] = self.max_total_amount
        if self.times_limit:
            if hasattr(self.times_limit, 'to_alipay_dict'):
                params['times_limit'] = self.times_limit.to_alipay_dict()
            else:
                params['times_limit'] = self.times_limit
        if self.times_timit:
            if hasattr(self.times_timit, 'to_alipay_dict'):
                params['times_timit'] = self.times_timit.to_alipay_dict()
            else:
                params['times_timit'] = self.times_timit
        if self.validity_end_time:
            if hasattr(self.validity_end_time, 'to_alipay_dict'):
                params['validity_end_time'] = self.validity_end_time.to_alipay_dict()
            else:
                params['validity_end_time'] = self.validity_end_time
        if self.validity_start_time:
            if hasattr(self.validity_start_time, 'to_alipay_dict'):
                params['validity_start_time'] = self.validity_start_time.to_alipay_dict()
            else:
                params['validity_start_time'] = self.validity_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DelegationParams()
        if 'delegation_desc' in d:
            o.delegation_desc = d['delegation_desc']
        if 'delegation_tag' in d:
            o.delegation_tag = d['delegation_tag']
        if 'external_delegation_id' in d:
            o.external_delegation_id = d['external_delegation_id']
        if 'max_total_amount' in d:
            o.max_total_amount = d['max_total_amount']
        if 'times_limit' in d:
            o.times_limit = d['times_limit']
        if 'times_timit' in d:
            o.times_timit = d['times_timit']
        if 'validity_end_time' in d:
            o.validity_end_time = d['validity_end_time']
        if 'validity_start_time' in d:
            o.validity_start_time = d['validity_start_time']
        return o


