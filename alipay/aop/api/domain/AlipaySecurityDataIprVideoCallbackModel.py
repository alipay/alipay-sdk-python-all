#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VideoData import VideoData


class AlipaySecurityDataIprVideoCallbackModel(object):

    def __init__(self):
        self._channel = None
        self._task_id = None
        self._video_list = None
        self._video_status = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def video_list(self):
        return self._video_list

    @video_list.setter
    def video_list(self, value):
        if isinstance(value, list):
            self._video_list = list()
            for i in value:
                if isinstance(i, VideoData):
                    self._video_list.append(i)
                else:
                    self._video_list.append(VideoData.from_alipay_dict(i))
    @property
    def video_status(self):
        return self._video_status

    @video_status.setter
    def video_status(self, value):
        self._video_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.video_list:
            if isinstance(self.video_list, list):
                for i in range(0, len(self.video_list)):
                    element = self.video_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_list[i] = element.to_alipay_dict()
            if hasattr(self.video_list, 'to_alipay_dict'):
                params['video_list'] = self.video_list.to_alipay_dict()
            else:
                params['video_list'] = self.video_list
        if self.video_status:
            if hasattr(self.video_status, 'to_alipay_dict'):
                params['video_status'] = self.video_status.to_alipay_dict()
            else:
                params['video_status'] = self.video_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataIprVideoCallbackModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'video_list' in d:
            o.video_list = d['video_list']
        if 'video_status' in d:
            o.video_status = d['video_status']
        return o


