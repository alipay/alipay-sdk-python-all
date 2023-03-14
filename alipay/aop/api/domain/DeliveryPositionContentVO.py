#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigueContent import DeliveryFatigueContent
from alipay.aop.api.domain.CreativityFatigue import CreativityFatigue


class DeliveryPositionContentVO(object):

    def __init__(self):
        self._content_fatigue = None
        self._creativity_fatigue = None
        self._image_url = None
        self._jump_url = None
        self._scm = None

    @property
    def content_fatigue(self):
        return self._content_fatigue

    @content_fatigue.setter
    def content_fatigue(self, value):
        if isinstance(value, DeliveryFatigueContent):
            self._content_fatigue = value
        else:
            self._content_fatigue = DeliveryFatigueContent.from_alipay_dict(value)
    @property
    def creativity_fatigue(self):
        return self._creativity_fatigue

    @creativity_fatigue.setter
    def creativity_fatigue(self, value):
        if isinstance(value, CreativityFatigue):
            self._creativity_fatigue = value
        else:
            self._creativity_fatigue = CreativityFatigue.from_alipay_dict(value)
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def scm(self):
        return self._scm

    @scm.setter
    def scm(self, value):
        self._scm = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_fatigue:
            if hasattr(self.content_fatigue, 'to_alipay_dict'):
                params['content_fatigue'] = self.content_fatigue.to_alipay_dict()
            else:
                params['content_fatigue'] = self.content_fatigue
        if self.creativity_fatigue:
            if hasattr(self.creativity_fatigue, 'to_alipay_dict'):
                params['creativity_fatigue'] = self.creativity_fatigue.to_alipay_dict()
            else:
                params['creativity_fatigue'] = self.creativity_fatigue
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.scm:
            if hasattr(self.scm, 'to_alipay_dict'):
                params['scm'] = self.scm.to_alipay_dict()
            else:
                params['scm'] = self.scm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryPositionContentVO()
        if 'content_fatigue' in d:
            o.content_fatigue = d['content_fatigue']
        if 'creativity_fatigue' in d:
            o.creativity_fatigue = d['creativity_fatigue']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'scm' in d:
            o.scm = d['scm']
        return o


