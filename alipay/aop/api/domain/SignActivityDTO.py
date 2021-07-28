#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignActivityDTO(object):

    def __init__(self):
        self._activity_end_time = None
        self._activity_entry_time = None
        self._activity_id = None
        self._activity_name = None
        self._activity_start_time = None
        self._activity_tag_name = None
        self._activity_type = None

    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_entry_time(self):
        return self._activity_entry_time

    @activity_entry_time.setter
    def activity_entry_time(self, value):
        self._activity_entry_time = value
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
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def activity_tag_name(self):
        return self._activity_tag_name

    @activity_tag_name.setter
    def activity_tag_name(self, value):
        self._activity_tag_name = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_end_time:
            if hasattr(self.activity_end_time, 'to_alipay_dict'):
                params['activity_end_time'] = self.activity_end_time.to_alipay_dict()
            else:
                params['activity_end_time'] = self.activity_end_time
        if self.activity_entry_time:
            if hasattr(self.activity_entry_time, 'to_alipay_dict'):
                params['activity_entry_time'] = self.activity_entry_time.to_alipay_dict()
            else:
                params['activity_entry_time'] = self.activity_entry_time
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
        if self.activity_start_time:
            if hasattr(self.activity_start_time, 'to_alipay_dict'):
                params['activity_start_time'] = self.activity_start_time.to_alipay_dict()
            else:
                params['activity_start_time'] = self.activity_start_time
        if self.activity_tag_name:
            if hasattr(self.activity_tag_name, 'to_alipay_dict'):
                params['activity_tag_name'] = self.activity_tag_name.to_alipay_dict()
            else:
                params['activity_tag_name'] = self.activity_tag_name
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignActivityDTO()
        if 'activity_end_time' in d:
            o.activity_end_time = d['activity_end_time']
        if 'activity_entry_time' in d:
            o.activity_entry_time = d['activity_entry_time']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_start_time' in d:
            o.activity_start_time = d['activity_start_time']
        if 'activity_tag_name' in d:
            o.activity_tag_name = d['activity_tag_name']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        return o


