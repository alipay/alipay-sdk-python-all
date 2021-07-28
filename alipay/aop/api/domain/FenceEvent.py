#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AudioEvent import AudioEvent


class FenceEvent(object):

    def __init__(self):
        self._audio_events = None
        self._fence_code = None
        self._latitude = None
        self._longitude = None
        self._multi_audio_interval = None
        self._radius = None

    @property
    def audio_events(self):
        return self._audio_events

    @audio_events.setter
    def audio_events(self, value):
        if isinstance(value, list):
            self._audio_events = list()
            for i in value:
                if isinstance(i, AudioEvent):
                    self._audio_events.append(i)
                else:
                    self._audio_events.append(AudioEvent.from_alipay_dict(i))
    @property
    def fence_code(self):
        return self._fence_code

    @fence_code.setter
    def fence_code(self, value):
        self._fence_code = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def multi_audio_interval(self):
        return self._multi_audio_interval

    @multi_audio_interval.setter
    def multi_audio_interval(self, value):
        self._multi_audio_interval = value
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_events:
            if isinstance(self.audio_events, list):
                for i in range(0, len(self.audio_events)):
                    element = self.audio_events[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audio_events[i] = element.to_alipay_dict()
            if hasattr(self.audio_events, 'to_alipay_dict'):
                params['audio_events'] = self.audio_events.to_alipay_dict()
            else:
                params['audio_events'] = self.audio_events
        if self.fence_code:
            if hasattr(self.fence_code, 'to_alipay_dict'):
                params['fence_code'] = self.fence_code.to_alipay_dict()
            else:
                params['fence_code'] = self.fence_code
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.multi_audio_interval:
            if hasattr(self.multi_audio_interval, 'to_alipay_dict'):
                params['multi_audio_interval'] = self.multi_audio_interval.to_alipay_dict()
            else:
                params['multi_audio_interval'] = self.multi_audio_interval
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FenceEvent()
        if 'audio_events' in d:
            o.audio_events = d['audio_events']
        if 'fence_code' in d:
            o.fence_code = d['fence_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'multi_audio_interval' in d:
            o.multi_audio_interval = d['multi_audio_interval']
        if 'radius' in d:
            o.radius = d['radius']
        return o


