#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogicalRuleItemDTO(object):

    def __init__(self):
        self._crowd_name = None
        self._ext_crowd_key = None
        self._gmt_expired_time = None
        self._schedule_type = None
        self._type = None

    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def ext_crowd_key(self):
        return self._ext_crowd_key

    @ext_crowd_key.setter
    def ext_crowd_key(self, value):
        self._ext_crowd_key = value
    @property
    def gmt_expired_time(self):
        return self._gmt_expired_time

    @gmt_expired_time.setter
    def gmt_expired_time(self, value):
        self._gmt_expired_time = value
    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, value):
        self._schedule_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.ext_crowd_key:
            if hasattr(self.ext_crowd_key, 'to_alipay_dict'):
                params['ext_crowd_key'] = self.ext_crowd_key.to_alipay_dict()
            else:
                params['ext_crowd_key'] = self.ext_crowd_key
        if self.gmt_expired_time:
            if hasattr(self.gmt_expired_time, 'to_alipay_dict'):
                params['gmt_expired_time'] = self.gmt_expired_time.to_alipay_dict()
            else:
                params['gmt_expired_time'] = self.gmt_expired_time
        if self.schedule_type:
            if hasattr(self.schedule_type, 'to_alipay_dict'):
                params['schedule_type'] = self.schedule_type.to_alipay_dict()
            else:
                params['schedule_type'] = self.schedule_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogicalRuleItemDTO()
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'ext_crowd_key' in d:
            o.ext_crowd_key = d['ext_crowd_key']
        if 'gmt_expired_time' in d:
            o.gmt_expired_time = d['gmt_expired_time']
        if 'schedule_type' in d:
            o.schedule_type = d['schedule_type']
        if 'type' in d:
            o.type = d['type']
        return o


