#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobdeliverModifyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._comment = None
        self._content_var = None
        self._interview_location = None
        self._interview_time = None
        self._latitude = None
        self._longitude = None
        self._source_code = None
        self._source_id = None
        self._status = None
        self._update_time = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value
    @property
    def interview_location(self):
        return self._interview_location

    @interview_location.setter
    def interview_location(self, value):
        self._interview_location = value
    @property
    def interview_time(self):
        return self._interview_time

    @interview_time.setter
    def interview_time(self, value):
        self._interview_time = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.content_var:
            if hasattr(self.content_var, 'to_alipay_dict'):
                params['content_var'] = self.content_var.to_alipay_dict()
            else:
                params['content_var'] = self.content_var
        if self.interview_location:
            if hasattr(self.interview_location, 'to_alipay_dict'):
                params['interview_location'] = self.interview_location.to_alipay_dict()
            else:
                params['interview_location'] = self.interview_location
        if self.interview_time:
            if hasattr(self.interview_time, 'to_alipay_dict'):
                params['interview_time'] = self.interview_time.to_alipay_dict()
            else:
                params['interview_time'] = self.interview_time
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduCampusJobdeliverModifyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'comment' in d:
            o.comment = d['comment']
        if 'content_var' in d:
            o.content_var = d['content_var']
        if 'interview_location' in d:
            o.interview_location = d['interview_location']
        if 'interview_time' in d:
            o.interview_time = d['interview_time']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'source_code' in d:
            o.source_code = d['source_code']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'status' in d:
            o.status = d['status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


