#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderDevice(object):

    def __init__(self):
        self._device_sn = None
        self._install_actual_photo = None
        self._install_mode = None
        self._install_scene_photo = None
        self._is_install_router = None
        self._screen_size = None
        self._supplier_sn = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def install_actual_photo(self):
        return self._install_actual_photo

    @install_actual_photo.setter
    def install_actual_photo(self, value):
        self._install_actual_photo = value
    @property
    def install_mode(self):
        return self._install_mode

    @install_mode.setter
    def install_mode(self, value):
        self._install_mode = value
    @property
    def install_scene_photo(self):
        return self._install_scene_photo

    @install_scene_photo.setter
    def install_scene_photo(self, value):
        self._install_scene_photo = value
    @property
    def is_install_router(self):
        return self._is_install_router

    @is_install_router.setter
    def is_install_router(self, value):
        self._is_install_router = value
    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        self._screen_size = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.install_actual_photo:
            if hasattr(self.install_actual_photo, 'to_alipay_dict'):
                params['install_actual_photo'] = self.install_actual_photo.to_alipay_dict()
            else:
                params['install_actual_photo'] = self.install_actual_photo
        if self.install_mode:
            if hasattr(self.install_mode, 'to_alipay_dict'):
                params['install_mode'] = self.install_mode.to_alipay_dict()
            else:
                params['install_mode'] = self.install_mode
        if self.install_scene_photo:
            if hasattr(self.install_scene_photo, 'to_alipay_dict'):
                params['install_scene_photo'] = self.install_scene_photo.to_alipay_dict()
            else:
                params['install_scene_photo'] = self.install_scene_photo
        if self.is_install_router:
            if hasattr(self.is_install_router, 'to_alipay_dict'):
                params['is_install_router'] = self.is_install_router.to_alipay_dict()
            else:
                params['is_install_router'] = self.is_install_router
        if self.screen_size:
            if hasattr(self.screen_size, 'to_alipay_dict'):
                params['screen_size'] = self.screen_size.to_alipay_dict()
            else:
                params['screen_size'] = self.screen_size
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDevice()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'install_actual_photo' in d:
            o.install_actual_photo = d['install_actual_photo']
        if 'install_mode' in d:
            o.install_mode = d['install_mode']
        if 'install_scene_photo' in d:
            o.install_scene_photo = d['install_scene_photo']
        if 'is_install_router' in d:
            o.is_install_router = d['is_install_router']
        if 'screen_size' in d:
            o.screen_size = d['screen_size']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        return o


