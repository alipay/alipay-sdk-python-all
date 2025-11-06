#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcVideoconferenceModifyModel(object):

    def __init__(self):
        self._real_end_time = None
        self._source_type = None
        self._status = None
        self._video_conference_id = None

    @property
    def real_end_time(self):
        return self._real_end_time

    @real_end_time.setter
    def real_end_time(self, value):
        self._real_end_time = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
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
        if self.real_end_time:
            if hasattr(self.real_end_time, 'to_alipay_dict'):
                params['real_end_time'] = self.real_end_time.to_alipay_dict()
            else:
                params['real_end_time'] = self.real_end_time
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
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
        o = AlipayCommerceMedicalHdfrtcVideoconferenceModifyModel()
        if 'real_end_time' in d:
            o.real_end_time = d['real_end_time']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'status' in d:
            o.status = d['status']
        if 'video_conference_id' in d:
            o.video_conference_id = d['video_conference_id']
        return o


