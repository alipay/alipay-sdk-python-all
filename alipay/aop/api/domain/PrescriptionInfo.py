#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrescriptionInfo(object):

    def __init__(self):
        self._activity_id = None
        self._channel = None
        self._diet_plan = None
        self._exercise_plan = None
        self._prescription_generate_time = None
        self._prescription_id = None
        self._prescription_name = None
        self._psychology_plan = None
        self._sleep_plan = None
        self._status = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def diet_plan(self):
        return self._diet_plan

    @diet_plan.setter
    def diet_plan(self, value):
        self._diet_plan = value
    @property
    def exercise_plan(self):
        return self._exercise_plan

    @exercise_plan.setter
    def exercise_plan(self, value):
        self._exercise_plan = value
    @property
    def prescription_generate_time(self):
        return self._prescription_generate_time

    @prescription_generate_time.setter
    def prescription_generate_time(self, value):
        self._prescription_generate_time = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def prescription_name(self):
        return self._prescription_name

    @prescription_name.setter
    def prescription_name(self, value):
        self._prescription_name = value
    @property
    def psychology_plan(self):
        return self._psychology_plan

    @psychology_plan.setter
    def psychology_plan(self, value):
        self._psychology_plan = value
    @property
    def sleep_plan(self):
        return self._sleep_plan

    @sleep_plan.setter
    def sleep_plan(self, value):
        self._sleep_plan = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.diet_plan:
            if hasattr(self.diet_plan, 'to_alipay_dict'):
                params['diet_plan'] = self.diet_plan.to_alipay_dict()
            else:
                params['diet_plan'] = self.diet_plan
        if self.exercise_plan:
            if hasattr(self.exercise_plan, 'to_alipay_dict'):
                params['exercise_plan'] = self.exercise_plan.to_alipay_dict()
            else:
                params['exercise_plan'] = self.exercise_plan
        if self.prescription_generate_time:
            if hasattr(self.prescription_generate_time, 'to_alipay_dict'):
                params['prescription_generate_time'] = self.prescription_generate_time.to_alipay_dict()
            else:
                params['prescription_generate_time'] = self.prescription_generate_time
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.prescription_name:
            if hasattr(self.prescription_name, 'to_alipay_dict'):
                params['prescription_name'] = self.prescription_name.to_alipay_dict()
            else:
                params['prescription_name'] = self.prescription_name
        if self.psychology_plan:
            if hasattr(self.psychology_plan, 'to_alipay_dict'):
                params['psychology_plan'] = self.psychology_plan.to_alipay_dict()
            else:
                params['psychology_plan'] = self.psychology_plan
        if self.sleep_plan:
            if hasattr(self.sleep_plan, 'to_alipay_dict'):
                params['sleep_plan'] = self.sleep_plan.to_alipay_dict()
            else:
                params['sleep_plan'] = self.sleep_plan
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrescriptionInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'diet_plan' in d:
            o.diet_plan = d['diet_plan']
        if 'exercise_plan' in d:
            o.exercise_plan = d['exercise_plan']
        if 'prescription_generate_time' in d:
            o.prescription_generate_time = d['prescription_generate_time']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'prescription_name' in d:
            o.prescription_name = d['prescription_name']
        if 'psychology_plan' in d:
            o.psychology_plan = d['psychology_plan']
        if 'sleep_plan' in d:
            o.sleep_plan = d['sleep_plan']
        if 'status' in d:
            o.status = d['status']
        return o


