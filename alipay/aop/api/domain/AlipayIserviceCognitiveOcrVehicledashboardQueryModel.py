#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveOcrVehicledashboardQueryModel(object):

    def __init__(self):
        self._biz_name = None
        self._image_content = None

    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.image_content:
            if hasattr(self.image_content, 'to_alipay_dict'):
                params['image_content'] = self.image_content.to_alipay_dict()
            else:
                params['image_content'] = self.image_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveOcrVehicledashboardQueryModel()
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'image_content' in d:
            o.image_content = d['image_content']
        return o


