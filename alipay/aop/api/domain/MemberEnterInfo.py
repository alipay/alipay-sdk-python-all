#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberEnterInfo(object):

    def __init__(self):
        self._doctor_has_entered = None
        self._doctor_is_present = None
        self._patient_is_present = None
        self._video_conference_id = None

    @property
    def doctor_has_entered(self):
        return self._doctor_has_entered

    @doctor_has_entered.setter
    def doctor_has_entered(self, value):
        self._doctor_has_entered = value
    @property
    def doctor_is_present(self):
        return self._doctor_is_present

    @doctor_is_present.setter
    def doctor_is_present(self, value):
        self._doctor_is_present = value
    @property
    def patient_is_present(self):
        return self._patient_is_present

    @patient_is_present.setter
    def patient_is_present(self, value):
        self._patient_is_present = value
    @property
    def video_conference_id(self):
        return self._video_conference_id

    @video_conference_id.setter
    def video_conference_id(self, value):
        self._video_conference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_has_entered:
            if hasattr(self.doctor_has_entered, 'to_alipay_dict'):
                params['doctor_has_entered'] = self.doctor_has_entered.to_alipay_dict()
            else:
                params['doctor_has_entered'] = self.doctor_has_entered
        if self.doctor_is_present:
            if hasattr(self.doctor_is_present, 'to_alipay_dict'):
                params['doctor_is_present'] = self.doctor_is_present.to_alipay_dict()
            else:
                params['doctor_is_present'] = self.doctor_is_present
        if self.patient_is_present:
            if hasattr(self.patient_is_present, 'to_alipay_dict'):
                params['patient_is_present'] = self.patient_is_present.to_alipay_dict()
            else:
                params['patient_is_present'] = self.patient_is_present
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
        o = MemberEnterInfo()
        if 'doctor_has_entered' in d:
            o.doctor_has_entered = d['doctor_has_entered']
        if 'doctor_is_present' in d:
            o.doctor_is_present = d['doctor_is_present']
        if 'patient_is_present' in d:
            o.patient_is_present = d['patient_is_present']
        if 'video_conference_id' in d:
            o.video_conference_id = d['video_conference_id']
        return o


