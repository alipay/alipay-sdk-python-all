#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzSdkEventProblemDTO(object):

    def __init__(self):
        self._appointment_no = None
        self._appointment_time = None
        self._campus_code = None
        self._campus_name = None
        self._correct_example = None
        self._event_code = None
        self._event_identifier = None
        self._event_name = None
        self._event_occur_time = None
        self._event_update_time = None
        self._gmt_create = None
        self._medical_institution_name = None
        self._problem_description = None
        self._problem_field = None
        self._registration_no = None
        self._registration_time = None
        self._uscc = None

    @property
    def appointment_no(self):
        return self._appointment_no

    @appointment_no.setter
    def appointment_no(self, value):
        self._appointment_no = value
    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        self._appointment_time = value
    @property
    def campus_code(self):
        return self._campus_code

    @campus_code.setter
    def campus_code(self, value):
        self._campus_code = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def correct_example(self):
        return self._correct_example

    @correct_example.setter
    def correct_example(self, value):
        self._correct_example = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_identifier(self):
        return self._event_identifier

    @event_identifier.setter
    def event_identifier(self, value):
        self._event_identifier = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def event_occur_time(self):
        return self._event_occur_time

    @event_occur_time.setter
    def event_occur_time(self, value):
        self._event_occur_time = value
    @property
    def event_update_time(self):
        return self._event_update_time

    @event_update_time.setter
    def event_update_time(self, value):
        self._event_update_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def medical_institution_name(self):
        return self._medical_institution_name

    @medical_institution_name.setter
    def medical_institution_name(self, value):
        self._medical_institution_name = value
    @property
    def problem_description(self):
        return self._problem_description

    @problem_description.setter
    def problem_description(self, value):
        self._problem_description = value
    @property
    def problem_field(self):
        return self._problem_field

    @problem_field.setter
    def problem_field(self, value):
        self._problem_field = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def registration_time(self):
        return self._registration_time

    @registration_time.setter
    def registration_time(self, value):
        self._registration_time = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_no:
            if hasattr(self.appointment_no, 'to_alipay_dict'):
                params['appointment_no'] = self.appointment_no.to_alipay_dict()
            else:
                params['appointment_no'] = self.appointment_no
        if self.appointment_time:
            if hasattr(self.appointment_time, 'to_alipay_dict'):
                params['appointment_time'] = self.appointment_time.to_alipay_dict()
            else:
                params['appointment_time'] = self.appointment_time
        if self.campus_code:
            if hasattr(self.campus_code, 'to_alipay_dict'):
                params['campus_code'] = self.campus_code.to_alipay_dict()
            else:
                params['campus_code'] = self.campus_code
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.correct_example:
            if hasattr(self.correct_example, 'to_alipay_dict'):
                params['correct_example'] = self.correct_example.to_alipay_dict()
            else:
                params['correct_example'] = self.correct_example
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_identifier:
            if hasattr(self.event_identifier, 'to_alipay_dict'):
                params['event_identifier'] = self.event_identifier.to_alipay_dict()
            else:
                params['event_identifier'] = self.event_identifier
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.event_occur_time:
            if hasattr(self.event_occur_time, 'to_alipay_dict'):
                params['event_occur_time'] = self.event_occur_time.to_alipay_dict()
            else:
                params['event_occur_time'] = self.event_occur_time
        if self.event_update_time:
            if hasattr(self.event_update_time, 'to_alipay_dict'):
                params['event_update_time'] = self.event_update_time.to_alipay_dict()
            else:
                params['event_update_time'] = self.event_update_time
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.medical_institution_name:
            if hasattr(self.medical_institution_name, 'to_alipay_dict'):
                params['medical_institution_name'] = self.medical_institution_name.to_alipay_dict()
            else:
                params['medical_institution_name'] = self.medical_institution_name
        if self.problem_description:
            if hasattr(self.problem_description, 'to_alipay_dict'):
                params['problem_description'] = self.problem_description.to_alipay_dict()
            else:
                params['problem_description'] = self.problem_description
        if self.problem_field:
            if hasattr(self.problem_field, 'to_alipay_dict'):
                params['problem_field'] = self.problem_field.to_alipay_dict()
            else:
                params['problem_field'] = self.problem_field
        if self.registration_no:
            if hasattr(self.registration_no, 'to_alipay_dict'):
                params['registration_no'] = self.registration_no.to_alipay_dict()
            else:
                params['registration_no'] = self.registration_no
        if self.registration_time:
            if hasattr(self.registration_time, 'to_alipay_dict'):
                params['registration_time'] = self.registration_time.to_alipay_dict()
            else:
                params['registration_time'] = self.registration_time
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzSdkEventProblemDTO()
        if 'appointment_no' in d:
            o.appointment_no = d['appointment_no']
        if 'appointment_time' in d:
            o.appointment_time = d['appointment_time']
        if 'campus_code' in d:
            o.campus_code = d['campus_code']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'correct_example' in d:
            o.correct_example = d['correct_example']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_identifier' in d:
            o.event_identifier = d['event_identifier']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'event_occur_time' in d:
            o.event_occur_time = d['event_occur_time']
        if 'event_update_time' in d:
            o.event_update_time = d['event_update_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'medical_institution_name' in d:
            o.medical_institution_name = d['medical_institution_name']
        if 'problem_description' in d:
            o.problem_description = d['problem_description']
        if 'problem_field' in d:
            o.problem_field = d['problem_field']
        if 'registration_no' in d:
            o.registration_no = d['registration_no']
        if 'registration_time' in d:
            o.registration_time = d['registration_time']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


