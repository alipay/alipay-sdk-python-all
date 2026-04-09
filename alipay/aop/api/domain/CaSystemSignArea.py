#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSystemCrossPage import CaSystemCrossPage
from alipay.aop.api.domain.CaSystemMainBody import CaSystemMainBody


class CaSystemSignArea(object):

    def __init__(self):
        self._ca_system_cross_page = None
        self._ca_system_main_body = None
        self._external_seal_type = None
        self._location_type = None
        self._position_type = None
        self._rotate_angle = None
        self._seal_height = None
        self._seal_id = None
        self._seal_pic_addr = None
        self._seal_width = None

    @property
    def ca_system_cross_page(self):
        return self._ca_system_cross_page

    @ca_system_cross_page.setter
    def ca_system_cross_page(self, value):
        if isinstance(value, CaSystemCrossPage):
            self._ca_system_cross_page = value
        else:
            self._ca_system_cross_page = CaSystemCrossPage.from_alipay_dict(value)
    @property
    def ca_system_main_body(self):
        return self._ca_system_main_body

    @ca_system_main_body.setter
    def ca_system_main_body(self, value):
        if isinstance(value, CaSystemMainBody):
            self._ca_system_main_body = value
        else:
            self._ca_system_main_body = CaSystemMainBody.from_alipay_dict(value)
    @property
    def external_seal_type(self):
        return self._external_seal_type

    @external_seal_type.setter
    def external_seal_type(self, value):
        self._external_seal_type = value
    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def position_type(self):
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        self._position_type = value
    @property
    def rotate_angle(self):
        return self._rotate_angle

    @rotate_angle.setter
    def rotate_angle(self, value):
        self._rotate_angle = value
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
    def seal_pic_addr(self):
        return self._seal_pic_addr

    @seal_pic_addr.setter
    def seal_pic_addr(self, value):
        self._seal_pic_addr = value
    @property
    def seal_width(self):
        return self._seal_width

    @seal_width.setter
    def seal_width(self, value):
        self._seal_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.ca_system_cross_page:
            if hasattr(self.ca_system_cross_page, 'to_alipay_dict'):
                params['ca_system_cross_page'] = self.ca_system_cross_page.to_alipay_dict()
            else:
                params['ca_system_cross_page'] = self.ca_system_cross_page
        if self.ca_system_main_body:
            if hasattr(self.ca_system_main_body, 'to_alipay_dict'):
                params['ca_system_main_body'] = self.ca_system_main_body.to_alipay_dict()
            else:
                params['ca_system_main_body'] = self.ca_system_main_body
        if self.external_seal_type:
            if hasattr(self.external_seal_type, 'to_alipay_dict'):
                params['external_seal_type'] = self.external_seal_type.to_alipay_dict()
            else:
                params['external_seal_type'] = self.external_seal_type
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.position_type:
            if hasattr(self.position_type, 'to_alipay_dict'):
                params['position_type'] = self.position_type.to_alipay_dict()
            else:
                params['position_type'] = self.position_type
        if self.rotate_angle:
            if hasattr(self.rotate_angle, 'to_alipay_dict'):
                params['rotate_angle'] = self.rotate_angle.to_alipay_dict()
            else:
                params['rotate_angle'] = self.rotate_angle
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
        if self.seal_pic_addr:
            if hasattr(self.seal_pic_addr, 'to_alipay_dict'):
                params['seal_pic_addr'] = self.seal_pic_addr.to_alipay_dict()
            else:
                params['seal_pic_addr'] = self.seal_pic_addr
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
        o = CaSystemSignArea()
        if 'ca_system_cross_page' in d:
            o.ca_system_cross_page = d['ca_system_cross_page']
        if 'ca_system_main_body' in d:
            o.ca_system_main_body = d['ca_system_main_body']
        if 'external_seal_type' in d:
            o.external_seal_type = d['external_seal_type']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'position_type' in d:
            o.position_type = d['position_type']
        if 'rotate_angle' in d:
            o.rotate_angle = d['rotate_angle']
        if 'seal_height' in d:
            o.seal_height = d['seal_height']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        if 'seal_pic_addr' in d:
            o.seal_pic_addr = d['seal_pic_addr']
        if 'seal_width' in d:
            o.seal_width = d['seal_width']
        return o


