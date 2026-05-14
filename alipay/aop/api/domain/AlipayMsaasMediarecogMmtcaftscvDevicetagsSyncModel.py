#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceLabelInfo import DeviceLabelInfo


class AlipayMsaasMediarecogMmtcaftscvDevicetagsSyncModel(object):

    def __init__(self):
        self._device_id = None
        self._device_label_infos = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_label_infos(self):
        return self._device_label_infos

    @device_label_infos.setter
    def device_label_infos(self, value):
        if isinstance(value, list):
            self._device_label_infos = list()
            for i in value:
                if isinstance(i, DeviceLabelInfo):
                    self._device_label_infos.append(i)
                else:
                    self._device_label_infos.append(DeviceLabelInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_label_infos:
            if isinstance(self.device_label_infos, list):
                for i in range(0, len(self.device_label_infos)):
                    element = self.device_label_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_label_infos[i] = element.to_alipay_dict()
            if hasattr(self.device_label_infos, 'to_alipay_dict'):
                params['device_label_infos'] = self.device_label_infos.to_alipay_dict()
            else:
                params['device_label_infos'] = self.device_label_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvDevicetagsSyncModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_label_infos' in d:
            o.device_label_infos = d['device_label_infos']
        return o


