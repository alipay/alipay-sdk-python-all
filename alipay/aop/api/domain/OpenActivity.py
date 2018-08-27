#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenActivity(object):

    def __init__(self):
        self._activity_end_date = None
        self._activity_id = None
        self._activity_name = None
        self._activity_start_date = None
        self._activity_status = None
        self._store_id = None

    @property
    def activity_end_date(self):
        return self._activity_end_date

    @activity_end_date.setter
    def activity_end_date(self, value):
        self._activity_end_date = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_start_date(self):
        return self._activity_start_date

    @activity_start_date.setter
    def activity_start_date(self, value):
        self._activity_start_date = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_end_date:
            if hasattr(self.activity_end_date, 'to_alipay_dict'):
                params['activity_end_date'] = self.activity_end_date.to_alipay_dict()
            else:
                params['activity_end_date'] = self.activity_end_date
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_start_date:
            if hasattr(self.activity_start_date, 'to_alipay_dict'):
                params['activity_start_date'] = self.activity_start_date.to_alipay_dict()
            else:
                params['activity_start_date'] = self.activity_start_date
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenActivity()
        if 'activity_end_date' in d:
            o.activity_end_date = d['activity_end_date']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_start_date' in d:
            o.activity_start_date = d['activity_start_date']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


