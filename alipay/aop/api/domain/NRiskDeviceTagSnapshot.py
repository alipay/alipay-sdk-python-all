#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NRiskDeviceTagSnapshotExtInfo import NRiskDeviceTagSnapshotExtInfo


class NRiskDeviceTagSnapshot(object):

    def __init__(self):
        self._device_type = None
        self._ext_info = None
        self._tag_id = None

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, NRiskDeviceTagSnapshotExtInfo):
            self._ext_info = value
        else:
            self._ext_info = NRiskDeviceTagSnapshotExtInfo.from_alipay_dict(value)
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NRiskDeviceTagSnapshot()
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        return o


