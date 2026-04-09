#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMarketingTaskCreateModel(object):

    def __init__(self):
        self._biz_tids = None
        self._end_time = None
        self._plan_name = None
        self._priority = None
        self._start_time = None
        self._template_id = None

    @property
    def biz_tids(self):
        return self._biz_tids

    @biz_tids.setter
    def biz_tids(self, value):
        if isinstance(value, list):
            self._biz_tids = list()
            for i in value:
                self._biz_tids.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tids:
            if isinstance(self.biz_tids, list):
                for i in range(0, len(self.biz_tids)):
                    element = self.biz_tids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_tids[i] = element.to_alipay_dict()
            if hasattr(self.biz_tids, 'to_alipay_dict'):
                params['biz_tids'] = self.biz_tids.to_alipay_dict()
            else:
                params['biz_tids'] = self.biz_tids
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMarketingTaskCreateModel()
        if 'biz_tids' in d:
            o.biz_tids = d['biz_tids']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'priority' in d:
            o.priority = d['priority']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


