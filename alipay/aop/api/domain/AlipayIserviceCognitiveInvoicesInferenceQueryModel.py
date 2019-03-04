#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveInvoicesInferenceQueryModel(object):

    def __init__(self):
        self._img_content = None

    @property
    def img_content(self):
        return self._img_content

    @img_content.setter
    def img_content(self, value):
        self._img_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_content:
            if hasattr(self.img_content, 'to_alipay_dict'):
                params['img_content'] = self.img_content.to_alipay_dict()
            else:
                params['img_content'] = self.img_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveInvoicesInferenceQueryModel()
        if 'img_content' in d:
            o.img_content = d['img_content']
        return o


