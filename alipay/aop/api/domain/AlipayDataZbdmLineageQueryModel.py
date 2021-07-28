#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataZbdmLineageQueryModel(object):

    def __init__(self):
        self._direction = None
        self._edge_type = None
        self._max_depth = None
        self._start_ids = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def edge_type(self):
        return self._edge_type

    @edge_type.setter
    def edge_type(self, value):
        if isinstance(value, list):
            self._edge_type = list()
            for i in value:
                self._edge_type.append(i)
    @property
    def max_depth(self):
        return self._max_depth

    @max_depth.setter
    def max_depth(self, value):
        self._max_depth = value
    @property
    def start_ids(self):
        return self._start_ids

    @start_ids.setter
    def start_ids(self, value):
        if isinstance(value, list):
            self._start_ids = list()
            for i in value:
                self._start_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.edge_type:
            if isinstance(self.edge_type, list):
                for i in range(0, len(self.edge_type)):
                    element = self.edge_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.edge_type[i] = element.to_alipay_dict()
            if hasattr(self.edge_type, 'to_alipay_dict'):
                params['edge_type'] = self.edge_type.to_alipay_dict()
            else:
                params['edge_type'] = self.edge_type
        if self.max_depth:
            if hasattr(self.max_depth, 'to_alipay_dict'):
                params['max_depth'] = self.max_depth.to_alipay_dict()
            else:
                params['max_depth'] = self.max_depth
        if self.start_ids:
            if isinstance(self.start_ids, list):
                for i in range(0, len(self.start_ids)):
                    element = self.start_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.start_ids[i] = element.to_alipay_dict()
            if hasattr(self.start_ids, 'to_alipay_dict'):
                params['start_ids'] = self.start_ids.to_alipay_dict()
            else:
                params['start_ids'] = self.start_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataZbdmLineageQueryModel()
        if 'direction' in d:
            o.direction = d['direction']
        if 'edge_type' in d:
            o.edge_type = d['edge_type']
        if 'max_depth' in d:
            o.max_depth = d['max_depth']
        if 'start_ids' in d:
            o.start_ids = d['start_ids']
        return o


