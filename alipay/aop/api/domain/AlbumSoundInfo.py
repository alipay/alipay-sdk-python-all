#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlbumSoundInfo(object):

    def __init__(self):
        self._duration = None
        self._sample_duration = None
        self._sound_free = None
        self._sound_id = None
        self._sound_name = None
        self._sound_operate_type = None
        self._sound_order = None
        self._sound_tags = None
        self._support_sample = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def sample_duration(self):
        return self._sample_duration

    @sample_duration.setter
    def sample_duration(self, value):
        self._sample_duration = value
    @property
    def sound_free(self):
        return self._sound_free

    @sound_free.setter
    def sound_free(self, value):
        self._sound_free = value
    @property
    def sound_id(self):
        return self._sound_id

    @sound_id.setter
    def sound_id(self, value):
        self._sound_id = value
    @property
    def sound_name(self):
        return self._sound_name

    @sound_name.setter
    def sound_name(self, value):
        self._sound_name = value
    @property
    def sound_operate_type(self):
        return self._sound_operate_type

    @sound_operate_type.setter
    def sound_operate_type(self, value):
        self._sound_operate_type = value
    @property
    def sound_order(self):
        return self._sound_order

    @sound_order.setter
    def sound_order(self, value):
        self._sound_order = value
    @property
    def sound_tags(self):
        return self._sound_tags

    @sound_tags.setter
    def sound_tags(self, value):
        if isinstance(value, list):
            self._sound_tags = list()
            for i in value:
                self._sound_tags.append(i)
    @property
    def support_sample(self):
        return self._support_sample

    @support_sample.setter
    def support_sample(self, value):
        self._support_sample = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.sample_duration:
            if hasattr(self.sample_duration, 'to_alipay_dict'):
                params['sample_duration'] = self.sample_duration.to_alipay_dict()
            else:
                params['sample_duration'] = self.sample_duration
        if self.sound_free:
            if hasattr(self.sound_free, 'to_alipay_dict'):
                params['sound_free'] = self.sound_free.to_alipay_dict()
            else:
                params['sound_free'] = self.sound_free
        if self.sound_id:
            if hasattr(self.sound_id, 'to_alipay_dict'):
                params['sound_id'] = self.sound_id.to_alipay_dict()
            else:
                params['sound_id'] = self.sound_id
        if self.sound_name:
            if hasattr(self.sound_name, 'to_alipay_dict'):
                params['sound_name'] = self.sound_name.to_alipay_dict()
            else:
                params['sound_name'] = self.sound_name
        if self.sound_operate_type:
            if hasattr(self.sound_operate_type, 'to_alipay_dict'):
                params['sound_operate_type'] = self.sound_operate_type.to_alipay_dict()
            else:
                params['sound_operate_type'] = self.sound_operate_type
        if self.sound_order:
            if hasattr(self.sound_order, 'to_alipay_dict'):
                params['sound_order'] = self.sound_order.to_alipay_dict()
            else:
                params['sound_order'] = self.sound_order
        if self.sound_tags:
            if isinstance(self.sound_tags, list):
                for i in range(0, len(self.sound_tags)):
                    element = self.sound_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sound_tags[i] = element.to_alipay_dict()
            if hasattr(self.sound_tags, 'to_alipay_dict'):
                params['sound_tags'] = self.sound_tags.to_alipay_dict()
            else:
                params['sound_tags'] = self.sound_tags
        if self.support_sample:
            if hasattr(self.support_sample, 'to_alipay_dict'):
                params['support_sample'] = self.support_sample.to_alipay_dict()
            else:
                params['support_sample'] = self.support_sample
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlbumSoundInfo()
        if 'duration' in d:
            o.duration = d['duration']
        if 'sample_duration' in d:
            o.sample_duration = d['sample_duration']
        if 'sound_free' in d:
            o.sound_free = d['sound_free']
        if 'sound_id' in d:
            o.sound_id = d['sound_id']
        if 'sound_name' in d:
            o.sound_name = d['sound_name']
        if 'sound_operate_type' in d:
            o.sound_operate_type = d['sound_operate_type']
        if 'sound_order' in d:
            o.sound_order = d['sound_order']
        if 'sound_tags' in d:
            o.sound_tags = d['sound_tags']
        if 'support_sample' in d:
            o.support_sample = d['support_sample']
        return o


