#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DateRuleInfo import DateRuleInfo
from alipay.aop.api.domain.HolidayRuleInfo import HolidayRuleInfo
from alipay.aop.api.domain.WeekRuleInfo import WeekRuleInfo


class VoucherUseTimeRuleInfo(object):

    def __init__(self):
        self._date_rule_info = None
        self._holiday_rule_info = None
        self._rule_type = None
        self._week_rule_info = None

    @property
    def date_rule_info(self):
        return self._date_rule_info

    @date_rule_info.setter
    def date_rule_info(self, value):
        if isinstance(value, DateRuleInfo):
            self._date_rule_info = value
        else:
            self._date_rule_info = DateRuleInfo.from_alipay_dict(value)
    @property
    def holiday_rule_info(self):
        return self._holiday_rule_info

    @holiday_rule_info.setter
    def holiday_rule_info(self, value):
        if isinstance(value, HolidayRuleInfo):
            self._holiday_rule_info = value
        else:
            self._holiday_rule_info = HolidayRuleInfo.from_alipay_dict(value)
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def week_rule_info(self):
        return self._week_rule_info

    @week_rule_info.setter
    def week_rule_info(self, value):
        if isinstance(value, WeekRuleInfo):
            self._week_rule_info = value
        else:
            self._week_rule_info = WeekRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.date_rule_info:
            if hasattr(self.date_rule_info, 'to_alipay_dict'):
                params['date_rule_info'] = self.date_rule_info.to_alipay_dict()
            else:
                params['date_rule_info'] = self.date_rule_info
        if self.holiday_rule_info:
            if hasattr(self.holiday_rule_info, 'to_alipay_dict'):
                params['holiday_rule_info'] = self.holiday_rule_info.to_alipay_dict()
            else:
                params['holiday_rule_info'] = self.holiday_rule_info
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.week_rule_info:
            if hasattr(self.week_rule_info, 'to_alipay_dict'):
                params['week_rule_info'] = self.week_rule_info.to_alipay_dict()
            else:
                params['week_rule_info'] = self.week_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseTimeRuleInfo()
        if 'date_rule_info' in d:
            o.date_rule_info = d['date_rule_info']
        if 'holiday_rule_info' in d:
            o.holiday_rule_info = d['holiday_rule_info']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'week_rule_info' in d:
            o.week_rule_info = d['week_rule_info']
        return o


