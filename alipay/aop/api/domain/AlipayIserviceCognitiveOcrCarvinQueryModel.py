#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveOcrCarvinQueryModel(object):

    def __init__(self):
        self._image_content = None

    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayIserviceCognitiveOcrCarvinQueryModel()
        if 'image_content' in d:
            o.image_content = d['image_content']
        return o


