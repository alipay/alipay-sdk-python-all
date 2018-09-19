#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CraftsmanWorkCreateOpenModel(object):

    def __init__(self):
        self._duration = None
        self._media_id = None
        self._media_type = None
        self._out_work_id = None
        self._title = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def media_id(self):
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        self._media_id = value
    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        self._media_type = value
    @property
    def out_work_id(self):
        return self._out_work_id

    @out_work_id.setter
    def out_work_id(self, value):
        self._out_work_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.media_id:
            if hasattr(self.media_id, 'to_alipay_dict'):
                params['media_id'] = self.media_id.to_alipay_dict()
            else:
                params['media_id'] = self.media_id
        if self.media_type:
            if hasattr(self.media_type, 'to_alipay_dict'):
                params['media_type'] = self.media_type.to_alipay_dict()
            else:
                params['media_type'] = self.media_type
        if self.out_work_id:
            if hasattr(self.out_work_id, 'to_alipay_dict'):
                params['out_work_id'] = self.out_work_id.to_alipay_dict()
            else:
                params['out_work_id'] = self.out_work_id
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
        o = CraftsmanWorkCreateOpenModel()
        if 'duration' in d:
            o.duration = d['duration']
        if 'media_id' in d:
            o.media_id = d['media_id']
        if 'media_type' in d:
            o.media_type = d['media_type']
        if 'out_work_id' in d:
            o.out_work_id = d['out_work_id']
        if 'title' in d:
            o.title = d['title']
        return o


