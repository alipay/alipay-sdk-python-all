#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReassignNumberResult(object):

    def __init__(self):
        self._pid = None
        self._reassign_suspected = None
        self._reassign_time = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def reassign_suspected(self):
        return self._reassign_suspected

    @reassign_suspected.setter
    def reassign_suspected(self, value):
        self._reassign_suspected = value
    @property
    def reassign_time(self):
        return self._reassign_time

    @reassign_time.setter
    def reassign_time(self, value):
        self._reassign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.reassign_suspected:
            if hasattr(self.reassign_suspected, 'to_alipay_dict'):
                params['reassign_suspected'] = self.reassign_suspected.to_alipay_dict()
            else:
                params['reassign_suspected'] = self.reassign_suspected
        if self.reassign_time:
            if hasattr(self.reassign_time, 'to_alipay_dict'):
                params['reassign_time'] = self.reassign_time.to_alipay_dict()
            else:
                params['reassign_time'] = self.reassign_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReassignNumberResult()
        if 'pid' in d:
            o.pid = d['pid']
        if 'reassign_suspected' in d:
            o.reassign_suspected = d['reassign_suspected']
        if 'reassign_time' in d:
            o.reassign_time = d['reassign_time']
        return o


