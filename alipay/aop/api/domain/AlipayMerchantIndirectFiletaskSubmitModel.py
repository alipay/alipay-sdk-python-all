#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectFiletaskSubmitModel(object):

    def __init__(self):
        self._biz_scene = None
        self._biz_type = None
        self._file_id = None
        self._source_pid = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectFiletaskSubmitModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        return o


