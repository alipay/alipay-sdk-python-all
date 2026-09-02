#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzSdkTimeLagDTOOne(object):

    def __init__(self):
        self._event_identifier = None
        self._event_name = None
        self._event_occur_time = None
        self._event_type = None
        self._origin_gmt_create = None
        self._registration_no = None
        self._remind_content = None
        self._time_difference = None

    @property
    def event_identifier(self):
        return self._event_identifier

    @event_identifier.setter
    def event_identifier(self, value):
        self._event_identifier = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def event_occur_time(self):
        return self._event_occur_time

    @event_occur_time.setter
    def event_occur_time(self, value):
        self._event_occur_time = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def origin_gmt_create(self):
        return self._origin_gmt_create

    @origin_gmt_create.setter
    def origin_gmt_create(self, value):
        self._origin_gmt_create = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def remind_content(self):
        return self._remind_content

    @remind_content.setter
    def remind_content(self, value):
        self._remind_content = value
    @property
    def time_difference(self):
        return self._time_difference

    @time_difference.setter
    def time_difference(self, value):
        self._time_difference = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_identifier:
            if hasattr(self.event_identifier, 'to_alipay_dict'):
                params['event_identifier'] = self.event_identifier.to_alipay_dict()
            else:
                params['event_identifier'] = self.event_identifier
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.event_occur_time:
            if hasattr(self.event_occur_time, 'to_alipay_dict'):
                params['event_occur_time'] = self.event_occur_time.to_alipay_dict()
            else:
                params['event_occur_time'] = self.event_occur_time
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.origin_gmt_create:
            if hasattr(self.origin_gmt_create, 'to_alipay_dict'):
                params['origin_gmt_create'] = self.origin_gmt_create.to_alipay_dict()
            else:
                params['origin_gmt_create'] = self.origin_gmt_create
        if self.registration_no:
            if hasattr(self.registration_no, 'to_alipay_dict'):
                params['registration_no'] = self.registration_no.to_alipay_dict()
            else:
                params['registration_no'] = self.registration_no
        if self.remind_content:
            if hasattr(self.remind_content, 'to_alipay_dict'):
                params['remind_content'] = self.remind_content.to_alipay_dict()
            else:
                params['remind_content'] = self.remind_content
        if self.time_difference:
            if hasattr(self.time_difference, 'to_alipay_dict'):
                params['time_difference'] = self.time_difference.to_alipay_dict()
            else:
                params['time_difference'] = self.time_difference
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzSdkTimeLagDTOOne()
        if 'event_identifier' in d:
            o.event_identifier = d['event_identifier']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'event_occur_time' in d:
            o.event_occur_time = d['event_occur_time']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'origin_gmt_create' in d:
            o.origin_gmt_create = d['origin_gmt_create']
        if 'registration_no' in d:
            o.registration_no = d['registration_no']
        if 'remind_content' in d:
            o.remind_content = d['remind_content']
        if 'time_difference' in d:
            o.time_difference = d['time_difference']
        return o


