#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcVideoconferenceRestartModel(object):

    def __init__(self):
        self._role = None
        self._source_type = None
        self._space_id = None
        self._user_id = None
        self._video_conference_id = None

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def video_conference_id(self):
        return self._video_conference_id

    @video_conference_id.setter
    def video_conference_id(self, value):
        self._video_conference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = AlipayCommerceMedicalHdfrtcVideoconferenceRestartModel()
        if 'role' in d:
            o.role = d['role']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'space_id' in d:
            o.space_id = d['space_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'video_conference_id' in d:
            o.video_conference_id = d['video_conference_id']
        return o


