#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelRoomVO(object):

    def __init__(self):
        self._build = None
        self._feature_tag_list = None
        self._floor = None
        self._room_area = None
        self._room_no = None

    @property
    def build(self):
        return self._build

    @build.setter
    def build(self, value):
        self._build = value
    @property
    def feature_tag_list(self):
        return self._feature_tag_list

    @feature_tag_list.setter
    def feature_tag_list(self, value):
        if isinstance(value, list):
            self._feature_tag_list = list()
            for i in value:
                self._feature_tag_list.append(i)
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def room_area(self):
        return self._room_area

    @room_area.setter
    def room_area(self, value):
        self._room_area = value
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, value):
        self._room_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.build:
            if hasattr(self.build, 'to_alipay_dict'):
                params['build'] = self.build.to_alipay_dict()
            else:
                params['build'] = self.build
        if self.feature_tag_list:
            if isinstance(self.feature_tag_list, list):
                for i in range(0, len(self.feature_tag_list)):
                    element = self.feature_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feature_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.feature_tag_list, 'to_alipay_dict'):
                params['feature_tag_list'] = self.feature_tag_list.to_alipay_dict()
            else:
                params['feature_tag_list'] = self.feature_tag_list
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.room_area:
            if hasattr(self.room_area, 'to_alipay_dict'):
                params['room_area'] = self.room_area.to_alipay_dict()
            else:
                params['room_area'] = self.room_area
        if self.room_no:
            if hasattr(self.room_no, 'to_alipay_dict'):
                params['room_no'] = self.room_no.to_alipay_dict()
            else:
                params['room_no'] = self.room_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelRoomVO()
        if 'build' in d:
            o.build = d['build']
        if 'feature_tag_list' in d:
            o.feature_tag_list = d['feature_tag_list']
        if 'floor' in d:
            o.floor = d['floor']
        if 'room_area' in d:
            o.room_area = d['room_area']
        if 'room_no' in d:
            o.room_no = d['room_no']
        return o


