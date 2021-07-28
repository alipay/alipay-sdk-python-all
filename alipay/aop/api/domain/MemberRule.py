#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GrouponRule import GrouponRule


class MemberRule(object):

    def __init__(self):
        self._appoint_date = None
        self._auto_settlement_time = None
        self._fix_date = None
        self._freeze_amount = None
        self._groupon_rule = None
        self._guarantee_amount = None
        self._member_period = None
        self._min_consumer_amount = None
        self._min_consumer_times = None
        self._original_amount = None
        self._period_mode = None
        self._promise_condition = None
        self._promise_type = None
        self._promise_type_desc = None
        self._settlement_type = None
        self._store_amount = None

    @property
    def appoint_date(self):
        return self._appoint_date

    @appoint_date.setter
    def appoint_date(self, value):
        self._appoint_date = value
    @property
    def auto_settlement_time(self):
        return self._auto_settlement_time

    @auto_settlement_time.setter
    def auto_settlement_time(self, value):
        self._auto_settlement_time = value
    @property
    def fix_date(self):
        return self._fix_date

    @fix_date.setter
    def fix_date(self, value):
        self._fix_date = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def groupon_rule(self):
        return self._groupon_rule

    @groupon_rule.setter
    def groupon_rule(self, value):
        if isinstance(value, GrouponRule):
            self._groupon_rule = value
        else:
            self._groupon_rule = GrouponRule.from_alipay_dict(value)
    @property
    def guarantee_amount(self):
        return self._guarantee_amount

    @guarantee_amount.setter
    def guarantee_amount(self, value):
        self._guarantee_amount = value
    @property
    def member_period(self):
        return self._member_period

    @member_period.setter
    def member_period(self, value):
        self._member_period = value
    @property
    def min_consumer_amount(self):
        return self._min_consumer_amount

    @min_consumer_amount.setter
    def min_consumer_amount(self, value):
        self._min_consumer_amount = value
    @property
    def min_consumer_times(self):
        return self._min_consumer_times

    @min_consumer_times.setter
    def min_consumer_times(self, value):
        self._min_consumer_times = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def period_mode(self):
        return self._period_mode

    @period_mode.setter
    def period_mode(self, value):
        self._period_mode = value
    @property
    def promise_condition(self):
        return self._promise_condition

    @promise_condition.setter
    def promise_condition(self, value):
        self._promise_condition = value
    @property
    def promise_type(self):
        return self._promise_type

    @promise_type.setter
    def promise_type(self, value):
        self._promise_type = value
    @property
    def promise_type_desc(self):
        return self._promise_type_desc

    @promise_type_desc.setter
    def promise_type_desc(self, value):
        self._promise_type_desc = value
    @property
    def settlement_type(self):
        return self._settlement_type

    @settlement_type.setter
    def settlement_type(self, value):
        self._settlement_type = value
    @property
    def store_amount(self):
        return self._store_amount

    @store_amount.setter
    def store_amount(self, value):
        self._store_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_date:
            if hasattr(self.appoint_date, 'to_alipay_dict'):
                params['appoint_date'] = self.appoint_date.to_alipay_dict()
            else:
                params['appoint_date'] = self.appoint_date
        if self.auto_settlement_time:
            if hasattr(self.auto_settlement_time, 'to_alipay_dict'):
                params['auto_settlement_time'] = self.auto_settlement_time.to_alipay_dict()
            else:
                params['auto_settlement_time'] = self.auto_settlement_time
        if self.fix_date:
            if hasattr(self.fix_date, 'to_alipay_dict'):
                params['fix_date'] = self.fix_date.to_alipay_dict()
            else:
                params['fix_date'] = self.fix_date
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.groupon_rule:
            if hasattr(self.groupon_rule, 'to_alipay_dict'):
                params['groupon_rule'] = self.groupon_rule.to_alipay_dict()
            else:
                params['groupon_rule'] = self.groupon_rule
        if self.guarantee_amount:
            if hasattr(self.guarantee_amount, 'to_alipay_dict'):
                params['guarantee_amount'] = self.guarantee_amount.to_alipay_dict()
            else:
                params['guarantee_amount'] = self.guarantee_amount
        if self.member_period:
            if hasattr(self.member_period, 'to_alipay_dict'):
                params['member_period'] = self.member_period.to_alipay_dict()
            else:
                params['member_period'] = self.member_period
        if self.min_consumer_amount:
            if hasattr(self.min_consumer_amount, 'to_alipay_dict'):
                params['min_consumer_amount'] = self.min_consumer_amount.to_alipay_dict()
            else:
                params['min_consumer_amount'] = self.min_consumer_amount
        if self.min_consumer_times:
            if hasattr(self.min_consumer_times, 'to_alipay_dict'):
                params['min_consumer_times'] = self.min_consumer_times.to_alipay_dict()
            else:
                params['min_consumer_times'] = self.min_consumer_times
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.period_mode:
            if hasattr(self.period_mode, 'to_alipay_dict'):
                params['period_mode'] = self.period_mode.to_alipay_dict()
            else:
                params['period_mode'] = self.period_mode
        if self.promise_condition:
            if hasattr(self.promise_condition, 'to_alipay_dict'):
                params['promise_condition'] = self.promise_condition.to_alipay_dict()
            else:
                params['promise_condition'] = self.promise_condition
        if self.promise_type:
            if hasattr(self.promise_type, 'to_alipay_dict'):
                params['promise_type'] = self.promise_type.to_alipay_dict()
            else:
                params['promise_type'] = self.promise_type
        if self.promise_type_desc:
            if hasattr(self.promise_type_desc, 'to_alipay_dict'):
                params['promise_type_desc'] = self.promise_type_desc.to_alipay_dict()
            else:
                params['promise_type_desc'] = self.promise_type_desc
        if self.settlement_type:
            if hasattr(self.settlement_type, 'to_alipay_dict'):
                params['settlement_type'] = self.settlement_type.to_alipay_dict()
            else:
                params['settlement_type'] = self.settlement_type
        if self.store_amount:
            if hasattr(self.store_amount, 'to_alipay_dict'):
                params['store_amount'] = self.store_amount.to_alipay_dict()
            else:
                params['store_amount'] = self.store_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberRule()
        if 'appoint_date' in d:
            o.appoint_date = d['appoint_date']
        if 'auto_settlement_time' in d:
            o.auto_settlement_time = d['auto_settlement_time']
        if 'fix_date' in d:
            o.fix_date = d['fix_date']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'groupon_rule' in d:
            o.groupon_rule = d['groupon_rule']
        if 'guarantee_amount' in d:
            o.guarantee_amount = d['guarantee_amount']
        if 'member_period' in d:
            o.member_period = d['member_period']
        if 'min_consumer_amount' in d:
            o.min_consumer_amount = d['min_consumer_amount']
        if 'min_consumer_times' in d:
            o.min_consumer_times = d['min_consumer_times']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'period_mode' in d:
            o.period_mode = d['period_mode']
        if 'promise_condition' in d:
            o.promise_condition = d['promise_condition']
        if 'promise_type' in d:
            o.promise_type = d['promise_type']
        if 'promise_type_desc' in d:
            o.promise_type_desc = d['promise_type_desc']
        if 'settlement_type' in d:
            o.settlement_type = d['settlement_type']
        if 'store_amount' in d:
            o.store_amount = d['store_amount']
        return o


