#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignatoryStyle import SignatoryStyle


class TimeStampRectOpenVO(object):

    def __init__(self):
        self._offset_x = None
        self._offset_y = None
        self._page = None
        self._rect_id = None
        self._rect_name = None
        self._rect_style = None
        self._required = None
        self._time_format = None

    @property
    def offset_x(self):
        return self._offset_x

    @offset_x.setter
    def offset_x(self, value):
        self._offset_x = value
    @property
    def offset_y(self):
        return self._offset_y

    @offset_y.setter
    def offset_y(self, value):
        self._offset_y = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def rect_id(self):
        return self._rect_id

    @rect_id.setter
    def rect_id(self, value):
        self._rect_id = value
    @property
    def rect_name(self):
        return self._rect_name

    @rect_name.setter
    def rect_name(self, value):
        self._rect_name = value
    @property
    def rect_style(self):
        return self._rect_style

    @rect_style.setter
    def rect_style(self, value):
        if isinstance(value, SignatoryStyle):
            self._rect_style = value
        else:
            self._rect_style = SignatoryStyle.from_alipay_dict(value)
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def time_format(self):
        return self._time_format

    @time_format.setter
    def time_format(self, value):
        self._time_format = value


    def to_alipay_dict(self):
        params = dict()
        if self.offset_x:
            if hasattr(self.offset_x, 'to_alipay_dict'):
                params['offset_x'] = self.offset_x.to_alipay_dict()
            else:
                params['offset_x'] = self.offset_x
        if self.offset_y:
            if hasattr(self.offset_y, 'to_alipay_dict'):
                params['offset_y'] = self.offset_y.to_alipay_dict()
            else:
                params['offset_y'] = self.offset_y
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.rect_id:
            if hasattr(self.rect_id, 'to_alipay_dict'):
                params['rect_id'] = self.rect_id.to_alipay_dict()
            else:
                params['rect_id'] = self.rect_id
        if self.rect_name:
            if hasattr(self.rect_name, 'to_alipay_dict'):
                params['rect_name'] = self.rect_name.to_alipay_dict()
            else:
                params['rect_name'] = self.rect_name
        if self.rect_style:
            if hasattr(self.rect_style, 'to_alipay_dict'):
                params['rect_style'] = self.rect_style.to_alipay_dict()
            else:
                params['rect_style'] = self.rect_style
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.time_format:
            if hasattr(self.time_format, 'to_alipay_dict'):
                params['time_format'] = self.time_format.to_alipay_dict()
            else:
                params['time_format'] = self.time_format
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeStampRectOpenVO()
        if 'offset_x' in d:
            o.offset_x = d['offset_x']
        if 'offset_y' in d:
            o.offset_y = d['offset_y']
        if 'page' in d:
            o.page = d['page']
        if 'rect_id' in d:
            o.rect_id = d['rect_id']
        if 'rect_name' in d:
            o.rect_name = d['rect_name']
        if 'rect_style' in d:
            o.rect_style = d['rect_style']
        if 'required' in d:
            o.required = d['required']
        if 'time_format' in d:
            o.time_format = d['time_format']
        return o


