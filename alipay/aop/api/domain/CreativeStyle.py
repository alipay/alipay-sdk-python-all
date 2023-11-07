#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativeStyle(object):

    def __init__(self):
        self._id = None
        self._mock_img = None
        self._pic_template_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mock_img(self):
        return self._mock_img

    @mock_img.setter
    def mock_img(self, value):
        self._mock_img = value
    @property
    def pic_template_id(self):
        return self._pic_template_id

    @pic_template_id.setter
    def pic_template_id(self, value):
        self._pic_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.mock_img:
            if hasattr(self.mock_img, 'to_alipay_dict'):
                params['mock_img'] = self.mock_img.to_alipay_dict()
            else:
                params['mock_img'] = self.mock_img
        if self.pic_template_id:
            if hasattr(self.pic_template_id, 'to_alipay_dict'):
                params['pic_template_id'] = self.pic_template_id.to_alipay_dict()
            else:
                params['pic_template_id'] = self.pic_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeStyle()
        if 'id' in d:
            o.id = d['id']
        if 'mock_img' in d:
            o.mock_img = d['mock_img']
        if 'pic_template_id' in d:
            o.pic_template_id = d['pic_template_id']
        return o


