#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketInfo(object):

    def __init__(self):
        self._activity_icon = None
        self._activity_id = None
        self._activity_record = None
        self._activity_url = None
        self._effective_end = None
        self._effective_start = None
        self._last_platform = None
        self._last_store_id = None
        self._priority_booth = None
        self._status = None

    @property
    def activity_icon(self):
        return self._activity_icon

    @activity_icon.setter
    def activity_icon(self, value):
        self._activity_icon = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_record(self):
        return self._activity_record

    @activity_record.setter
    def activity_record(self, value):
        self._activity_record = value
    @property
    def activity_url(self):
        return self._activity_url

    @activity_url.setter
    def activity_url(self, value):
        self._activity_url = value
    @property
    def effective_end(self):
        return self._effective_end

    @effective_end.setter
    def effective_end(self, value):
        self._effective_end = value
    @property
    def effective_start(self):
        return self._effective_start

    @effective_start.setter
    def effective_start(self, value):
        self._effective_start = value
    @property
    def last_platform(self):
        return self._last_platform

    @last_platform.setter
    def last_platform(self, value):
        self._last_platform = value
    @property
    def last_store_id(self):
        return self._last_store_id

    @last_store_id.setter
    def last_store_id(self, value):
        self._last_store_id = value
    @property
    def priority_booth(self):
        return self._priority_booth

    @priority_booth.setter
    def priority_booth(self, value):
        self._priority_booth = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_icon:
            if hasattr(self.activity_icon, 'to_alipay_dict'):
                params['activity_icon'] = self.activity_icon.to_alipay_dict()
            else:
                params['activity_icon'] = self.activity_icon
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_record:
            if hasattr(self.activity_record, 'to_alipay_dict'):
                params['activity_record'] = self.activity_record.to_alipay_dict()
            else:
                params['activity_record'] = self.activity_record
        if self.activity_url:
            if hasattr(self.activity_url, 'to_alipay_dict'):
                params['activity_url'] = self.activity_url.to_alipay_dict()
            else:
                params['activity_url'] = self.activity_url
        if self.effective_end:
            if hasattr(self.effective_end, 'to_alipay_dict'):
                params['effective_end'] = self.effective_end.to_alipay_dict()
            else:
                params['effective_end'] = self.effective_end
        if self.effective_start:
            if hasattr(self.effective_start, 'to_alipay_dict'):
                params['effective_start'] = self.effective_start.to_alipay_dict()
            else:
                params['effective_start'] = self.effective_start
        if self.last_platform:
            if hasattr(self.last_platform, 'to_alipay_dict'):
                params['last_platform'] = self.last_platform.to_alipay_dict()
            else:
                params['last_platform'] = self.last_platform
        if self.last_store_id:
            if hasattr(self.last_store_id, 'to_alipay_dict'):
                params['last_store_id'] = self.last_store_id.to_alipay_dict()
            else:
                params['last_store_id'] = self.last_store_id
        if self.priority_booth:
            if hasattr(self.priority_booth, 'to_alipay_dict'):
                params['priority_booth'] = self.priority_booth.to_alipay_dict()
            else:
                params['priority_booth'] = self.priority_booth
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketInfo()
        if 'activity_icon' in d:
            o.activity_icon = d['activity_icon']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_record' in d:
            o.activity_record = d['activity_record']
        if 'activity_url' in d:
            o.activity_url = d['activity_url']
        if 'effective_end' in d:
            o.effective_end = d['effective_end']
        if 'effective_start' in d:
            o.effective_start = d['effective_start']
        if 'last_platform' in d:
            o.last_platform = d['last_platform']
        if 'last_store_id' in d:
            o.last_store_id = d['last_store_id']
        if 'priority_booth' in d:
            o.priority_booth = d['priority_booth']
        if 'status' in d:
            o.status = d['status']
        return o


