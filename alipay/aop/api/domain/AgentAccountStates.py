#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentAccountStates(object):

    def __init__(self):
        self._agent_id = None
        self._agent_name = None
        self._dn = None
        self._instance_id = None
        self._login_name = None
        self._state = None
        self._state_duration = None

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
    def dn(self):
        return self._dn

    @dn.setter
    def dn(self, value):
        self._dn = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def state_duration(self):
        return self._state_duration

    @state_duration.setter
    def state_duration(self, value):
        self._state_duration = value


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
        if self.dn:
            if hasattr(self.dn, 'to_alipay_dict'):
                params['dn'] = self.dn.to_alipay_dict()
            else:
                params['dn'] = self.dn
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.login_name:
            if hasattr(self.login_name, 'to_alipay_dict'):
                params['login_name'] = self.login_name.to_alipay_dict()
            else:
                params['login_name'] = self.login_name
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.state_duration:
            if hasattr(self.state_duration, 'to_alipay_dict'):
                params['state_duration'] = self.state_duration.to_alipay_dict()
            else:
                params['state_duration'] = self.state_duration
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentAccountStates()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'dn' in d:
            o.dn = d['dn']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'login_name' in d:
            o.login_name = d['login_name']
        if 'state' in d:
            o.state = d['state']
        if 'state_duration' in d:
            o.state_duration = d['state_duration']
        return o


