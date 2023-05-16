#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceSceneChannelVO import ServiceSceneChannelVO


class ServiceSceneBasicVO(object):

    def __init__(self):
        self._channels = None
        self._scene_info_id = None
        self._scene_name = None
        self._service_mode = None
        self._service_scene_id = None
        self._solution_code = None
        self._status = None
        self._tnt_inst_id = None

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                if isinstance(i, ServiceSceneChannelVO):
                    self._channels.append(i)
                else:
                    self._channels.append(ServiceSceneChannelVO.from_alipay_dict(i))
    @property
    def scene_info_id(self):
        return self._scene_info_id

    @scene_info_id.setter
    def scene_info_id(self, value):
        self._scene_info_id = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def service_mode(self):
        return self._service_mode

    @service_mode.setter
    def service_mode(self, value):
        self._service_mode = value
    @property
    def service_scene_id(self):
        return self._service_scene_id

    @service_scene_id.setter
    def service_scene_id(self, value):
        self._service_scene_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channels:
            if isinstance(self.channels, list):
                for i in range(0, len(self.channels)):
                    element = self.channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channels[i] = element.to_alipay_dict()
            if hasattr(self.channels, 'to_alipay_dict'):
                params['channels'] = self.channels.to_alipay_dict()
            else:
                params['channels'] = self.channels
        if self.scene_info_id:
            if hasattr(self.scene_info_id, 'to_alipay_dict'):
                params['scene_info_id'] = self.scene_info_id.to_alipay_dict()
            else:
                params['scene_info_id'] = self.scene_info_id
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.service_mode:
            if hasattr(self.service_mode, 'to_alipay_dict'):
                params['service_mode'] = self.service_mode.to_alipay_dict()
            else:
                params['service_mode'] = self.service_mode
        if self.service_scene_id:
            if hasattr(self.service_scene_id, 'to_alipay_dict'):
                params['service_scene_id'] = self.service_scene_id.to_alipay_dict()
            else:
                params['service_scene_id'] = self.service_scene_id
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceSceneBasicVO()
        if 'channels' in d:
            o.channels = d['channels']
        if 'scene_info_id' in d:
            o.scene_info_id = d['scene_info_id']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'service_mode' in d:
            o.service_mode = d['service_mode']
        if 'service_scene_id' in d:
            o.service_scene_id = d['service_scene_id']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'status' in d:
            o.status = d['status']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


