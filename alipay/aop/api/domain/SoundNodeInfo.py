#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SoundNodeInfo(object):

    def __init__(self):
        self._node_desc = None
        self._node_time = None

    @property
    def node_desc(self):
        return self._node_desc

    @node_desc.setter
    def node_desc(self, value):
        self._node_desc = value
    @property
    def node_time(self):
        return self._node_time

    @node_time.setter
    def node_time(self, value):
        self._node_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_desc:
            if hasattr(self.node_desc, 'to_alipay_dict'):
                params['node_desc'] = self.node_desc.to_alipay_dict()
            else:
                params['node_desc'] = self.node_desc
        if self.node_time:
            if hasattr(self.node_time, 'to_alipay_dict'):
                params['node_time'] = self.node_time.to_alipay_dict()
            else:
                params['node_time'] = self.node_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SoundNodeInfo()
        if 'node_desc' in d:
            o.node_desc = d['node_desc']
        if 'node_time' in d:
            o.node_time = d['node_time']
        return o


