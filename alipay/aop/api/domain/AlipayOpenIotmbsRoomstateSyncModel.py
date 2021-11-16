#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsRoomstateSyncModel(object):

    def __init__(self):
        self._dev_id = None
        self._project_id = None
        self._room_state = None

    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def room_state(self):
        return self._room_state

    @room_state.setter
    def room_state(self, value):
        self._room_state = value


    def to_alipay_dict(self):
        params = dict()
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.room_state:
            if hasattr(self.room_state, 'to_alipay_dict'):
                params['room_state'] = self.room_state.to_alipay_dict()
            else:
                params['room_state'] = self.room_state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsRoomstateSyncModel()
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'room_state' in d:
            o.room_state = d['room_state']
        return o


