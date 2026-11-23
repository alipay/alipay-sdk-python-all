#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateDevicebindwhitelistBatchcreateModel(object):

    def __init__(self):
        self._device_sn_list = None
        self._operate_type = None

    @property
    def device_sn_list(self):
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, value):
        if isinstance(value, list):
            self._device_sn_list = list()
            for i in value:
                self._device_sn_list.append(i)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn_list:
            if isinstance(self.device_sn_list, list):
                for i in range(0, len(self.device_sn_list)):
                    element = self.device_sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_sn_list[i] = element.to_alipay_dict()
            if hasattr(self.device_sn_list, 'to_alipay_dict'):
                params['device_sn_list'] = self.device_sn_list.to_alipay_dict()
            else:
                params['device_sn_list'] = self.device_sn_list
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateDevicebindwhitelistBatchcreateModel()
        if 'device_sn_list' in d:
            o.device_sn_list = d['device_sn_list']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


