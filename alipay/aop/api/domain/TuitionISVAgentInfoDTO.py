#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVAgentInfoDTO(object):

    def __init__(self):
        self._agent_sub_name = None
        self._pid = None
        self._sub_pid = None

    @property
    def agent_sub_name(self):
        return self._agent_sub_name

    @agent_sub_name.setter
    def agent_sub_name(self, value):
        self._agent_sub_name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sub_pid(self):
        return self._sub_pid

    @sub_pid.setter
    def sub_pid(self, value):
        self._sub_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_sub_name:
            if hasattr(self.agent_sub_name, 'to_alipay_dict'):
                params['agent_sub_name'] = self.agent_sub_name.to_alipay_dict()
            else:
                params['agent_sub_name'] = self.agent_sub_name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.sub_pid:
            if hasattr(self.sub_pid, 'to_alipay_dict'):
                params['sub_pid'] = self.sub_pid.to_alipay_dict()
            else:
                params['sub_pid'] = self.sub_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVAgentInfoDTO()
        if 'agent_sub_name' in d:
            o.agent_sub_name = d['agent_sub_name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'sub_pid' in d:
            o.sub_pid = d['sub_pid']
        return o


