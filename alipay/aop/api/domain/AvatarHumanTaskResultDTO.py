#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvatarHumanTaskResultDTO(object):

    def __init__(self):
        self._duration = None
        self._error_msg = None
        self._final_video_url = None
        self._id = None
        self._preview = None
        self._status = None
        self._video_name = None
        self._video_type = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def final_video_url(self):
        return self._final_video_url

    @final_video_url.setter
    def final_video_url(self, value):
        self._final_video_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def preview(self):
        return self._preview

    @preview.setter
    def preview(self, value):
        self._preview = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def video_name(self):
        return self._video_name

    @video_name.setter
    def video_name(self, value):
        self._video_name = value
    @property
    def video_type(self):
        return self._video_type

    @video_type.setter
    def video_type(self, value):
        self._video_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.final_video_url:
            if hasattr(self.final_video_url, 'to_alipay_dict'):
                params['final_video_url'] = self.final_video_url.to_alipay_dict()
            else:
                params['final_video_url'] = self.final_video_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.preview:
            if hasattr(self.preview, 'to_alipay_dict'):
                params['preview'] = self.preview.to_alipay_dict()
            else:
                params['preview'] = self.preview
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.video_name:
            if hasattr(self.video_name, 'to_alipay_dict'):
                params['video_name'] = self.video_name.to_alipay_dict()
            else:
                params['video_name'] = self.video_name
        if self.video_type:
            if hasattr(self.video_type, 'to_alipay_dict'):
                params['video_type'] = self.video_type.to_alipay_dict()
            else:
                params['video_type'] = self.video_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvatarHumanTaskResultDTO()
        if 'duration' in d:
            o.duration = d['duration']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'final_video_url' in d:
            o.final_video_url = d['final_video_url']
        if 'id' in d:
            o.id = d['id']
        if 'preview' in d:
            o.preview = d['preview']
        if 'status' in d:
            o.status = d['status']
        if 'video_name' in d:
            o.video_name = d['video_name']
        if 'video_type' in d:
            o.video_type = d['video_type']
        return o


