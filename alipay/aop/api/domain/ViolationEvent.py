#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ViolationEvent(object):

    def __init__(self):
        self._can_appeal = None
        self._can_rectify = None
        self._punish_action = None
        self._status = None
        self._target_id = None
        self._target_name = None
        self._target_type = None
        self._violation_record_id = None
        self._violation_time = None
        self._violation_type = None

    @property
    def can_appeal(self):
        return self._can_appeal

    @can_appeal.setter
    def can_appeal(self, value):
        self._can_appeal = value
    @property
    def can_rectify(self):
        return self._can_rectify

    @can_rectify.setter
    def can_rectify(self, value):
        self._can_rectify = value
    @property
    def punish_action(self):
        return self._punish_action

    @punish_action.setter
    def punish_action(self, value):
        self._punish_action = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def violation_record_id(self):
        return self._violation_record_id

    @violation_record_id.setter
    def violation_record_id(self, value):
        self._violation_record_id = value
    @property
    def violation_time(self):
        return self._violation_time

    @violation_time.setter
    def violation_time(self, value):
        self._violation_time = value
    @property
    def violation_type(self):
        return self._violation_type

    @violation_type.setter
    def violation_type(self, value):
        self._violation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_appeal:
            if hasattr(self.can_appeal, 'to_alipay_dict'):
                params['can_appeal'] = self.can_appeal.to_alipay_dict()
            else:
                params['can_appeal'] = self.can_appeal
        if self.can_rectify:
            if hasattr(self.can_rectify, 'to_alipay_dict'):
                params['can_rectify'] = self.can_rectify.to_alipay_dict()
            else:
                params['can_rectify'] = self.can_rectify
        if self.punish_action:
            if hasattr(self.punish_action, 'to_alipay_dict'):
                params['punish_action'] = self.punish_action.to_alipay_dict()
            else:
                params['punish_action'] = self.punish_action
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_name:
            if hasattr(self.target_name, 'to_alipay_dict'):
                params['target_name'] = self.target_name.to_alipay_dict()
            else:
                params['target_name'] = self.target_name
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        if self.violation_record_id:
            if hasattr(self.violation_record_id, 'to_alipay_dict'):
                params['violation_record_id'] = self.violation_record_id.to_alipay_dict()
            else:
                params['violation_record_id'] = self.violation_record_id
        if self.violation_time:
            if hasattr(self.violation_time, 'to_alipay_dict'):
                params['violation_time'] = self.violation_time.to_alipay_dict()
            else:
                params['violation_time'] = self.violation_time
        if self.violation_type:
            if hasattr(self.violation_type, 'to_alipay_dict'):
                params['violation_type'] = self.violation_type.to_alipay_dict()
            else:
                params['violation_type'] = self.violation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ViolationEvent()
        if 'can_appeal' in d:
            o.can_appeal = d['can_appeal']
        if 'can_rectify' in d:
            o.can_rectify = d['can_rectify']
        if 'punish_action' in d:
            o.punish_action = d['punish_action']
        if 'status' in d:
            o.status = d['status']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_name' in d:
            o.target_name = d['target_name']
        if 'target_type' in d:
            o.target_type = d['target_type']
        if 'violation_record_id' in d:
            o.violation_record_id = d['violation_record_id']
        if 'violation_time' in d:
            o.violation_time = d['violation_time']
        if 'violation_type' in d:
            o.violation_type = d['violation_type']
        return o


