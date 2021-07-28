#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceTimeInfo(object):

    def __init__(self):
        self._advance_time = None
        self._time_nodes = None

    @property
    def advance_time(self):
        return self._advance_time

    @advance_time.setter
    def advance_time(self, value):
        self._advance_time = value
    @property
    def time_nodes(self):
        return self._time_nodes

    @time_nodes.setter
    def time_nodes(self, value):
        if isinstance(value, list):
            self._time_nodes = list()
            for i in value:
                self._time_nodes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.advance_time:
            if hasattr(self.advance_time, 'to_alipay_dict'):
                params['advance_time'] = self.advance_time.to_alipay_dict()
            else:
                params['advance_time'] = self.advance_time
        if self.time_nodes:
            if isinstance(self.time_nodes, list):
                for i in range(0, len(self.time_nodes)):
                    element = self.time_nodes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_nodes[i] = element.to_alipay_dict()
            if hasattr(self.time_nodes, 'to_alipay_dict'):
                params['time_nodes'] = self.time_nodes.to_alipay_dict()
            else:
                params['time_nodes'] = self.time_nodes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceTimeInfo()
        if 'advance_time' in d:
            o.advance_time = d['advance_time']
        if 'time_nodes' in d:
            o.time_nodes = d['time_nodes']
        return o


