#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryNode(object):

    def __init__(self):
        self._node_desc = None
        self._node_name = None
        self._time = None

    @property
    def node_desc(self):
        return self._node_desc

    @node_desc.setter
    def node_desc(self, value):
        self._node_desc = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_desc:
            if hasattr(self.node_desc, 'to_alipay_dict'):
                params['node_desc'] = self.node_desc.to_alipay_dict()
            else:
                params['node_desc'] = self.node_desc
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryNode()
        if 'node_desc' in d:
            o.node_desc = d['node_desc']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'time' in d:
            o.time = d['time']
        return o


