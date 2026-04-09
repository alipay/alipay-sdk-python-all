#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActSignUpRecord(object):

    def __init__(self):
        self._activity_code = None
        self._activity_round_end_time = None
        self._activity_round_start_time = None
        self._activity_user_end_time = None
        self._activity_user_start_time = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._round_id = None
        self._status = None
        self._subject_id = None
        self._subject_type = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_round_end_time(self):
        return self._activity_round_end_time

    @activity_round_end_time.setter
    def activity_round_end_time(self, value):
        self._activity_round_end_time = value
    @property
    def activity_round_start_time(self):
        return self._activity_round_start_time

    @activity_round_start_time.setter
    def activity_round_start_time(self, value):
        self._activity_round_start_time = value
    @property
    def activity_user_end_time(self):
        return self._activity_user_end_time

    @activity_user_end_time.setter
    def activity_user_end_time(self, value):
        self._activity_user_end_time = value
    @property
    def activity_user_start_time(self):
        return self._activity_user_start_time

    @activity_user_start_time.setter
    def activity_user_start_time(self, value):
        self._activity_user_start_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def round_id(self):
        return self._round_id

    @round_id.setter
    def round_id(self, value):
        self._round_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.activity_round_end_time:
            if hasattr(self.activity_round_end_time, 'to_alipay_dict'):
                params['activity_round_end_time'] = self.activity_round_end_time.to_alipay_dict()
            else:
                params['activity_round_end_time'] = self.activity_round_end_time
        if self.activity_round_start_time:
            if hasattr(self.activity_round_start_time, 'to_alipay_dict'):
                params['activity_round_start_time'] = self.activity_round_start_time.to_alipay_dict()
            else:
                params['activity_round_start_time'] = self.activity_round_start_time
        if self.activity_user_end_time:
            if hasattr(self.activity_user_end_time, 'to_alipay_dict'):
                params['activity_user_end_time'] = self.activity_user_end_time.to_alipay_dict()
            else:
                params['activity_user_end_time'] = self.activity_user_end_time
        if self.activity_user_start_time:
            if hasattr(self.activity_user_start_time, 'to_alipay_dict'):
                params['activity_user_start_time'] = self.activity_user_start_time.to_alipay_dict()
            else:
                params['activity_user_start_time'] = self.activity_user_start_time
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.round_id:
            if hasattr(self.round_id, 'to_alipay_dict'):
                params['round_id'] = self.round_id.to_alipay_dict()
            else:
                params['round_id'] = self.round_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActSignUpRecord()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'activity_round_end_time' in d:
            o.activity_round_end_time = d['activity_round_end_time']
        if 'activity_round_start_time' in d:
            o.activity_round_start_time = d['activity_round_start_time']
        if 'activity_user_end_time' in d:
            o.activity_user_end_time = d['activity_user_end_time']
        if 'activity_user_start_time' in d:
            o.activity_user_start_time = d['activity_user_start_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'round_id' in d:
            o.round_id = d['round_id']
        if 'status' in d:
            o.status = d['status']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        return o


