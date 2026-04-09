#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubDepartmentInfoVO(object):

    def __init__(self):
        self._depart_id = None
        self._depart_name = None

    @property
    def depart_id(self):
        return self._depart_id

    @depart_id.setter
    def depart_id(self, value):
        self._depart_id = value
    @property
    def depart_name(self):
        return self._depart_name

    @depart_name.setter
    def depart_name(self, value):
        self._depart_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.depart_id:
            if hasattr(self.depart_id, 'to_alipay_dict'):
                params['depart_id'] = self.depart_id.to_alipay_dict()
            else:
                params['depart_id'] = self.depart_id
        if self.depart_name:
            if hasattr(self.depart_name, 'to_alipay_dict'):
                params['depart_name'] = self.depart_name.to_alipay_dict()
            else:
                params['depart_name'] = self.depart_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubDepartmentInfoVO()
        if 'depart_id' in d:
            o.depart_id = d['depart_id']
        if 'depart_name' in d:
            o.depart_name = d['depart_name']
        return o


