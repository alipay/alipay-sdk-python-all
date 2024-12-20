#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalServiceMagaCardDTO(object):

    def __init__(self):
        self._desc = None
        self._icon_url = None
        self._jump_url = None
        self._name = None
        self._third_service_flag = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def third_service_flag(self):
        return self._third_service_flag

    @third_service_flag.setter
    def third_service_flag(self, value):
        self._third_service_flag = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.third_service_flag:
            if hasattr(self.third_service_flag, 'to_alipay_dict'):
                params['third_service_flag'] = self.third_service_flag.to_alipay_dict()
            else:
                params['third_service_flag'] = self.third_service_flag
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
        o = MedicalServiceMagaCardDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'name' in d:
            o.name = d['name']
        if 'third_service_flag' in d:
            o.third_service_flag = d['third_service_flag']
        if 'title' in d:
            o.title = d['title']
        return o


