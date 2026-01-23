#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHdfaitransferBingliIdentifyModel(object):

    def __init__(self):
        self._ocr_content = None
        self._scene_code = None

    @property
    def ocr_content(self):
        return self._ocr_content

    @ocr_content.setter
    def ocr_content(self, value):
        self._ocr_content = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ocr_content:
            if hasattr(self.ocr_content, 'to_alipay_dict'):
                params['ocr_content'] = self.ocr_content.to_alipay_dict()
            else:
                params['ocr_content'] = self.ocr_content
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
        o = AlipayCommerceHdfaitransferBingliIdentifyModel()
        if 'ocr_content' in d:
            o.ocr_content = d['ocr_content']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


