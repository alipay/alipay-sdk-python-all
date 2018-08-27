#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HoloGraphicContactInfo(object):

    def __init__(self):
        self._call_frequency = None
        self._call_time = None
        self._called_frequency = None
        self._called_time = None
        self._mobile = None
        self._talk_frequency = None
        self._talk_time = None

    @property
    def call_frequency(self):
        return self._call_frequency

    @call_frequency.setter
    def call_frequency(self, value):
        self._call_frequency = value
    @property
    def call_time(self):
        return self._call_time

    @call_time.setter
    def call_time(self, value):
        self._call_time = value
    @property
    def called_frequency(self):
        return self._called_frequency

    @called_frequency.setter
    def called_frequency(self, value):
        self._called_frequency = value
    @property
    def called_time(self):
        return self._called_time

    @called_time.setter
    def called_time(self, value):
        self._called_time = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def talk_frequency(self):
        return self._talk_frequency

    @talk_frequency.setter
    def talk_frequency(self, value):
        self._talk_frequency = value
    @property
    def talk_time(self):
        return self._talk_time

    @talk_time.setter
    def talk_time(self, value):
        self._talk_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_frequency:
            if hasattr(self.call_frequency, 'to_alipay_dict'):
                params['call_frequency'] = self.call_frequency.to_alipay_dict()
            else:
                params['call_frequency'] = self.call_frequency
        if self.call_time:
            if hasattr(self.call_time, 'to_alipay_dict'):
                params['call_time'] = self.call_time.to_alipay_dict()
            else:
                params['call_time'] = self.call_time
        if self.called_frequency:
            if hasattr(self.called_frequency, 'to_alipay_dict'):
                params['called_frequency'] = self.called_frequency.to_alipay_dict()
            else:
                params['called_frequency'] = self.called_frequency
        if self.called_time:
            if hasattr(self.called_time, 'to_alipay_dict'):
                params['called_time'] = self.called_time.to_alipay_dict()
            else:
                params['called_time'] = self.called_time
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.talk_frequency:
            if hasattr(self.talk_frequency, 'to_alipay_dict'):
                params['talk_frequency'] = self.talk_frequency.to_alipay_dict()
            else:
                params['talk_frequency'] = self.talk_frequency
        if self.talk_time:
            if hasattr(self.talk_time, 'to_alipay_dict'):
                params['talk_time'] = self.talk_time.to_alipay_dict()
            else:
                params['talk_time'] = self.talk_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HoloGraphicContactInfo()
        if 'call_frequency' in d:
            o.call_frequency = d['call_frequency']
        if 'call_time' in d:
            o.call_time = d['call_time']
        if 'called_frequency' in d:
            o.called_frequency = d['called_frequency']
        if 'called_time' in d:
            o.called_time = d['called_time']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'talk_frequency' in d:
            o.talk_frequency = d['talk_frequency']
        if 'talk_time' in d:
            o.talk_time = d['talk_time']
        return o


