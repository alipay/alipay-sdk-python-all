#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShortPlayEpisodeInfo import ShortPlayEpisodeInfo
from alipay.aop.api.domain.ShortPlayRecordMaterial import ShortPlayRecordMaterial


class AlipaySocialBaseLifecreationShortplayCreateModel(object):

    def __init__(self):
        self._broadcast_record_number = None
        self._cover = None
        self._episode_info_list = None
        self._record_material = None
        self._tag_list = None
        self._title = None

    @property
    def broadcast_record_number(self):
        return self._broadcast_record_number

    @broadcast_record_number.setter
    def broadcast_record_number(self, value):
        self._broadcast_record_number = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def episode_info_list(self):
        return self._episode_info_list

    @episode_info_list.setter
    def episode_info_list(self, value):
        if isinstance(value, list):
            self._episode_info_list = list()
            for i in value:
                if isinstance(i, ShortPlayEpisodeInfo):
                    self._episode_info_list.append(i)
                else:
                    self._episode_info_list.append(ShortPlayEpisodeInfo.from_alipay_dict(i))
    @property
    def record_material(self):
        return self._record_material

    @record_material.setter
    def record_material(self, value):
        if isinstance(value, ShortPlayRecordMaterial):
            self._record_material = value
        else:
            self._record_material = ShortPlayRecordMaterial.from_alipay_dict(value)
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.broadcast_record_number:
            if hasattr(self.broadcast_record_number, 'to_alipay_dict'):
                params['broadcast_record_number'] = self.broadcast_record_number.to_alipay_dict()
            else:
                params['broadcast_record_number'] = self.broadcast_record_number
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.episode_info_list:
            if isinstance(self.episode_info_list, list):
                for i in range(0, len(self.episode_info_list)):
                    element = self.episode_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.episode_info_list[i] = element.to_alipay_dict()
            if hasattr(self.episode_info_list, 'to_alipay_dict'):
                params['episode_info_list'] = self.episode_info_list.to_alipay_dict()
            else:
                params['episode_info_list'] = self.episode_info_list
        if self.record_material:
            if hasattr(self.record_material, 'to_alipay_dict'):
                params['record_material'] = self.record_material.to_alipay_dict()
            else:
                params['record_material'] = self.record_material
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseLifecreationShortplayCreateModel()
        if 'broadcast_record_number' in d:
            o.broadcast_record_number = d['broadcast_record_number']
        if 'cover' in d:
            o.cover = d['cover']
        if 'episode_info_list' in d:
            o.episode_info_list = d['episode_info_list']
        if 'record_material' in d:
            o.record_material = d['record_material']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'title' in d:
            o.title = d['title']
        return o


