#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignedCrossResult(object):

    def __init__(self):
        self._pos_x = None
        self._pos_y = None
        self._seal_height = None
        self._seal_id = None
        self._seal_impression = None
        self._seal_width = None

    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value
    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value
    @property
    def seal_height(self):
        return self._seal_height

    @seal_height.setter
    def seal_height(self, value):
        self._seal_height = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value
    @property
    def seal_impression(self):
        return self._seal_impression

    @seal_impression.setter
    def seal_impression(self, value):
        self._seal_impression = value
    @property
    def seal_width(self):
        return self._seal_width

    @seal_width.setter
    def seal_width(self, value):
        self._seal_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.pos_x:
            if hasattr(self.pos_x, 'to_alipay_dict'):
                params['pos_x'] = self.pos_x.to_alipay_dict()
            else:
                params['pos_x'] = self.pos_x
        if self.pos_y:
            if hasattr(self.pos_y, 'to_alipay_dict'):
                params['pos_y'] = self.pos_y.to_alipay_dict()
            else:
                params['pos_y'] = self.pos_y
        if self.seal_height:
            if hasattr(self.seal_height, 'to_alipay_dict'):
                params['seal_height'] = self.seal_height.to_alipay_dict()
            else:
                params['seal_height'] = self.seal_height
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        if self.seal_impression:
            if hasattr(self.seal_impression, 'to_alipay_dict'):
                params['seal_impression'] = self.seal_impression.to_alipay_dict()
            else:
                params['seal_impression'] = self.seal_impression
        if self.seal_width:
            if hasattr(self.seal_width, 'to_alipay_dict'):
                params['seal_width'] = self.seal_width.to_alipay_dict()
            else:
                params['seal_width'] = self.seal_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignedCrossResult()
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'seal_height' in d:
            o.seal_height = d['seal_height']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        if 'seal_impression' in d:
            o.seal_impression = d['seal_impression']
        if 'seal_width' in d:
            o.seal_width = d['seal_width']
        return o


