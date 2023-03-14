#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignfieldInfoDTO(object):

    def __init__(self):
        self._file_id = None
        self._free_sign = None
        self._pos_page = None
        self._pos_page_end = None
        self._pos_x = None
        self._pos_y = None
        self._position_type = None
        self._sign_area_type = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def free_sign(self):
        return self._free_sign

    @free_sign.setter
    def free_sign(self, value):
        self._free_sign = value
    @property
    def pos_page(self):
        return self._pos_page

    @pos_page.setter
    def pos_page(self, value):
        self._pos_page = value
    @property
    def pos_page_end(self):
        return self._pos_page_end

    @pos_page_end.setter
    def pos_page_end(self, value):
        self._pos_page_end = value
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
    def sign_area_type(self):
        return self._sign_area_type

    @sign_area_type.setter
    def sign_area_type(self, value):
        self._sign_area_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.free_sign:
            if hasattr(self.free_sign, 'to_alipay_dict'):
                params['free_sign'] = self.free_sign.to_alipay_dict()
            else:
                params['free_sign'] = self.free_sign
        if self.pos_page:
            if hasattr(self.pos_page, 'to_alipay_dict'):
                params['pos_page'] = self.pos_page.to_alipay_dict()
            else:
                params['pos_page'] = self.pos_page
        if self.pos_page_end:
            if hasattr(self.pos_page_end, 'to_alipay_dict'):
                params['pos_page_end'] = self.pos_page_end.to_alipay_dict()
            else:
                params['pos_page_end'] = self.pos_page_end
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
        if self.sign_area_type:
            if hasattr(self.sign_area_type, 'to_alipay_dict'):
                params['sign_area_type'] = self.sign_area_type.to_alipay_dict()
            else:
                params['sign_area_type'] = self.sign_area_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignfieldInfoDTO()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'free_sign' in d:
            o.free_sign = d['free_sign']
        if 'pos_page' in d:
            o.pos_page = d['pos_page']
        if 'pos_page_end' in d:
            o.pos_page_end = d['pos_page_end']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'position_type' in d:
            o.position_type = d['position_type']
        if 'sign_area_type' in d:
            o.sign_area_type = d['sign_area_type']
        return o


