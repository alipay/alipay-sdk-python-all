#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseQuotaInfo(object):

    def __init__(self):
        self._effective_end_date = None
        self._effective_start_date = None
        self._enterprise_id = None
        self._freeze = None
        self._owner_id = None
        self._owner_type = None
        self._quota_available = None
        self._quota_id = None
        self._quota_locked = None
        self._quota_total = None
        self._quota_used = None
        self._target_id = None
        self._target_type = None

    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def freeze(self):
        return self._freeze

    @freeze.setter
    def freeze(self, value):
        self._freeze = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def quota_available(self):
        return self._quota_available

    @quota_available.setter
    def quota_available(self, value):
        self._quota_available = value
    @property
    def quota_id(self):
        return self._quota_id

    @quota_id.setter
    def quota_id(self, value):
        self._quota_id = value
    @property
    def quota_locked(self):
        return self._quota_locked

    @quota_locked.setter
    def quota_locked(self, value):
        self._quota_locked = value
    @property
    def quota_total(self):
        return self._quota_total

    @quota_total.setter
    def quota_total(self, value):
        self._quota_total = value
    @property
    def quota_used(self):
        return self._quota_used

    @quota_used.setter
    def quota_used(self, value):
        self._quota_used = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_end_date:
            if hasattr(self.effective_end_date, 'to_alipay_dict'):
                params['effective_end_date'] = self.effective_end_date.to_alipay_dict()
            else:
                params['effective_end_date'] = self.effective_end_date
        if self.effective_start_date:
            if hasattr(self.effective_start_date, 'to_alipay_dict'):
                params['effective_start_date'] = self.effective_start_date.to_alipay_dict()
            else:
                params['effective_start_date'] = self.effective_start_date
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.freeze:
            if hasattr(self.freeze, 'to_alipay_dict'):
                params['freeze'] = self.freeze.to_alipay_dict()
            else:
                params['freeze'] = self.freeze
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.quota_available:
            if hasattr(self.quota_available, 'to_alipay_dict'):
                params['quota_available'] = self.quota_available.to_alipay_dict()
            else:
                params['quota_available'] = self.quota_available
        if self.quota_id:
            if hasattr(self.quota_id, 'to_alipay_dict'):
                params['quota_id'] = self.quota_id.to_alipay_dict()
            else:
                params['quota_id'] = self.quota_id
        if self.quota_locked:
            if hasattr(self.quota_locked, 'to_alipay_dict'):
                params['quota_locked'] = self.quota_locked.to_alipay_dict()
            else:
                params['quota_locked'] = self.quota_locked
        if self.quota_total:
            if hasattr(self.quota_total, 'to_alipay_dict'):
                params['quota_total'] = self.quota_total.to_alipay_dict()
            else:
                params['quota_total'] = self.quota_total
        if self.quota_used:
            if hasattr(self.quota_used, 'to_alipay_dict'):
                params['quota_used'] = self.quota_used.to_alipay_dict()
            else:
                params['quota_used'] = self.quota_used
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseQuotaInfo()
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'freeze' in d:
            o.freeze = d['freeze']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'quota_available' in d:
            o.quota_available = d['quota_available']
        if 'quota_id' in d:
            o.quota_id = d['quota_id']
        if 'quota_locked' in d:
            o.quota_locked = d['quota_locked']
        if 'quota_total' in d:
            o.quota_total = d['quota_total']
        if 'quota_used' in d:
            o.quota_used = d['quota_used']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


