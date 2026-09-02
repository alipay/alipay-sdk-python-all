#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzSdkEventRatioDTO(object):

    def __init__(self):
        self._event_code = None
        self._event_id_event_count = None
        self._event_id_event_rate = None
        self._event_id_event_rate_result = None
        self._event_name = None
        self._event_occur_date = None
        self._medical_institution_name = None
        self._registration_count = None
        self._serial_no_event_count = None
        self._serial_no_event_rate = None
        self._serial_no_event_rate_result = None
        self._uscc = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_id_event_count(self):
        return self._event_id_event_count

    @event_id_event_count.setter
    def event_id_event_count(self, value):
        self._event_id_event_count = value
    @property
    def event_id_event_rate(self):
        return self._event_id_event_rate

    @event_id_event_rate.setter
    def event_id_event_rate(self, value):
        self._event_id_event_rate = value
    @property
    def event_id_event_rate_result(self):
        return self._event_id_event_rate_result

    @event_id_event_rate_result.setter
    def event_id_event_rate_result(self, value):
        self._event_id_event_rate_result = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def event_occur_date(self):
        return self._event_occur_date

    @event_occur_date.setter
    def event_occur_date(self, value):
        self._event_occur_date = value
    @property
    def medical_institution_name(self):
        return self._medical_institution_name

    @medical_institution_name.setter
    def medical_institution_name(self, value):
        self._medical_institution_name = value
    @property
    def registration_count(self):
        return self._registration_count

    @registration_count.setter
    def registration_count(self, value):
        self._registration_count = value
    @property
    def serial_no_event_count(self):
        return self._serial_no_event_count

    @serial_no_event_count.setter
    def serial_no_event_count(self, value):
        self._serial_no_event_count = value
    @property
    def serial_no_event_rate(self):
        return self._serial_no_event_rate

    @serial_no_event_rate.setter
    def serial_no_event_rate(self, value):
        self._serial_no_event_rate = value
    @property
    def serial_no_event_rate_result(self):
        return self._serial_no_event_rate_result

    @serial_no_event_rate_result.setter
    def serial_no_event_rate_result(self, value):
        self._serial_no_event_rate_result = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_id_event_count:
            if hasattr(self.event_id_event_count, 'to_alipay_dict'):
                params['event_id_event_count'] = self.event_id_event_count.to_alipay_dict()
            else:
                params['event_id_event_count'] = self.event_id_event_count
        if self.event_id_event_rate:
            if hasattr(self.event_id_event_rate, 'to_alipay_dict'):
                params['event_id_event_rate'] = self.event_id_event_rate.to_alipay_dict()
            else:
                params['event_id_event_rate'] = self.event_id_event_rate
        if self.event_id_event_rate_result:
            if hasattr(self.event_id_event_rate_result, 'to_alipay_dict'):
                params['event_id_event_rate_result'] = self.event_id_event_rate_result.to_alipay_dict()
            else:
                params['event_id_event_rate_result'] = self.event_id_event_rate_result
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.event_occur_date:
            if hasattr(self.event_occur_date, 'to_alipay_dict'):
                params['event_occur_date'] = self.event_occur_date.to_alipay_dict()
            else:
                params['event_occur_date'] = self.event_occur_date
        if self.medical_institution_name:
            if hasattr(self.medical_institution_name, 'to_alipay_dict'):
                params['medical_institution_name'] = self.medical_institution_name.to_alipay_dict()
            else:
                params['medical_institution_name'] = self.medical_institution_name
        if self.registration_count:
            if hasattr(self.registration_count, 'to_alipay_dict'):
                params['registration_count'] = self.registration_count.to_alipay_dict()
            else:
                params['registration_count'] = self.registration_count
        if self.serial_no_event_count:
            if hasattr(self.serial_no_event_count, 'to_alipay_dict'):
                params['serial_no_event_count'] = self.serial_no_event_count.to_alipay_dict()
            else:
                params['serial_no_event_count'] = self.serial_no_event_count
        if self.serial_no_event_rate:
            if hasattr(self.serial_no_event_rate, 'to_alipay_dict'):
                params['serial_no_event_rate'] = self.serial_no_event_rate.to_alipay_dict()
            else:
                params['serial_no_event_rate'] = self.serial_no_event_rate
        if self.serial_no_event_rate_result:
            if hasattr(self.serial_no_event_rate_result, 'to_alipay_dict'):
                params['serial_no_event_rate_result'] = self.serial_no_event_rate_result.to_alipay_dict()
            else:
                params['serial_no_event_rate_result'] = self.serial_no_event_rate_result
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
        o = YpzSdkEventRatioDTO()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_id_event_count' in d:
            o.event_id_event_count = d['event_id_event_count']
        if 'event_id_event_rate' in d:
            o.event_id_event_rate = d['event_id_event_rate']
        if 'event_id_event_rate_result' in d:
            o.event_id_event_rate_result = d['event_id_event_rate_result']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'event_occur_date' in d:
            o.event_occur_date = d['event_occur_date']
        if 'medical_institution_name' in d:
            o.medical_institution_name = d['medical_institution_name']
        if 'registration_count' in d:
            o.registration_count = d['registration_count']
        if 'serial_no_event_count' in d:
            o.serial_no_event_count = d['serial_no_event_count']
        if 'serial_no_event_rate' in d:
            o.serial_no_event_rate = d['serial_no_event_rate']
        if 'serial_no_event_rate_result' in d:
            o.serial_no_event_rate_result = d['serial_no_event_rate_result']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


