#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CraftsmanWorkOpenModel(object):

    def __init__(self):
        self._craftsman_id = None
        self._duration = None
        self._media_id = None
        self._media_type = None
        self._status = None
        self._title = None
        self._work_id = None

    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CraftsmanWorkOpenModel()
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'duration' in d:
            o.duration = d['duration']
        if 'media_id' in d:
            o.media_id = d['media_id']
        if 'media_type' in d:
            o.media_type = d['media_type']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'work_id' in d:
            o.work_id = d['work_id']
        return o


