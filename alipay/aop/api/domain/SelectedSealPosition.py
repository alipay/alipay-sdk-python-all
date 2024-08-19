#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelectedSealPosition(object):

    def __init__(self):
        self._location_type = None
        self._main_body_page = None
        self._pos_x = None
        self._pos_y = None
        self._position_type = None
        self._seal_height = None
        self._seal_width = None

    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def main_body_page(self):
        return self._main_body_page

    @main_body_page.setter
    def main_body_page(self, value):
        self._main_body_page = value
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
    def position_type(self):
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        self._position_type = value
    @property
    def seal_height(self):
        return self._seal_height

    @seal_height.setter
    def seal_height(self, value):
        self._seal_height = value
    @property
    def seal_width(self):
        return self._seal_width

    @seal_width.setter
    def seal_width(self, value):
        self._seal_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.main_body_page:
            if hasattr(self.main_body_page, 'to_alipay_dict'):
                params['main_body_page'] = self.main_body_page.to_alipay_dict()
            else:
                params['main_body_page'] = self.main_body_page
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
        if self.position_type:
            if hasattr(self.position_type, 'to_alipay_dict'):
                params['position_type'] = self.position_type.to_alipay_dict()
            else:
                params['position_type'] = self.position_type
        if self.seal_height:
            if hasattr(self.seal_height, 'to_alipay_dict'):
                params['seal_height'] = self.seal_height.to_alipay_dict()
            else:
                params['seal_height'] = self.seal_height
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
        o = SelectedSealPosition()
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'main_body_page' in d:
            o.main_body_page = d['main_body_page']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'position_type' in d:
            o.position_type = d['position_type']
        if 'seal_height' in d:
            o.seal_height = d['seal_height']
        if 'seal_width' in d:
            o.seal_width = d['seal_width']
        return o


