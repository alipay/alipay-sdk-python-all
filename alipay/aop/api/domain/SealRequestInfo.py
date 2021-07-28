#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SealRequestInfo(object):

    def __init__(self):
        self._axis_x = None
        self._axis_y = None
        self._location_type = None
        self._rotate_angle = None
        self._seal_id = None

    @property
    def axis_x(self):
        return self._axis_x

    @axis_x.setter
    def axis_x(self, value):
        self._axis_x = value
    @property
    def axis_y(self):
        return self._axis_y

    @axis_y.setter
    def axis_y(self, value):
        self._axis_y = value
    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def rotate_angle(self):
        return self._rotate_angle

    @rotate_angle.setter
    def rotate_angle(self, value):
        self._rotate_angle = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.axis_x:
            if hasattr(self.axis_x, 'to_alipay_dict'):
                params['axis_x'] = self.axis_x.to_alipay_dict()
            else:
                params['axis_x'] = self.axis_x
        if self.axis_y:
            if hasattr(self.axis_y, 'to_alipay_dict'):
                params['axis_y'] = self.axis_y.to_alipay_dict()
            else:
                params['axis_y'] = self.axis_y
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.rotate_angle:
            if hasattr(self.rotate_angle, 'to_alipay_dict'):
                params['rotate_angle'] = self.rotate_angle.to_alipay_dict()
            else:
                params['rotate_angle'] = self.rotate_angle
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SealRequestInfo()
        if 'axis_x' in d:
            o.axis_x = d['axis_x']
        if 'axis_y' in d:
            o.axis_y = d['axis_y']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'rotate_angle' in d:
            o.rotate_angle = d['rotate_angle']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        return o


