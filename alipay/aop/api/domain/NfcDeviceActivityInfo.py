#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityParticipateInfo import ActivityParticipateInfo


class NfcDeviceActivityInfo(object):

    def __init__(self):
        self._device_id = None
        self._device_type = None
        self._dvc_participate_info_list = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def dvc_participate_info_list(self):
        return self._dvc_participate_info_list

    @dvc_participate_info_list.setter
    def dvc_participate_info_list(self, value):
        if isinstance(value, list):
            self._dvc_participate_info_list = list()
            for i in value:
                if isinstance(i, ActivityParticipateInfo):
                    self._dvc_participate_info_list.append(i)
                else:
                    self._dvc_participate_info_list.append(ActivityParticipateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.dvc_participate_info_list:
            if isinstance(self.dvc_participate_info_list, list):
                for i in range(0, len(self.dvc_participate_info_list)):
                    element = self.dvc_participate_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dvc_participate_info_list[i] = element.to_alipay_dict()
            if hasattr(self.dvc_participate_info_list, 'to_alipay_dict'):
                params['dvc_participate_info_list'] = self.dvc_participate_info_list.to_alipay_dict()
            else:
                params['dvc_participate_info_list'] = self.dvc_participate_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcDeviceActivityInfo()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'dvc_participate_info_list' in d:
            o.dvc_participate_info_list = d['dvc_participate_info_list']
        return o


