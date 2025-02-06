#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicAllBaseDTO(object):

    def __init__(self):
        self._avatar = None
        self._avatar_video = None
        self._city = None
        self._color_thief = None
        self._confort_level = None
        self._description = None
        self._introduction = None
        self._open_time = None
        self._scenery_name = None
        self._scenic_id = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def avatar_video(self):
        return self._avatar_video

    @avatar_video.setter
    def avatar_video(self, value):
        self._avatar_video = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def color_thief(self):
        return self._color_thief

    @color_thief.setter
    def color_thief(self, value):
        self._color_thief = value
    @property
    def confort_level(self):
        return self._confort_level

    @confort_level.setter
    def confort_level(self, value):
        self._confort_level = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def scenery_name(self):
        return self._scenery_name

    @scenery_name.setter
    def scenery_name(self, value):
        self._scenery_name = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.avatar_video:
            if hasattr(self.avatar_video, 'to_alipay_dict'):
                params['avatar_video'] = self.avatar_video.to_alipay_dict()
            else:
                params['avatar_video'] = self.avatar_video
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.color_thief:
            if hasattr(self.color_thief, 'to_alipay_dict'):
                params['color_thief'] = self.color_thief.to_alipay_dict()
            else:
                params['color_thief'] = self.color_thief
        if self.confort_level:
            if hasattr(self.confort_level, 'to_alipay_dict'):
                params['confort_level'] = self.confort_level.to_alipay_dict()
            else:
                params['confort_level'] = self.confort_level
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.scenery_name:
            if hasattr(self.scenery_name, 'to_alipay_dict'):
                params['scenery_name'] = self.scenery_name.to_alipay_dict()
            else:
                params['scenery_name'] = self.scenery_name
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicAllBaseDTO()
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'avatar_video' in d:
            o.avatar_video = d['avatar_video']
        if 'city' in d:
            o.city = d['city']
        if 'color_thief' in d:
            o.color_thief = d['color_thief']
        if 'confort_level' in d:
            o.confort_level = d['confort_level']
        if 'description' in d:
            o.description = d['description']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'scenery_name' in d:
            o.scenery_name = d['scenery_name']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        return o


