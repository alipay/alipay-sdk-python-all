#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IvrTrackingVO(object):

    def __init__(self):
        self._callee = None
        self._caller = None
        self._channel_id = None
        self._contact_id = None
        self._enter_time = None
        self._flow_id = None
        self._flow_name = None
        self._leave_time = None
        self._node_exit_code = None
        self._node_id = None
        self._node_name = None
        self._node_properties = None
        self._node_type = None
        self._node_variables = None

    @property
    def callee(self):
        return self._callee

    @callee.setter
    def callee(self, value):
        self._callee = value
    @property
    def caller(self):
        return self._caller

    @caller.setter
    def caller(self, value):
        self._caller = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def enter_time(self):
        return self._enter_time

    @enter_time.setter
    def enter_time(self, value):
        self._enter_time = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def flow_name(self):
        return self._flow_name

    @flow_name.setter
    def flow_name(self, value):
        self._flow_name = value
    @property
    def leave_time(self):
        return self._leave_time

    @leave_time.setter
    def leave_time(self, value):
        self._leave_time = value
    @property
    def node_exit_code(self):
        return self._node_exit_code

    @node_exit_code.setter
    def node_exit_code(self, value):
        self._node_exit_code = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def node_properties(self):
        return self._node_properties

    @node_properties.setter
    def node_properties(self, value):
        self._node_properties = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def node_variables(self):
        return self._node_variables

    @node_variables.setter
    def node_variables(self, value):
        self._node_variables = value


    def to_alipay_dict(self):
        params = dict()
        if self.callee:
            if hasattr(self.callee, 'to_alipay_dict'):
                params['callee'] = self.callee.to_alipay_dict()
            else:
                params['callee'] = self.callee
        if self.caller:
            if hasattr(self.caller, 'to_alipay_dict'):
                params['caller'] = self.caller.to_alipay_dict()
            else:
                params['caller'] = self.caller
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.enter_time:
            if hasattr(self.enter_time, 'to_alipay_dict'):
                params['enter_time'] = self.enter_time.to_alipay_dict()
            else:
                params['enter_time'] = self.enter_time
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.flow_name:
            if hasattr(self.flow_name, 'to_alipay_dict'):
                params['flow_name'] = self.flow_name.to_alipay_dict()
            else:
                params['flow_name'] = self.flow_name
        if self.leave_time:
            if hasattr(self.leave_time, 'to_alipay_dict'):
                params['leave_time'] = self.leave_time.to_alipay_dict()
            else:
                params['leave_time'] = self.leave_time
        if self.node_exit_code:
            if hasattr(self.node_exit_code, 'to_alipay_dict'):
                params['node_exit_code'] = self.node_exit_code.to_alipay_dict()
            else:
                params['node_exit_code'] = self.node_exit_code
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.node_properties:
            if hasattr(self.node_properties, 'to_alipay_dict'):
                params['node_properties'] = self.node_properties.to_alipay_dict()
            else:
                params['node_properties'] = self.node_properties
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.node_variables:
            if hasattr(self.node_variables, 'to_alipay_dict'):
                params['node_variables'] = self.node_variables.to_alipay_dict()
            else:
                params['node_variables'] = self.node_variables
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IvrTrackingVO()
        if 'callee' in d:
            o.callee = d['callee']
        if 'caller' in d:
            o.caller = d['caller']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'enter_time' in d:
            o.enter_time = d['enter_time']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'flow_name' in d:
            o.flow_name = d['flow_name']
        if 'leave_time' in d:
            o.leave_time = d['leave_time']
        if 'node_exit_code' in d:
            o.node_exit_code = d['node_exit_code']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'node_properties' in d:
            o.node_properties = d['node_properties']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'node_variables' in d:
            o.node_variables = d['node_variables']
        return o


