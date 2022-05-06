#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExplanationPoint import ScenicExplanationPoint


class AlipayCommerceDataScenicExplanationSyncModel(object):

    def __init__(self):
        self._scenic_app_id = None
        self._scenic_outer_id = None
        self._scenic_points = None
        self._service_plugin_id = None

    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def scenic_outer_id(self):
        return self._scenic_outer_id

    @scenic_outer_id.setter
    def scenic_outer_id(self, value):
        self._scenic_outer_id = value
    @property
    def scenic_points(self):
        return self._scenic_points

    @scenic_points.setter
    def scenic_points(self, value):
        if isinstance(value, list):
            self._scenic_points = list()
            for i in value:
                if isinstance(i, ScenicExplanationPoint):
                    self._scenic_points.append(i)
                else:
                    self._scenic_points.append(ScenicExplanationPoint.from_alipay_dict(i))
    @property
    def service_plugin_id(self):
        return self._service_plugin_id

    @service_plugin_id.setter
    def service_plugin_id(self, value):
        self._service_plugin_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.scenic_outer_id:
            if hasattr(self.scenic_outer_id, 'to_alipay_dict'):
                params['scenic_outer_id'] = self.scenic_outer_id.to_alipay_dict()
            else:
                params['scenic_outer_id'] = self.scenic_outer_id
        if self.scenic_points:
            if isinstance(self.scenic_points, list):
                for i in range(0, len(self.scenic_points)):
                    element = self.scenic_points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenic_points[i] = element.to_alipay_dict()
            if hasattr(self.scenic_points, 'to_alipay_dict'):
                params['scenic_points'] = self.scenic_points.to_alipay_dict()
            else:
                params['scenic_points'] = self.scenic_points
        if self.service_plugin_id:
            if hasattr(self.service_plugin_id, 'to_alipay_dict'):
                params['service_plugin_id'] = self.service_plugin_id.to_alipay_dict()
            else:
                params['service_plugin_id'] = self.service_plugin_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataScenicExplanationSyncModel()
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'scenic_outer_id' in d:
            o.scenic_outer_id = d['scenic_outer_id']
        if 'scenic_points' in d:
            o.scenic_points = d['scenic_points']
        if 'service_plugin_id' in d:
            o.service_plugin_id = d['service_plugin_id']
        return o


