#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StatesSyncPayload(object):

    def __init__(self):
        self._device_id = None
        self._online = None
        self._states = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def online(self):
        return self._online

    @online.setter
    def online(self, value):
        self._online = value
    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, value):
        self._states = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.online:
            if hasattr(self.online, 'to_alipay_dict'):
                params['online'] = self.online.to_alipay_dict()
            else:
                params['online'] = self.online
        if self.states:
            if hasattr(self.states, 'to_alipay_dict'):
                params['states'] = self.states.to_alipay_dict()
            else:
                params['states'] = self.states
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StatesSyncPayload()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'online' in d:
            o.online = d['online']
        if 'states' in d:
            o.states = d['states']
        return o


