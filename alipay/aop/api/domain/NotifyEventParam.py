#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotifyEventParam(object):

    def __init__(self):
        self._event_config = None
        self._event_type = None
        self._page = None
        self._punch_time = None
        self._target_app_id = None
        self._work_time = None

    @property
    def event_config(self):
        return self._event_config

    @event_config.setter
    def event_config(self, value):
        self._event_config = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def punch_time(self):
        return self._punch_time

    @punch_time.setter
    def punch_time(self, value):
        self._punch_time = value
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value
    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, value):
        self._work_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_config:
            if hasattr(self.event_config, 'to_alipay_dict'):
                params['event_config'] = self.event_config.to_alipay_dict()
            else:
                params['event_config'] = self.event_config
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.punch_time:
            if hasattr(self.punch_time, 'to_alipay_dict'):
                params['punch_time'] = self.punch_time.to_alipay_dict()
            else:
                params['punch_time'] = self.punch_time
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        if self.work_time:
            if hasattr(self.work_time, 'to_alipay_dict'):
                params['work_time'] = self.work_time.to_alipay_dict()
            else:
                params['work_time'] = self.work_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NotifyEventParam()
        if 'event_config' in d:
            o.event_config = d['event_config']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'page' in d:
            o.page = d['page']
        if 'punch_time' in d:
            o.punch_time = d['punch_time']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        if 'work_time' in d:
            o.work_time = d['work_time']
        return o


