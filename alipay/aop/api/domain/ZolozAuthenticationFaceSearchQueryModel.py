#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationFaceSearchQueryModel(object):

    def __init__(self):
        self._blob = None
        self._device_num = None
        self._group = None
        self._zim_id = None

    @property
    def blob(self):
        return self._blob

    @blob.setter
    def blob(self, value):
        self._blob = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.blob:
            if hasattr(self.blob, 'to_alipay_dict'):
                params['blob'] = self.blob.to_alipay_dict()
            else:
                params['blob'] = self.blob
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.zim_id:
            if hasattr(self.zim_id, 'to_alipay_dict'):
                params['zim_id'] = self.zim_id.to_alipay_dict()
            else:
                params['zim_id'] = self.zim_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationFaceSearchQueryModel()
        if 'blob' in d:
            o.blob = d['blob']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'group' in d:
            o.group = d['group']
        if 'zim_id' in d:
            o.zim_id = d['zim_id']
        return o


