#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmRecordSummaryItem(object):

    def __init__(self):
        self._activity_id = None
        self._activity_type = None
        self._record_date = None
        self._record_num = None
        self._record_type = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def record_num(self):
        return self._record_num

    @record_num.setter
    def record_num(self, value):
        self._record_num = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.record_num:
            if hasattr(self.record_num, 'to_alipay_dict'):
                params['record_num'] = self.record_num.to_alipay_dict()
            else:
                params['record_num'] = self.record_num
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmRecordSummaryItem()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'record_num' in d:
            o.record_num = d['record_num']
        if 'record_type' in d:
            o.record_type = d['record_type']
        return o


