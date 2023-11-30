#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppItemCategoryPreconsultModel(object):

    def __init__(self):
        self._img_id = None
        self._path = None
        self._title = None

    @property
    def img_id(self):
        return self._img_id

    @img_id.setter
    def img_id(self, value):
        self._img_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_id:
            if hasattr(self.img_id, 'to_alipay_dict'):
                params['img_id'] = self.img_id.to_alipay_dict()
            else:
                params['img_id'] = self.img_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItemCategoryPreconsultModel()
        if 'img_id' in d:
            o.img_id = d['img_id']
        if 'path' in d:
            o.path = d['path']
        if 'title' in d:
            o.title = d['title']
        return o


