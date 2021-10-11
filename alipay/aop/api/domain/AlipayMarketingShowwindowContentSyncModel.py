#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeviceInfo import IotDeviceInfo


class AlipayMarketingShowwindowContentSyncModel(object):

    def __init__(self):
        self._device_info_list = None
        self._event_tag = None
        self._source = None

    @property
    def device_info_list(self):
        return self._device_info_list

    @device_info_list.setter
    def device_info_list(self, value):
        if isinstance(value, list):
            self._device_info_list = list()
            for i in value:
                if isinstance(i, IotDeviceInfo):
                    self._device_info_list.append(i)
                else:
                    self._device_info_list.append(IotDeviceInfo.from_alipay_dict(i))
    @property
    def event_tag(self):
        return self._event_tag

    @event_tag.setter
    def event_tag(self, value):
        self._event_tag = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_info_list:
            if isinstance(self.device_info_list, list):
                for i in range(0, len(self.device_info_list)):
                    element = self.device_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_info_list[i] = element.to_alipay_dict()
            if hasattr(self.device_info_list, 'to_alipay_dict'):
                params['device_info_list'] = self.device_info_list.to_alipay_dict()
            else:
                params['device_info_list'] = self.device_info_list
        if self.event_tag:
            if hasattr(self.event_tag, 'to_alipay_dict'):
                params['event_tag'] = self.event_tag.to_alipay_dict()
            else:
                params['event_tag'] = self.event_tag
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingShowwindowContentSyncModel()
        if 'device_info_list' in d:
            o.device_info_list = d['device_info_list']
        if 'event_tag' in d:
            o.event_tag = d['event_tag']
        if 'source' in d:
            o.source = d['source']
        return o


