#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CissSportsGuidance(object):

    def __init__(self):
        self._attention = None
        self._exercise_intensity = None
        self._exercise_points = None
        self._exercise_type = None
        self._exercise_type_id = None
        self._id = None

    @property
    def attention(self):
        return self._attention

    @attention.setter
    def attention(self, value):
        self._attention = value
    @property
    def exercise_intensity(self):
        return self._exercise_intensity

    @exercise_intensity.setter
    def exercise_intensity(self, value):
        self._exercise_intensity = value
    @property
    def exercise_points(self):
        return self._exercise_points

    @exercise_points.setter
    def exercise_points(self, value):
        self._exercise_points = value
    @property
    def exercise_type(self):
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, value):
        self._exercise_type = value
    @property
    def exercise_type_id(self):
        return self._exercise_type_id

    @exercise_type_id.setter
    def exercise_type_id(self, value):
        self._exercise_type_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attention:
            if hasattr(self.attention, 'to_alipay_dict'):
                params['attention'] = self.attention.to_alipay_dict()
            else:
                params['attention'] = self.attention
        if self.exercise_intensity:
            if hasattr(self.exercise_intensity, 'to_alipay_dict'):
                params['exercise_intensity'] = self.exercise_intensity.to_alipay_dict()
            else:
                params['exercise_intensity'] = self.exercise_intensity
        if self.exercise_points:
            if hasattr(self.exercise_points, 'to_alipay_dict'):
                params['exercise_points'] = self.exercise_points.to_alipay_dict()
            else:
                params['exercise_points'] = self.exercise_points
        if self.exercise_type:
            if hasattr(self.exercise_type, 'to_alipay_dict'):
                params['exercise_type'] = self.exercise_type.to_alipay_dict()
            else:
                params['exercise_type'] = self.exercise_type
        if self.exercise_type_id:
            if hasattr(self.exercise_type_id, 'to_alipay_dict'):
                params['exercise_type_id'] = self.exercise_type_id.to_alipay_dict()
            else:
                params['exercise_type_id'] = self.exercise_type_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CissSportsGuidance()
        if 'attention' in d:
            o.attention = d['attention']
        if 'exercise_intensity' in d:
            o.exercise_intensity = d['exercise_intensity']
        if 'exercise_points' in d:
            o.exercise_points = d['exercise_points']
        if 'exercise_type' in d:
            o.exercise_type = d['exercise_type']
        if 'exercise_type_id' in d:
            o.exercise_type_id = d['exercise_type_id']
        if 'id' in d:
            o.id = d['id']
        return o


