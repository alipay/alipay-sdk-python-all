#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConferenceInfo(object):

    def __init__(self):
        self._duration = None
        self._remaining_duration = None
        self._remaining_scheduled_start_duration = None
        self._status = None
        self._video_conference_id = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def remaining_duration(self):
        return self._remaining_duration

    @remaining_duration.setter
    def remaining_duration(self, value):
        self._remaining_duration = value
    @property
    def remaining_scheduled_start_duration(self):
        return self._remaining_scheduled_start_duration

    @remaining_scheduled_start_duration.setter
    def remaining_scheduled_start_duration(self, value):
        self._remaining_scheduled_start_duration = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def video_conference_id(self):
        return self._video_conference_id

    @video_conference_id.setter
    def video_conference_id(self, value):
        self._video_conference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.remaining_duration:
            if hasattr(self.remaining_duration, 'to_alipay_dict'):
                params['remaining_duration'] = self.remaining_duration.to_alipay_dict()
            else:
                params['remaining_duration'] = self.remaining_duration
        if self.remaining_scheduled_start_duration:
            if hasattr(self.remaining_scheduled_start_duration, 'to_alipay_dict'):
                params['remaining_scheduled_start_duration'] = self.remaining_scheduled_start_duration.to_alipay_dict()
            else:
                params['remaining_scheduled_start_duration'] = self.remaining_scheduled_start_duration
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.video_conference_id:
            if hasattr(self.video_conference_id, 'to_alipay_dict'):
                params['video_conference_id'] = self.video_conference_id.to_alipay_dict()
            else:
                params['video_conference_id'] = self.video_conference_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConferenceInfo()
        if 'duration' in d:
            o.duration = d['duration']
        if 'remaining_duration' in d:
            o.remaining_duration = d['remaining_duration']
        if 'remaining_scheduled_start_duration' in d:
            o.remaining_scheduled_start_duration = d['remaining_scheduled_start_duration']
        if 'status' in d:
            o.status = d['status']
        if 'video_conference_id' in d:
            o.video_conference_id = d['video_conference_id']
        return o


