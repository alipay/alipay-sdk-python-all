#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvRsVectorQueryModel(object):

    def __init__(self):
        self._project_id = None
        self._x = None
        self._y = None
        self._z = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value


    def to_alipay_dict(self):
        params = dict()
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.x:
            if hasattr(self.x, 'to_alipay_dict'):
                params['x'] = self.x.to_alipay_dict()
            else:
                params['x'] = self.x
        if self.y:
            if hasattr(self.y, 'to_alipay_dict'):
                params['y'] = self.y.to_alipay_dict()
            else:
                params['y'] = self.y
        if self.z:
            if hasattr(self.z, 'to_alipay_dict'):
                params['z'] = self.z.to_alipay_dict()
            else:
                params['z'] = self.z
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvRsVectorQueryModel()
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        if 'z' in d:
            o.z = d['z']
        return o


