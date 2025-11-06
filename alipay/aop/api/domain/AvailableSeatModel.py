#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvailableSeatModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._clv_user_id = None
        self._concurrency = None
        self._contact_id = None
        self._snap_shot_time = None
        self._type = None
        self._user_id = None
        self._work_skill_group_id = None
        self._work_status = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def clv_user_id(self):
        return self._clv_user_id

    @clv_user_id.setter
    def clv_user_id(self, value):
        self._clv_user_id = value
    @property
    def concurrency(self):
        return self._concurrency

    @concurrency.setter
    def concurrency(self, value):
        self._concurrency = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def snap_shot_time(self):
        return self._snap_shot_time

    @snap_shot_time.setter
    def snap_shot_time(self, value):
        self._snap_shot_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def work_skill_group_id(self):
        return self._work_skill_group_id

    @work_skill_group_id.setter
    def work_skill_group_id(self, value):
        self._work_skill_group_id = value
    @property
    def work_status(self):
        return self._work_status

    @work_status.setter
    def work_status(self, value):
        self._work_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.clv_user_id:
            if hasattr(self.clv_user_id, 'to_alipay_dict'):
                params['clv_user_id'] = self.clv_user_id.to_alipay_dict()
            else:
                params['clv_user_id'] = self.clv_user_id
        if self.concurrency:
            if hasattr(self.concurrency, 'to_alipay_dict'):
                params['concurrency'] = self.concurrency.to_alipay_dict()
            else:
                params['concurrency'] = self.concurrency
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.snap_shot_time:
            if hasattr(self.snap_shot_time, 'to_alipay_dict'):
                params['snap_shot_time'] = self.snap_shot_time.to_alipay_dict()
            else:
                params['snap_shot_time'] = self.snap_shot_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.work_skill_group_id:
            if hasattr(self.work_skill_group_id, 'to_alipay_dict'):
                params['work_skill_group_id'] = self.work_skill_group_id.to_alipay_dict()
            else:
                params['work_skill_group_id'] = self.work_skill_group_id
        if self.work_status:
            if hasattr(self.work_status, 'to_alipay_dict'):
                params['work_status'] = self.work_status.to_alipay_dict()
            else:
                params['work_status'] = self.work_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvailableSeatModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'clv_user_id' in d:
            o.clv_user_id = d['clv_user_id']
        if 'concurrency' in d:
            o.concurrency = d['concurrency']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'snap_shot_time' in d:
            o.snap_shot_time = d['snap_shot_time']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'work_skill_group_id' in d:
            o.work_skill_group_id = d['work_skill_group_id']
        if 'work_status' in d:
            o.work_status = d['work_status']
        return o


