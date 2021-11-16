#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsDooropenresultSyncModel(object):

    def __init__(self):
        self._dev_id = None
        self._door_state = None
        self._project_id = None

    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def door_state(self):
        return self._door_state

    @door_state.setter
    def door_state(self, value):
        self._door_state = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.door_state:
            if hasattr(self.door_state, 'to_alipay_dict'):
                params['door_state'] = self.door_state.to_alipay_dict()
            else:
                params['door_state'] = self.door_state
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsDooropenresultSyncModel()
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'door_state' in d:
            o.door_state = d['door_state']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


