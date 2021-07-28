#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentScheduleLog(object):

    def __init__(self):
        self._agent_id = None
        self._agent_name = None
        self._create_time = None
        self._duration = None
        self._end_time = None
        self._external_user_no = None
        self._id = None
        self._last_status = None
        self._start_time = None
        self._status = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def external_user_no(self):
        return self._external_user_no

    @external_user_no.setter
    def external_user_no(self, value):
        self._external_user_no = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def last_status(self):
        return self._last_status

    @last_status.setter
    def last_status(self, value):
        self._last_status = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.external_user_no:
            if hasattr(self.external_user_no, 'to_alipay_dict'):
                params['external_user_no'] = self.external_user_no.to_alipay_dict()
            else:
                params['external_user_no'] = self.external_user_no
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.last_status:
            if hasattr(self.last_status, 'to_alipay_dict'):
                params['last_status'] = self.last_status.to_alipay_dict()
            else:
                params['last_status'] = self.last_status
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AgentScheduleLog()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'duration' in d:
            o.duration = d['duration']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'external_user_no' in d:
            o.external_user_no = d['external_user_no']
        if 'id' in d:
            o.id = d['id']
        if 'last_status' in d:
            o.last_status = d['last_status']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


