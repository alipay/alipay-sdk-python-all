#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PatientDetails(object):

    def __init__(self):
        self._has_enter_room = None
        self._patient_id = None
        self._rtc_user_id = None
        self._user_id = None

    @property
    def has_enter_room(self):
        return self._has_enter_room

    @has_enter_room.setter
    def has_enter_room(self, value):
        self._has_enter_room = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def rtc_user_id(self):
        return self._rtc_user_id

    @rtc_user_id.setter
    def rtc_user_id(self, value):
        self._rtc_user_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_enter_room:
            if hasattr(self.has_enter_room, 'to_alipay_dict'):
                params['has_enter_room'] = self.has_enter_room.to_alipay_dict()
            else:
                params['has_enter_room'] = self.has_enter_room
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.rtc_user_id:
            if hasattr(self.rtc_user_id, 'to_alipay_dict'):
                params['rtc_user_id'] = self.rtc_user_id.to_alipay_dict()
            else:
                params['rtc_user_id'] = self.rtc_user_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PatientDetails()
        if 'has_enter_room' in d:
            o.has_enter_room = d['has_enter_room']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'rtc_user_id' in d:
            o.rtc_user_id = d['rtc_user_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


