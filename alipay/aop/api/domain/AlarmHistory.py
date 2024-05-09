#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmHistory(object):

    def __init__(self):
        self._alarm_time = None
        self._duration = None
        self._id = None
        self._page_index = None
        self._page_size = None
        self._recover_time = None
        self._rule_id = None
        self._rule_name = None
        self._total = None

    @property
    def alarm_time(self):
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, value):
        self._alarm_time = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def recover_time(self):
        return self._recover_time

    @recover_time.setter
    def recover_time(self, value):
        self._recover_time = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_time:
            if hasattr(self.alarm_time, 'to_alipay_dict'):
                params['alarm_time'] = self.alarm_time.to_alipay_dict()
            else:
                params['alarm_time'] = self.alarm_time
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.recover_time:
            if hasattr(self.recover_time, 'to_alipay_dict'):
                params['recover_time'] = self.recover_time.to_alipay_dict()
            else:
                params['recover_time'] = self.recover_time
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmHistory()
        if 'alarm_time' in d:
            o.alarm_time = d['alarm_time']
        if 'duration' in d:
            o.duration = d['duration']
        if 'id' in d:
            o.id = d['id']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'recover_time' in d:
            o.recover_time = d['recover_time']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'total' in d:
            o.total = d['total']
        return o


