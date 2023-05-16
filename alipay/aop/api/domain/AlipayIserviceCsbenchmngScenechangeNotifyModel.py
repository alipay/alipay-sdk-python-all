#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceSceneBasicVO import ServiceSceneBasicVO


class AlipayIserviceCsbenchmngScenechangeNotifyModel(object):

    def __init__(self):
        self._service_scene_list = None

    @property
    def service_scene_list(self):
        return self._service_scene_list

    @service_scene_list.setter
    def service_scene_list(self, value):
        if isinstance(value, list):
            self._service_scene_list = list()
            for i in value:
                if isinstance(i, ServiceSceneBasicVO):
                    self._service_scene_list.append(i)
                else:
                    self._service_scene_list.append(ServiceSceneBasicVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.service_scene_list:
            if isinstance(self.service_scene_list, list):
                for i in range(0, len(self.service_scene_list)):
                    element = self.service_scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_scene_list[i] = element.to_alipay_dict()
            if hasattr(self.service_scene_list, 'to_alipay_dict'):
                params['service_scene_list'] = self.service_scene_list.to_alipay_dict()
            else:
                params['service_scene_list'] = self.service_scene_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCsbenchmngScenechangeNotifyModel()
        if 'service_scene_list' in d:
            o.service_scene_list = d['service_scene_list']
        return o


