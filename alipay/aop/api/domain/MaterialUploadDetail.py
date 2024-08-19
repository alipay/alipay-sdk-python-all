#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaterialUploadDetail(object):

    def __init__(self):
        self._material_instance_id = None
        self._status = None

    @property
    def material_instance_id(self):
        return self._material_instance_id

    @material_instance_id.setter
    def material_instance_id(self, value):
        self._material_instance_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_instance_id:
            if hasattr(self.material_instance_id, 'to_alipay_dict'):
                params['material_instance_id'] = self.material_instance_id.to_alipay_dict()
            else:
                params['material_instance_id'] = self.material_instance_id
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
        o = MaterialUploadDetail()
        if 'material_instance_id' in d:
            o.material_instance_id = d['material_instance_id']
        if 'status' in d:
            o.status = d['status']
        return o


