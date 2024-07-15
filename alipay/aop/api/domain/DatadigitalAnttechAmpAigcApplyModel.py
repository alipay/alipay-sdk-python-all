#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechAmpAigcApplyModel(object):

    def __init__(self):
        self._context = None
        self._device_id = None
        self._device_id_type = None
        self._height = None
        self._mode = None
        self._param_data = None
        self._request_id = None
        self._social_code = None
        self._style = None
        self._width = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_id_type(self):
        return self._device_id_type

    @device_id_type.setter
    def device_id_type(self, value):
        self._device_id_type = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def param_data(self):
        return self._param_data

    @param_data.setter
    def param_data(self, value):
        self._param_data = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def social_code(self):
        return self._social_code

    @social_code.setter
    def social_code(self, value):
        self._social_code = value
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_id_type:
            if hasattr(self.device_id_type, 'to_alipay_dict'):
                params['device_id_type'] = self.device_id_type.to_alipay_dict()
            else:
                params['device_id_type'] = self.device_id_type
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.param_data:
            if hasattr(self.param_data, 'to_alipay_dict'):
                params['param_data'] = self.param_data.to_alipay_dict()
            else:
                params['param_data'] = self.param_data
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.social_code:
            if hasattr(self.social_code, 'to_alipay_dict'):
                params['social_code'] = self.social_code.to_alipay_dict()
            else:
                params['social_code'] = self.social_code
        if self.style:
            if hasattr(self.style, 'to_alipay_dict'):
                params['style'] = self.style.to_alipay_dict()
            else:
                params['style'] = self.style
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechAmpAigcApplyModel()
        if 'context' in d:
            o.context = d['context']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_id_type' in d:
            o.device_id_type = d['device_id_type']
        if 'height' in d:
            o.height = d['height']
        if 'mode' in d:
            o.mode = d['mode']
        if 'param_data' in d:
            o.param_data = d['param_data']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'social_code' in d:
            o.social_code = d['social_code']
        if 'style' in d:
            o.style = d['style']
        if 'width' in d:
            o.width = d['width']
        return o


