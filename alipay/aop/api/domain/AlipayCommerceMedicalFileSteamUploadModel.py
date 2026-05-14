#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalFileSteamUploadModel(object):

    def __init__(self):
        self._biz_no = None
        self._file_content = None
        self._file_no = None
        self._file_type = None
        self._scene_type = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        self._file_content = value
    @property
    def file_no(self):
        return self._file_no

    @file_no.setter
    def file_no(self, value):
        self._file_no = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.file_content:
            if hasattr(self.file_content, 'to_alipay_dict'):
                params['file_content'] = self.file_content.to_alipay_dict()
            else:
                params['file_content'] = self.file_content
        if self.file_no:
            if hasattr(self.file_no, 'to_alipay_dict'):
                params['file_no'] = self.file_no.to_alipay_dict()
            else:
                params['file_no'] = self.file_no
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFileSteamUploadModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'file_content' in d:
            o.file_content = d['file_content']
        if 'file_no' in d:
            o.file_no = d['file_no']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


