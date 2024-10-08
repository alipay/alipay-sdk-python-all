#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderBundmeetingPassNotifyModel(object):

    def __init__(self):
        self._action = None
        self._activity_uuid = None
        self._appoint_time_uuid = None
        self._forum_uuid = None
        self._other_info = None
        self._post_info = None
        self._scene = None
        self._status = None
        self._uuid = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def activity_uuid(self):
        return self._activity_uuid

    @activity_uuid.setter
    def activity_uuid(self, value):
        self._activity_uuid = value
    @property
    def appoint_time_uuid(self):
        return self._appoint_time_uuid

    @appoint_time_uuid.setter
    def appoint_time_uuid(self, value):
        self._appoint_time_uuid = value
    @property
    def forum_uuid(self):
        return self._forum_uuid

    @forum_uuid.setter
    def forum_uuid(self, value):
        self._forum_uuid = value
    @property
    def other_info(self):
        return self._other_info

    @other_info.setter
    def other_info(self, value):
        self._other_info = value
    @property
    def post_info(self):
        return self._post_info

    @post_info.setter
    def post_info(self, value):
        self._post_info = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.activity_uuid:
            if hasattr(self.activity_uuid, 'to_alipay_dict'):
                params['activity_uuid'] = self.activity_uuid.to_alipay_dict()
            else:
                params['activity_uuid'] = self.activity_uuid
        if self.appoint_time_uuid:
            if hasattr(self.appoint_time_uuid, 'to_alipay_dict'):
                params['appoint_time_uuid'] = self.appoint_time_uuid.to_alipay_dict()
            else:
                params['appoint_time_uuid'] = self.appoint_time_uuid
        if self.forum_uuid:
            if hasattr(self.forum_uuid, 'to_alipay_dict'):
                params['forum_uuid'] = self.forum_uuid.to_alipay_dict()
            else:
                params['forum_uuid'] = self.forum_uuid
        if self.other_info:
            if hasattr(self.other_info, 'to_alipay_dict'):
                params['other_info'] = self.other_info.to_alipay_dict()
            else:
                params['other_info'] = self.other_info
        if self.post_info:
            if hasattr(self.post_info, 'to_alipay_dict'):
                params['post_info'] = self.post_info.to_alipay_dict()
            else:
                params['post_info'] = self.post_info
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderBundmeetingPassNotifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'activity_uuid' in d:
            o.activity_uuid = d['activity_uuid']
        if 'appoint_time_uuid' in d:
            o.appoint_time_uuid = d['appoint_time_uuid']
        if 'forum_uuid' in d:
            o.forum_uuid = d['forum_uuid']
        if 'other_info' in d:
            o.other_info = d['other_info']
        if 'post_info' in d:
            o.post_info = d['post_info']
        if 'scene' in d:
            o.scene = d['scene']
        if 'status' in d:
            o.status = d['status']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


