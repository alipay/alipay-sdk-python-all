#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SoundNodeInfo import SoundNodeInfo


class AlbumSoundInfo(object):

    def __init__(self):
        self._duration = None
        self._sample_duration = None
        self._sound_brief = None
        self._sound_cover_url = None
        self._sound_digest_desc = None
        self._sound_free = None
        self._sound_id = None
        self._sound_name = None
        self._sound_node_list = None
        self._sound_operate_type = None
        self._sound_order = None
        self._sound_release_time = None
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
    def sound_brief(self):
        return self._sound_brief

    @sound_brief.setter
    def sound_brief(self, value):
        self._sound_brief = value
    @property
    def sound_cover_url(self):
        return self._sound_cover_url

    @sound_cover_url.setter
    def sound_cover_url(self, value):
        self._sound_cover_url = value
    @property
    def sound_digest_desc(self):
        return self._sound_digest_desc

    @sound_digest_desc.setter
    def sound_digest_desc(self, value):
        self._sound_digest_desc = value
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
    def sound_node_list(self):
        return self._sound_node_list

    @sound_node_list.setter
    def sound_node_list(self, value):
        if isinstance(value, list):
            self._sound_node_list = list()
            for i in value:
                if isinstance(i, SoundNodeInfo):
                    self._sound_node_list.append(i)
                else:
                    self._sound_node_list.append(SoundNodeInfo.from_alipay_dict(i))
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
    def sound_release_time(self):
        return self._sound_release_time

    @sound_release_time.setter
    def sound_release_time(self, value):
        self._sound_release_time = value
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
        if self.sound_brief:
            if hasattr(self.sound_brief, 'to_alipay_dict'):
                params['sound_brief'] = self.sound_brief.to_alipay_dict()
            else:
                params['sound_brief'] = self.sound_brief
        if self.sound_cover_url:
            if hasattr(self.sound_cover_url, 'to_alipay_dict'):
                params['sound_cover_url'] = self.sound_cover_url.to_alipay_dict()
            else:
                params['sound_cover_url'] = self.sound_cover_url
        if self.sound_digest_desc:
            if hasattr(self.sound_digest_desc, 'to_alipay_dict'):
                params['sound_digest_desc'] = self.sound_digest_desc.to_alipay_dict()
            else:
                params['sound_digest_desc'] = self.sound_digest_desc
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
        if self.sound_node_list:
            if isinstance(self.sound_node_list, list):
                for i in range(0, len(self.sound_node_list)):
                    element = self.sound_node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sound_node_list[i] = element.to_alipay_dict()
            if hasattr(self.sound_node_list, 'to_alipay_dict'):
                params['sound_node_list'] = self.sound_node_list.to_alipay_dict()
            else:
                params['sound_node_list'] = self.sound_node_list
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
        if self.sound_release_time:
            if hasattr(self.sound_release_time, 'to_alipay_dict'):
                params['sound_release_time'] = self.sound_release_time.to_alipay_dict()
            else:
                params['sound_release_time'] = self.sound_release_time
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
        if 'sound_brief' in d:
            o.sound_brief = d['sound_brief']
        if 'sound_cover_url' in d:
            o.sound_cover_url = d['sound_cover_url']
        if 'sound_digest_desc' in d:
            o.sound_digest_desc = d['sound_digest_desc']
        if 'sound_free' in d:
            o.sound_free = d['sound_free']
        if 'sound_id' in d:
            o.sound_id = d['sound_id']
        if 'sound_name' in d:
            o.sound_name = d['sound_name']
        if 'sound_node_list' in d:
            o.sound_node_list = d['sound_node_list']
        if 'sound_operate_type' in d:
            o.sound_operate_type = d['sound_operate_type']
        if 'sound_order' in d:
            o.sound_order = d['sound_order']
        if 'sound_release_time' in d:
            o.sound_release_time = d['sound_release_time']
        if 'sound_tags' in d:
            o.sound_tags = d['sound_tags']
        if 'support_sample' in d:
            o.support_sample = d['support_sample']
        return o


