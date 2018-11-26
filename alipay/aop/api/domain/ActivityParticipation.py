#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Activity import Activity


class ActivityParticipation(object):

    def __init__(self):
        self._activity = None
        self._can_dispense = None
        self._consumed_amount = None
        self._consumed_times = None
        self._contract_no = None
        self._contract_status = None
        self._discount_amount = None
        self._expire_time = None
        self._participated = None
        self._user_id = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, Activity):
            self._activity = value
        else:
            self._activity = Activity.from_alipay_dict(value)
    @property
    def can_dispense(self):
        return self._can_dispense

    @can_dispense.setter
    def can_dispense(self, value):
        self._can_dispense = value
    @property
    def consumed_amount(self):
        return self._consumed_amount

    @consumed_amount.setter
    def consumed_amount(self, value):
        self._consumed_amount = value
    @property
    def consumed_times(self):
        return self._consumed_times

    @consumed_times.setter
    def consumed_times(self, value):
        self._consumed_times = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def participated(self):
        return self._participated

    @participated.setter
    def participated(self, value):
        self._participated = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.can_dispense:
            if hasattr(self.can_dispense, 'to_alipay_dict'):
                params['can_dispense'] = self.can_dispense.to_alipay_dict()
            else:
                params['can_dispense'] = self.can_dispense
        if self.consumed_amount:
            if hasattr(self.consumed_amount, 'to_alipay_dict'):
                params['consumed_amount'] = self.consumed_amount.to_alipay_dict()
            else:
                params['consumed_amount'] = self.consumed_amount
        if self.consumed_times:
            if hasattr(self.consumed_times, 'to_alipay_dict'):
                params['consumed_times'] = self.consumed_times.to_alipay_dict()
            else:
                params['consumed_times'] = self.consumed_times
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.participated:
            if hasattr(self.participated, 'to_alipay_dict'):
                params['participated'] = self.participated.to_alipay_dict()
            else:
                params['participated'] = self.participated
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
        o = ActivityParticipation()
        if 'activity' in d:
            o.activity = d['activity']
        if 'can_dispense' in d:
            o.can_dispense = d['can_dispense']
        if 'consumed_amount' in d:
            o.consumed_amount = d['consumed_amount']
        if 'consumed_times' in d:
            o.consumed_times = d['consumed_times']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'participated' in d:
            o.participated = d['participated']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


