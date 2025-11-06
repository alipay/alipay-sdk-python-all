#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorScmQueryModel(object):

    def __init__(self):
        self._channel_code = None
        self._doctor_id_list = None
        self._scene_code = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def doctor_id_list(self):
        return self._doctor_id_list

    @doctor_id_list.setter
    def doctor_id_list(self, value):
        if isinstance(value, list):
            self._doctor_id_list = list()
            for i in value:
                self._doctor_id_list.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.doctor_id_list:
            if isinstance(self.doctor_id_list, list):
                for i in range(0, len(self.doctor_id_list)):
                    element = self.doctor_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_id_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_id_list, 'to_alipay_dict'):
                params['doctor_id_list'] = self.doctor_id_list.to_alipay_dict()
            else:
                params['doctor_id_list'] = self.doctor_id_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorScmQueryModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'doctor_id_list' in d:
            o.doctor_id_list = d['doctor_id_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


