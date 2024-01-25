#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookingRule(object):

    def __init__(self):
        self._booking_rule_id = None
        self._description = None
        self._end_date = None
        self._end_hour = None
        self._max_adv_hours = None
        self._max_amount = None
        self._max_days = None
        self._min_adv_hours = None
        self._min_amount = None
        self._min_days = None
        self._start_date = None
        self._start_hour = None
        self._week_set = None

    @property
    def booking_rule_id(self):
        return self._booking_rule_id

    @booking_rule_id.setter
    def booking_rule_id(self, value):
        self._booking_rule_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, value):
        self._end_hour = value
    @property
    def max_adv_hours(self):
        return self._max_adv_hours

    @max_adv_hours.setter
    def max_adv_hours(self, value):
        self._max_adv_hours = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def max_days(self):
        return self._max_days

    @max_days.setter
    def max_days(self, value):
        self._max_days = value
    @property
    def min_adv_hours(self):
        return self._min_adv_hours

    @min_adv_hours.setter
    def min_adv_hours(self, value):
        self._min_adv_hours = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def min_days(self):
        return self._min_days

    @min_days.setter
    def min_days(self, value):
        self._min_days = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, value):
        self._start_hour = value
    @property
    def week_set(self):
        return self._week_set

    @week_set.setter
    def week_set(self, value):
        self._week_set = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_rule_id:
            if hasattr(self.booking_rule_id, 'to_alipay_dict'):
                params['booking_rule_id'] = self.booking_rule_id.to_alipay_dict()
            else:
                params['booking_rule_id'] = self.booking_rule_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_hour:
            if hasattr(self.end_hour, 'to_alipay_dict'):
                params['end_hour'] = self.end_hour.to_alipay_dict()
            else:
                params['end_hour'] = self.end_hour
        if self.max_adv_hours:
            if hasattr(self.max_adv_hours, 'to_alipay_dict'):
                params['max_adv_hours'] = self.max_adv_hours.to_alipay_dict()
            else:
                params['max_adv_hours'] = self.max_adv_hours
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.max_days:
            if hasattr(self.max_days, 'to_alipay_dict'):
                params['max_days'] = self.max_days.to_alipay_dict()
            else:
                params['max_days'] = self.max_days
        if self.min_adv_hours:
            if hasattr(self.min_adv_hours, 'to_alipay_dict'):
                params['min_adv_hours'] = self.min_adv_hours.to_alipay_dict()
            else:
                params['min_adv_hours'] = self.min_adv_hours
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.min_days:
            if hasattr(self.min_days, 'to_alipay_dict'):
                params['min_days'] = self.min_days.to_alipay_dict()
            else:
                params['min_days'] = self.min_days
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.start_hour:
            if hasattr(self.start_hour, 'to_alipay_dict'):
                params['start_hour'] = self.start_hour.to_alipay_dict()
            else:
                params['start_hour'] = self.start_hour
        if self.week_set:
            if hasattr(self.week_set, 'to_alipay_dict'):
                params['week_set'] = self.week_set.to_alipay_dict()
            else:
                params['week_set'] = self.week_set
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookingRule()
        if 'booking_rule_id' in d:
            o.booking_rule_id = d['booking_rule_id']
        if 'description' in d:
            o.description = d['description']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_hour' in d:
            o.end_hour = d['end_hour']
        if 'max_adv_hours' in d:
            o.max_adv_hours = d['max_adv_hours']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'max_days' in d:
            o.max_days = d['max_days']
        if 'min_adv_hours' in d:
            o.min_adv_hours = d['min_adv_hours']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'min_days' in d:
            o.min_days = d['min_days']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'start_hour' in d:
            o.start_hour = d['start_hour']
        if 'week_set' in d:
            o.week_set = d['week_set']
        return o


