#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallRecordDetail(object):

    def __init__(self):
        self._call_duration = None
        self._contact_status = None
        self._intent_description = None
        self._message_type = None
        self._meter_num = None
        self._meter_unit = None
        self._mobile = None

    @property
    def call_duration(self):
        return self._call_duration

    @call_duration.setter
    def call_duration(self, value):
        self._call_duration = value
    @property
    def contact_status(self):
        return self._contact_status

    @contact_status.setter
    def contact_status(self, value):
        self._contact_status = value
    @property
    def intent_description(self):
        return self._intent_description

    @intent_description.setter
    def intent_description(self, value):
        self._intent_description = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value
    @property
    def meter_num(self):
        return self._meter_num

    @meter_num.setter
    def meter_num(self, value):
        self._meter_num = value
    @property
    def meter_unit(self):
        return self._meter_unit

    @meter_unit.setter
    def meter_unit(self, value):
        self._meter_unit = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_duration:
            if hasattr(self.call_duration, 'to_alipay_dict'):
                params['call_duration'] = self.call_duration.to_alipay_dict()
            else:
                params['call_duration'] = self.call_duration
        if self.contact_status:
            if hasattr(self.contact_status, 'to_alipay_dict'):
                params['contact_status'] = self.contact_status.to_alipay_dict()
            else:
                params['contact_status'] = self.contact_status
        if self.intent_description:
            if hasattr(self.intent_description, 'to_alipay_dict'):
                params['intent_description'] = self.intent_description.to_alipay_dict()
            else:
                params['intent_description'] = self.intent_description
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        if self.meter_num:
            if hasattr(self.meter_num, 'to_alipay_dict'):
                params['meter_num'] = self.meter_num.to_alipay_dict()
            else:
                params['meter_num'] = self.meter_num
        if self.meter_unit:
            if hasattr(self.meter_unit, 'to_alipay_dict'):
                params['meter_unit'] = self.meter_unit.to_alipay_dict()
            else:
                params['meter_unit'] = self.meter_unit
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallRecordDetail()
        if 'call_duration' in d:
            o.call_duration = d['call_duration']
        if 'contact_status' in d:
            o.contact_status = d['contact_status']
        if 'intent_description' in d:
            o.intent_description = d['intent_description']
        if 'message_type' in d:
            o.message_type = d['message_type']
        if 'meter_num' in d:
            o.meter_num = d['meter_num']
        if 'meter_unit' in d:
            o.meter_unit = d['meter_unit']
        if 'mobile' in d:
            o.mobile = d['mobile']
        return o


