#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveInvoicesInferenceQueryModel(object):

    def __init__(self):
        self._file_type = None
        self._img_content = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def img_content(self):
        return self._img_content

    @img_content.setter
    def img_content(self, value):
        self._img_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
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
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'img_content' in d:
            o.img_content = d['img_content']
        return o


