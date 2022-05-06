#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StepUnit import StepUnit


class BPOpenApiInstancePreviewStep(object):

    def __init__(self):
        self._activity_id = None
        self._error_msg = None
        self._finish_date = None
        self._next = None
        self._node = None
        self._node_name = None
        self._source_act_id = None
        self._sub_steps = None
        self._success = None
        self._type = None
        self._units = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def finish_date(self):
        return self._finish_date

    @finish_date.setter
    def finish_date(self, value):
        self._finish_date = value
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def source_act_id(self):
        return self._source_act_id

    @source_act_id.setter
    def source_act_id(self, value):
        self._source_act_id = value
    @property
    def sub_steps(self):
        return self._sub_steps

    @sub_steps.setter
    def sub_steps(self, value):
        self._sub_steps = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        if isinstance(value, list):
            self._units = list()
            for i in value:
                if isinstance(i, StepUnit):
                    self._units.append(i)
                else:
                    self._units.append(StepUnit.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.finish_date:
            if hasattr(self.finish_date, 'to_alipay_dict'):
                params['finish_date'] = self.finish_date.to_alipay_dict()
            else:
                params['finish_date'] = self.finish_date
        if self.next:
            if hasattr(self.next, 'to_alipay_dict'):
                params['next'] = self.next.to_alipay_dict()
            else:
                params['next'] = self.next
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.source_act_id:
            if hasattr(self.source_act_id, 'to_alipay_dict'):
                params['source_act_id'] = self.source_act_id.to_alipay_dict()
            else:
                params['source_act_id'] = self.source_act_id
        if self.sub_steps:
            if hasattr(self.sub_steps, 'to_alipay_dict'):
                params['sub_steps'] = self.sub_steps.to_alipay_dict()
            else:
                params['sub_steps'] = self.sub_steps
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.units:
            if isinstance(self.units, list):
                for i in range(0, len(self.units)):
                    element = self.units[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.units[i] = element.to_alipay_dict()
            if hasattr(self.units, 'to_alipay_dict'):
                params['units'] = self.units.to_alipay_dict()
            else:
                params['units'] = self.units
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiInstancePreviewStep()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'finish_date' in d:
            o.finish_date = d['finish_date']
        if 'next' in d:
            o.next = d['next']
        if 'node' in d:
            o.node = d['node']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'source_act_id' in d:
            o.source_act_id = d['source_act_id']
        if 'sub_steps' in d:
            o.sub_steps = d['sub_steps']
        if 'success' in d:
            o.success = d['success']
        if 'type' in d:
            o.type = d['type']
        if 'units' in d:
            o.units = d['units']
        return o


