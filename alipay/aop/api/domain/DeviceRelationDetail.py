#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceRelationDetail(object):

    def __init__(self):
        self._device_sn = None
        self._related_pid = None
        self._supplier_id = None
        self._tag_sn = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def related_pid(self):
        return self._related_pid

    @related_pid.setter
    def related_pid(self, value):
        self._related_pid = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def tag_sn(self):
        return self._tag_sn

    @tag_sn.setter
    def tag_sn(self, value):
        self._tag_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.related_pid:
            if hasattr(self.related_pid, 'to_alipay_dict'):
                params['related_pid'] = self.related_pid.to_alipay_dict()
            else:
                params['related_pid'] = self.related_pid
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.tag_sn:
            if hasattr(self.tag_sn, 'to_alipay_dict'):
                params['tag_sn'] = self.tag_sn.to_alipay_dict()
            else:
                params['tag_sn'] = self.tag_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceRelationDetail()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'related_pid' in d:
            o.related_pid = d['related_pid']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tag_sn' in d:
            o.tag_sn = d['tag_sn']
        return o


