#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ISPTaskInfo(object):

    def __init__(self):
        self._biz_ids = None
        self._create_time = None
        self._end_time = None
        self._file_id = None
        self._modify_time = None
        self._plan_id = None
        self._plan_name = None
        self._priority = None
        self._space_code = None
        self._start_time = None
        self._status_code = None

    @property
    def biz_ids(self):
        return self._biz_ids

    @biz_ids.setter
    def biz_ids(self, value):
        if isinstance(value, list):
            self._biz_ids = list()
            for i in value:
                self._biz_ids.append(i)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
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
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ids:
            if isinstance(self.biz_ids, list):
                for i in range(0, len(self.biz_ids)):
                    element = self.biz_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_ids[i] = element.to_alipay_dict()
            if hasattr(self.biz_ids, 'to_alipay_dict'):
                params['biz_ids'] = self.biz_ids.to_alipay_dict()
            else:
                params['biz_ids'] = self.biz_ids
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
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
        if self.space_code:
            if hasattr(self.space_code, 'to_alipay_dict'):
                params['space_code'] = self.space_code.to_alipay_dict()
            else:
                params['space_code'] = self.space_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ISPTaskInfo()
        if 'biz_ids' in d:
            o.biz_ids = d['biz_ids']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'priority' in d:
            o.priority = d['priority']
        if 'space_code' in d:
            o.space_code = d['space_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status_code' in d:
            o.status_code = d['status_code']
        return o


