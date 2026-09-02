#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeatherAlertDTO(object):

    def __init__(self):
        self._alert_code = None
        self._alert_id = None
        self._alert_name = None
        self._certainty = None
        self._criteria = None
        self._description = None
        self._effective_time = None
        self._expire_time = None
        self._headline = None
        self._onset_time = None

    @property
    def alert_code(self):
        return self._alert_code

    @alert_code.setter
    def alert_code(self, value):
        self._alert_code = value
    @property
    def alert_id(self):
        return self._alert_id

    @alert_id.setter
    def alert_id(self, value):
        self._alert_id = value
    @property
    def alert_name(self):
        return self._alert_name

    @alert_name.setter
    def alert_name(self, value):
        self._alert_name = value
    @property
    def certainty(self):
        return self._certainty

    @certainty.setter
    def certainty(self, value):
        self._certainty = value
    @property
    def criteria(self):
        return self._criteria

    @criteria.setter
    def criteria(self, value):
        self._criteria = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, value):
        self._headline = value
    @property
    def onset_time(self):
        return self._onset_time

    @onset_time.setter
    def onset_time(self, value):
        self._onset_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_code:
            if hasattr(self.alert_code, 'to_alipay_dict'):
                params['alert_code'] = self.alert_code.to_alipay_dict()
            else:
                params['alert_code'] = self.alert_code
        if self.alert_id:
            if hasattr(self.alert_id, 'to_alipay_dict'):
                params['alert_id'] = self.alert_id.to_alipay_dict()
            else:
                params['alert_id'] = self.alert_id
        if self.alert_name:
            if hasattr(self.alert_name, 'to_alipay_dict'):
                params['alert_name'] = self.alert_name.to_alipay_dict()
            else:
                params['alert_name'] = self.alert_name
        if self.certainty:
            if hasattr(self.certainty, 'to_alipay_dict'):
                params['certainty'] = self.certainty.to_alipay_dict()
            else:
                params['certainty'] = self.certainty
        if self.criteria:
            if hasattr(self.criteria, 'to_alipay_dict'):
                params['criteria'] = self.criteria.to_alipay_dict()
            else:
                params['criteria'] = self.criteria
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.headline:
            if hasattr(self.headline, 'to_alipay_dict'):
                params['headline'] = self.headline.to_alipay_dict()
            else:
                params['headline'] = self.headline
        if self.onset_time:
            if hasattr(self.onset_time, 'to_alipay_dict'):
                params['onset_time'] = self.onset_time.to_alipay_dict()
            else:
                params['onset_time'] = self.onset_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WeatherAlertDTO()
        if 'alert_code' in d:
            o.alert_code = d['alert_code']
        if 'alert_id' in d:
            o.alert_id = d['alert_id']
        if 'alert_name' in d:
            o.alert_name = d['alert_name']
        if 'certainty' in d:
            o.certainty = d['certainty']
        if 'criteria' in d:
            o.criteria = d['criteria']
        if 'description' in d:
            o.description = d['description']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'headline' in d:
            o.headline = d['headline']
        if 'onset_time' in d:
            o.onset_time = d['onset_time']
        return o


