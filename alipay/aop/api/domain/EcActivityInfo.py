#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcActivityInfo(object):

    def __init__(self):
        self._activity_id = None
        self._end_date = None
        self._promotion_describe = None
        self._promotion_discount = None
        self._promotion_duration = None
        self._promotion_type = None
        self._start_date = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def promotion_describe(self):
        return self._promotion_describe

    @promotion_describe.setter
    def promotion_describe(self, value):
        self._promotion_describe = value
    @property
    def promotion_discount(self):
        return self._promotion_discount

    @promotion_discount.setter
    def promotion_discount(self, value):
        self._promotion_discount = value
    @property
    def promotion_duration(self):
        return self._promotion_duration

    @promotion_duration.setter
    def promotion_duration(self, value):
        self._promotion_duration = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.promotion_describe:
            if hasattr(self.promotion_describe, 'to_alipay_dict'):
                params['promotion_describe'] = self.promotion_describe.to_alipay_dict()
            else:
                params['promotion_describe'] = self.promotion_describe
        if self.promotion_discount:
            if hasattr(self.promotion_discount, 'to_alipay_dict'):
                params['promotion_discount'] = self.promotion_discount.to_alipay_dict()
            else:
                params['promotion_discount'] = self.promotion_discount
        if self.promotion_duration:
            if hasattr(self.promotion_duration, 'to_alipay_dict'):
                params['promotion_duration'] = self.promotion_duration.to_alipay_dict()
            else:
                params['promotion_duration'] = self.promotion_duration
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcActivityInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'promotion_describe' in d:
            o.promotion_describe = d['promotion_describe']
        if 'promotion_discount' in d:
            o.promotion_discount = d['promotion_discount']
        if 'promotion_duration' in d:
            o.promotion_duration = d['promotion_duration']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


