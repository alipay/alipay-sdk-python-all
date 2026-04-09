#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LandingTypeDto import LandingTypeDto
from alipay.aop.api.domain.VideoInfo import VideoInfo


class AlipayDataDataserviceProductLandinginfoCreateormodifyModel(object):

    def __init__(self):
        self._item_id = None
        self._landing = None
        self._out_item_id = None
        self._video_info_list = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def landing(self):
        return self._landing

    @landing.setter
    def landing(self, value):
        if isinstance(value, list):
            self._landing = list()
            for i in value:
                if isinstance(i, LandingTypeDto):
                    self._landing.append(i)
                else:
                    self._landing.append(LandingTypeDto.from_alipay_dict(i))
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def video_info_list(self):
        return self._video_info_list

    @video_info_list.setter
    def video_info_list(self, value):
        if isinstance(value, list):
            self._video_info_list = list()
            for i in value:
                if isinstance(i, VideoInfo):
                    self._video_info_list.append(i)
                else:
                    self._video_info_list.append(VideoInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.landing:
            if isinstance(self.landing, list):
                for i in range(0, len(self.landing)):
                    element = self.landing[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.landing[i] = element.to_alipay_dict()
            if hasattr(self.landing, 'to_alipay_dict'):
                params['landing'] = self.landing.to_alipay_dict()
            else:
                params['landing'] = self.landing
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.video_info_list:
            if isinstance(self.video_info_list, list):
                for i in range(0, len(self.video_info_list)):
                    element = self.video_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_info_list[i] = element.to_alipay_dict()
            if hasattr(self.video_info_list, 'to_alipay_dict'):
                params['video_info_list'] = self.video_info_list.to_alipay_dict()
            else:
                params['video_info_list'] = self.video_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceProductLandinginfoCreateormodifyModel()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'landing' in d:
            o.landing = d['landing']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'video_info_list' in d:
            o.video_info_list = d['video_info_list']
        return o


