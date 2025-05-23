#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NCardAdvertiseTask(object):

    def __init__(self):
        self._advertise_type = None
        self._card_install_location = None
        self._desens_staff_name = None
        self._position_id = None
        self._position_name = None
        self._status = None
        self._tag_id = None
        self._task_id = None
        self._work_end_time = None
        self._work_start_time = None

    @property
    def advertise_type(self):
        return self._advertise_type

    @advertise_type.setter
    def advertise_type(self, value):
        self._advertise_type = value
    @property
    def card_install_location(self):
        return self._card_install_location

    @card_install_location.setter
    def card_install_location(self, value):
        self._card_install_location = value
    @property
    def desens_staff_name(self):
        return self._desens_staff_name

    @desens_staff_name.setter
    def desens_staff_name(self, value):
        self._desens_staff_name = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def position_name(self):
        return self._position_name

    @position_name.setter
    def position_name(self, value):
        self._position_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def work_end_time(self):
        return self._work_end_time

    @work_end_time.setter
    def work_end_time(self, value):
        self._work_end_time = value
    @property
    def work_start_time(self):
        return self._work_start_time

    @work_start_time.setter
    def work_start_time(self, value):
        self._work_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.advertise_type:
            if hasattr(self.advertise_type, 'to_alipay_dict'):
                params['advertise_type'] = self.advertise_type.to_alipay_dict()
            else:
                params['advertise_type'] = self.advertise_type
        if self.card_install_location:
            if hasattr(self.card_install_location, 'to_alipay_dict'):
                params['card_install_location'] = self.card_install_location.to_alipay_dict()
            else:
                params['card_install_location'] = self.card_install_location
        if self.desens_staff_name:
            if hasattr(self.desens_staff_name, 'to_alipay_dict'):
                params['desens_staff_name'] = self.desens_staff_name.to_alipay_dict()
            else:
                params['desens_staff_name'] = self.desens_staff_name
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.position_name:
            if hasattr(self.position_name, 'to_alipay_dict'):
                params['position_name'] = self.position_name.to_alipay_dict()
            else:
                params['position_name'] = self.position_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.work_end_time:
            if hasattr(self.work_end_time, 'to_alipay_dict'):
                params['work_end_time'] = self.work_end_time.to_alipay_dict()
            else:
                params['work_end_time'] = self.work_end_time
        if self.work_start_time:
            if hasattr(self.work_start_time, 'to_alipay_dict'):
                params['work_start_time'] = self.work_start_time.to_alipay_dict()
            else:
                params['work_start_time'] = self.work_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NCardAdvertiseTask()
        if 'advertise_type' in d:
            o.advertise_type = d['advertise_type']
        if 'card_install_location' in d:
            o.card_install_location = d['card_install_location']
        if 'desens_staff_name' in d:
            o.desens_staff_name = d['desens_staff_name']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'position_name' in d:
            o.position_name = d['position_name']
        if 'status' in d:
            o.status = d['status']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'work_end_time' in d:
            o.work_end_time = d['work_end_time']
        if 'work_start_time' in d:
            o.work_start_time = d['work_start_time']
        return o


