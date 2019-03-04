#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessPoint(object):

    def __init__(self):
        self._point_desc = None
        self._point_id = None
        self._point_name = None
        self._remark = None
        self._status = None

    @property
    def point_desc(self):
        return self._point_desc

    @point_desc.setter
    def point_desc(self, value):
        self._point_desc = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.point_desc:
            if hasattr(self.point_desc, 'to_alipay_dict'):
                params['point_desc'] = self.point_desc.to_alipay_dict()
            else:
                params['point_desc'] = self.point_desc
        if self.point_id:
            if hasattr(self.point_id, 'to_alipay_dict'):
                params['point_id'] = self.point_id.to_alipay_dict()
            else:
                params['point_id'] = self.point_id
        if self.point_name:
            if hasattr(self.point_name, 'to_alipay_dict'):
                params['point_name'] = self.point_name.to_alipay_dict()
            else:
                params['point_name'] = self.point_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessPoint()
        if 'point_desc' in d:
            o.point_desc = d['point_desc']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'point_name' in d:
            o.point_name = d['point_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        return o


