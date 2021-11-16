#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingOrderPromo(object):

    def __init__(self):
        self._agent_pid = None

    @property
    def agent_pid(self):
        return self._agent_pid

    @agent_pid.setter
    def agent_pid(self, value):
        self._agent_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_pid:
            if hasattr(self.agent_pid, 'to_alipay_dict'):
                params['agent_pid'] = self.agent_pid.to_alipay_dict()
            else:
                params['agent_pid'] = self.agent_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingOrderPromo()
        if 'agent_pid' in d:
            o.agent_pid = d['agent_pid']
        return o


