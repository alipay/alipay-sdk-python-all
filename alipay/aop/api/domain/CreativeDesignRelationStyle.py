#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativeDesignRelationStyle(object):

    def __init__(self):
        self._style_design_relation_mock_img = None
        self._style_id = None
        self._style_mock_img = None

    @property
    def style_design_relation_mock_img(self):
        return self._style_design_relation_mock_img

    @style_design_relation_mock_img.setter
    def style_design_relation_mock_img(self, value):
        self._style_design_relation_mock_img = value
    @property
    def style_id(self):
        return self._style_id

    @style_id.setter
    def style_id(self, value):
        self._style_id = value
    @property
    def style_mock_img(self):
        return self._style_mock_img

    @style_mock_img.setter
    def style_mock_img(self, value):
        self._style_mock_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.style_design_relation_mock_img:
            if hasattr(self.style_design_relation_mock_img, 'to_alipay_dict'):
                params['style_design_relation_mock_img'] = self.style_design_relation_mock_img.to_alipay_dict()
            else:
                params['style_design_relation_mock_img'] = self.style_design_relation_mock_img
        if self.style_id:
            if hasattr(self.style_id, 'to_alipay_dict'):
                params['style_id'] = self.style_id.to_alipay_dict()
            else:
                params['style_id'] = self.style_id
        if self.style_mock_img:
            if hasattr(self.style_mock_img, 'to_alipay_dict'):
                params['style_mock_img'] = self.style_mock_img.to_alipay_dict()
            else:
                params['style_mock_img'] = self.style_mock_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeDesignRelationStyle()
        if 'style_design_relation_mock_img' in d:
            o.style_design_relation_mock_img = d['style_design_relation_mock_img']
        if 'style_id' in d:
            o.style_id = d['style_id']
        if 'style_mock_img' in d:
            o.style_mock_img = d['style_mock_img']
        return o


