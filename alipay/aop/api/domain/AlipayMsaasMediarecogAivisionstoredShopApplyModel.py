#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CameraInfo import CameraInfo


class AlipayMsaasMediarecogAivisionstoredShopApplyModel(object):

    def __init__(self):
        self._camera_infos = None
        self._device_sn = None
        self._isv_pid = None
        self._shop_name = None
        self._shop_pid = None

    @property
    def camera_infos(self):
        return self._camera_infos

    @camera_infos.setter
    def camera_infos(self, value):
        if isinstance(value, list):
            self._camera_infos = list()
            for i in value:
                if isinstance(i, CameraInfo):
                    self._camera_infos.append(i)
                else:
                    self._camera_infos.append(CameraInfo.from_alipay_dict(i))
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_pid(self):
        return self._shop_pid

    @shop_pid.setter
    def shop_pid(self, value):
        self._shop_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.camera_infos:
            if isinstance(self.camera_infos, list):
                for i in range(0, len(self.camera_infos)):
                    element = self.camera_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.camera_infos[i] = element.to_alipay_dict()
            if hasattr(self.camera_infos, 'to_alipay_dict'):
                params['camera_infos'] = self.camera_infos.to_alipay_dict()
            else:
                params['camera_infos'] = self.camera_infos
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_pid:
            if hasattr(self.shop_pid, 'to_alipay_dict'):
                params['shop_pid'] = self.shop_pid.to_alipay_dict()
            else:
                params['shop_pid'] = self.shop_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionstoredShopApplyModel()
        if 'camera_infos' in d:
            o.camera_infos = d['camera_infos']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_pid' in d:
            o.shop_pid = d['shop_pid']
        return o


