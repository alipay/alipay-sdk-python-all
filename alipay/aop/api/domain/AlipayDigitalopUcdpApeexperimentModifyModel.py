#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalopUcdpApeexperimentModifyModel(object):

    def __init__(self):
        self._action = None
        self._flow_rate = None
        self._project_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def flow_rate(self):
        return self._flow_rate

    @flow_rate.setter
    def flow_rate(self, value):
        self._flow_rate = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.flow_rate:
            if hasattr(self.flow_rate, 'to_alipay_dict'):
                params['flow_rate'] = self.flow_rate.to_alipay_dict()
            else:
                params['flow_rate'] = self.flow_rate
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
        o = AlipayDigitalopUcdpApeexperimentModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'flow_rate' in d:
            o.flow_rate = d['flow_rate']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


