#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataBaiCargocountQueryModel(object):

    def __init__(self):
        self._camera_id = None
        self._counting_params = None
        self._counting_time = None
        self._input_frame = None
        self._input_template = None

    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        self._camera_id = value
    @property
    def counting_params(self):
        return self._counting_params

    @counting_params.setter
    def counting_params(self, value):
        self._counting_params = value
    @property
    def counting_time(self):
        return self._counting_time

    @counting_time.setter
    def counting_time(self, value):
        self._counting_time = value
    @property
    def input_frame(self):
        return self._input_frame

    @input_frame.setter
    def input_frame(self, value):
        self._input_frame = value
    @property
    def input_template(self):
        return self._input_template

    @input_template.setter
    def input_template(self, value):
        self._input_template = value


    def to_alipay_dict(self):
        params = dict()
        if self.camera_id:
            if hasattr(self.camera_id, 'to_alipay_dict'):
                params['camera_id'] = self.camera_id.to_alipay_dict()
            else:
                params['camera_id'] = self.camera_id
        if self.counting_params:
            if hasattr(self.counting_params, 'to_alipay_dict'):
                params['counting_params'] = self.counting_params.to_alipay_dict()
            else:
                params['counting_params'] = self.counting_params
        if self.counting_time:
            if hasattr(self.counting_time, 'to_alipay_dict'):
                params['counting_time'] = self.counting_time.to_alipay_dict()
            else:
                params['counting_time'] = self.counting_time
        if self.input_frame:
            if hasattr(self.input_frame, 'to_alipay_dict'):
                params['input_frame'] = self.input_frame.to_alipay_dict()
            else:
                params['input_frame'] = self.input_frame
        if self.input_template:
            if hasattr(self.input_template, 'to_alipay_dict'):
                params['input_template'] = self.input_template.to_alipay_dict()
            else:
                params['input_template'] = self.input_template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataBaiCargocountQueryModel()
        if 'camera_id' in d:
            o.camera_id = d['camera_id']
        if 'counting_params' in d:
            o.counting_params = d['counting_params']
        if 'counting_time' in d:
            o.counting_time = d['counting_time']
        if 'input_frame' in d:
            o.input_frame = d['input_frame']
        if 'input_template' in d:
            o.input_template = d['input_template']
        return o


