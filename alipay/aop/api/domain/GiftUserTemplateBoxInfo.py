#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GiftTemplateAtmosphereBox import GiftTemplateAtmosphereBox
from alipay.aop.api.domain.GiftTemplateBackCoverBox import GiftTemplateBackCoverBox
from alipay.aop.api.domain.GiftTemplateBaseInfo import GiftTemplateBaseInfo
from alipay.aop.api.domain.GiftTemplateButtonBox import GiftTemplateButtonBox
from alipay.aop.api.domain.GiftTemplateFrontCoverBox import GiftTemplateFrontCoverBox
from alipay.aop.api.domain.GiftTemplateStoryBox import GiftTemplateStoryBox


class GiftUserTemplateBoxInfo(object):

    def __init__(self):
        self._atmosphere_box = None
        self._back_cover_box = None
        self._base_info = None
        self._button_box = None
        self._front_cover_box = None
        self._story_box = None
        self._valid = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def atmosphere_box(self):
        return self._atmosphere_box

    @atmosphere_box.setter
    def atmosphere_box(self, value):
        if isinstance(value, GiftTemplateAtmosphereBox):
            self._atmosphere_box = value
        else:
            self._atmosphere_box = GiftTemplateAtmosphereBox.from_alipay_dict(value)
    @property
    def back_cover_box(self):
        return self._back_cover_box

    @back_cover_box.setter
    def back_cover_box(self, value):
        if isinstance(value, GiftTemplateBackCoverBox):
            self._back_cover_box = value
        else:
            self._back_cover_box = GiftTemplateBackCoverBox.from_alipay_dict(value)
    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, GiftTemplateBaseInfo):
            self._base_info = value
        else:
            self._base_info = GiftTemplateBaseInfo.from_alipay_dict(value)
    @property
    def button_box(self):
        return self._button_box

    @button_box.setter
    def button_box(self, value):
        if isinstance(value, GiftTemplateButtonBox):
            self._button_box = value
        else:
            self._button_box = GiftTemplateButtonBox.from_alipay_dict(value)
    @property
    def front_cover_box(self):
        return self._front_cover_box

    @front_cover_box.setter
    def front_cover_box(self, value):
        if isinstance(value, GiftTemplateFrontCoverBox):
            self._front_cover_box = value
        else:
            self._front_cover_box = GiftTemplateFrontCoverBox.from_alipay_dict(value)
    @property
    def story_box(self):
        return self._story_box

    @story_box.setter
    def story_box(self, value):
        if isinstance(value, GiftTemplateStoryBox):
            self._story_box = value
        else:
            self._story_box = GiftTemplateStoryBox.from_alipay_dict(value)
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.atmosphere_box:
            if hasattr(self.atmosphere_box, 'to_alipay_dict'):
                params['atmosphere_box'] = self.atmosphere_box.to_alipay_dict()
            else:
                params['atmosphere_box'] = self.atmosphere_box
        if self.back_cover_box:
            if hasattr(self.back_cover_box, 'to_alipay_dict'):
                params['back_cover_box'] = self.back_cover_box.to_alipay_dict()
            else:
                params['back_cover_box'] = self.back_cover_box
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.button_box:
            if hasattr(self.button_box, 'to_alipay_dict'):
                params['button_box'] = self.button_box.to_alipay_dict()
            else:
                params['button_box'] = self.button_box
        if self.front_cover_box:
            if hasattr(self.front_cover_box, 'to_alipay_dict'):
                params['front_cover_box'] = self.front_cover_box.to_alipay_dict()
            else:
                params['front_cover_box'] = self.front_cover_box
        if self.story_box:
            if hasattr(self.story_box, 'to_alipay_dict'):
                params['story_box'] = self.story_box.to_alipay_dict()
            else:
                params['story_box'] = self.story_box
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftUserTemplateBoxInfo()
        if 'atmosphere_box' in d:
            o.atmosphere_box = d['atmosphere_box']
        if 'back_cover_box' in d:
            o.back_cover_box = d['back_cover_box']
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'button_box' in d:
            o.button_box = d['button_box']
        if 'front_cover_box' in d:
            o.front_cover_box = d['front_cover_box']
        if 'story_box' in d:
            o.story_box = d['story_box']
        if 'valid' in d:
            o.valid = d['valid']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


