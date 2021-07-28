#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayCodecAcodeDecodeUseModel(object):

    def __init__(self):
        self._acode_scene = None
        self._biz_scene = None
        self._device_id = None
        self._dynamic_id = None
        self._institution_type = None
        self._lbs_info = None
        self._scan_time = None
        self._scene_no = None

    @property
    def acode_scene(self):
        return self._acode_scene

    @acode_scene.setter
    def acode_scene(self, value):
        self._acode_scene = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def dynamic_id(self):
        return self._dynamic_id

    @dynamic_id.setter
    def dynamic_id(self, value):
        self._dynamic_id = value
    @property
    def institution_type(self):
        return self._institution_type

    @institution_type.setter
    def institution_type(self, value):
        self._institution_type = value
    @property
    def lbs_info(self):
        return self._lbs_info

    @lbs_info.setter
    def lbs_info(self, value):
        self._lbs_info = value
    @property
    def scan_time(self):
        return self._scan_time

    @scan_time.setter
    def scan_time(self, value):
        self._scan_time = value
    @property
    def scene_no(self):
        return self._scene_no

    @scene_no.setter
    def scene_no(self, value):
        self._scene_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.acode_scene:
            if hasattr(self.acode_scene, 'to_alipay_dict'):
                params['acode_scene'] = self.acode_scene.to_alipay_dict()
            else:
                params['acode_scene'] = self.acode_scene
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.dynamic_id:
            if hasattr(self.dynamic_id, 'to_alipay_dict'):
                params['dynamic_id'] = self.dynamic_id.to_alipay_dict()
            else:
                params['dynamic_id'] = self.dynamic_id
        if self.institution_type:
            if hasattr(self.institution_type, 'to_alipay_dict'):
                params['institution_type'] = self.institution_type.to_alipay_dict()
            else:
                params['institution_type'] = self.institution_type
        if self.lbs_info:
            if hasattr(self.lbs_info, 'to_alipay_dict'):
                params['lbs_info'] = self.lbs_info.to_alipay_dict()
            else:
                params['lbs_info'] = self.lbs_info
        if self.scan_time:
            if hasattr(self.scan_time, 'to_alipay_dict'):
                params['scan_time'] = self.scan_time.to_alipay_dict()
            else:
                params['scan_time'] = self.scan_time
        if self.scene_no:
            if hasattr(self.scene_no, 'to_alipay_dict'):
                params['scene_no'] = self.scene_no.to_alipay_dict()
            else:
                params['scene_no'] = self.scene_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecAcodeDecodeUseModel()
        if 'acode_scene' in d:
            o.acode_scene = d['acode_scene']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'dynamic_id' in d:
            o.dynamic_id = d['dynamic_id']
        if 'institution_type' in d:
            o.institution_type = d['institution_type']
        if 'lbs_info' in d:
            o.lbs_info = d['lbs_info']
        if 'scan_time' in d:
            o.scan_time = d['scan_time']
        if 'scene_no' in d:
            o.scene_no = d['scene_no']
        return o


