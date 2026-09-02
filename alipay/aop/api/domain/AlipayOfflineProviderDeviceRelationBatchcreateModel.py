#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceRelationDetail import DeviceRelationDetail


class AlipayOfflineProviderDeviceRelationBatchcreateModel(object):

    def __init__(self):
        self._device_relation_list = None

    @property
    def device_relation_list(self):
        return self._device_relation_list

    @device_relation_list.setter
    def device_relation_list(self, value):
        if isinstance(value, list):
            self._device_relation_list = list()
            for i in value:
                if isinstance(i, DeviceRelationDetail):
                    self._device_relation_list.append(i)
                else:
                    self._device_relation_list.append(DeviceRelationDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.device_relation_list:
            if isinstance(self.device_relation_list, list):
                for i in range(0, len(self.device_relation_list)):
                    element = self.device_relation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_relation_list[i] = element.to_alipay_dict()
            if hasattr(self.device_relation_list, 'to_alipay_dict'):
                params['device_relation_list'] = self.device_relation_list.to_alipay_dict()
            else:
                params['device_relation_list'] = self.device_relation_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderDeviceRelationBatchcreateModel()
        if 'device_relation_list' in d:
            o.device_relation_list = d['device_relation_list']
        return o


