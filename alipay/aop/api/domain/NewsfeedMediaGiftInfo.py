#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedMediaGiftInfo(object):

    def __init__(self):
        self._action = None
        self._adr_height = None
        self._adr_thumb = None
        self._adr_width = None
        self._ios_height = None
        self._ios_thumb = None
        self._ios_width = None
        self._theme = None
        self._type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def adr_height(self):
        return self._adr_height

    @adr_height.setter
    def adr_height(self, value):
        self._adr_height = value
    @property
    def adr_thumb(self):
        return self._adr_thumb

    @adr_thumb.setter
    def adr_thumb(self, value):
        self._adr_thumb = value
    @property
    def adr_width(self):
        return self._adr_width

    @adr_width.setter
    def adr_width(self, value):
        self._adr_width = value
    @property
    def ios_height(self):
        return self._ios_height

    @ios_height.setter
    def ios_height(self, value):
        self._ios_height = value
    @property
    def ios_thumb(self):
        return self._ios_thumb

    @ios_thumb.setter
    def ios_thumb(self, value):
        self._ios_thumb = value
    @property
    def ios_width(self):
        return self._ios_width

    @ios_width.setter
    def ios_width(self, value):
        self._ios_width = value
    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.adr_height:
            if hasattr(self.adr_height, 'to_alipay_dict'):
                params['adr_height'] = self.adr_height.to_alipay_dict()
            else:
                params['adr_height'] = self.adr_height
        if self.adr_thumb:
            if hasattr(self.adr_thumb, 'to_alipay_dict'):
                params['adr_thumb'] = self.adr_thumb.to_alipay_dict()
            else:
                params['adr_thumb'] = self.adr_thumb
        if self.adr_width:
            if hasattr(self.adr_width, 'to_alipay_dict'):
                params['adr_width'] = self.adr_width.to_alipay_dict()
            else:
                params['adr_width'] = self.adr_width
        if self.ios_height:
            if hasattr(self.ios_height, 'to_alipay_dict'):
                params['ios_height'] = self.ios_height.to_alipay_dict()
            else:
                params['ios_height'] = self.ios_height
        if self.ios_thumb:
            if hasattr(self.ios_thumb, 'to_alipay_dict'):
                params['ios_thumb'] = self.ios_thumb.to_alipay_dict()
            else:
                params['ios_thumb'] = self.ios_thumb
        if self.ios_width:
            if hasattr(self.ios_width, 'to_alipay_dict'):
                params['ios_width'] = self.ios_width.to_alipay_dict()
            else:
                params['ios_width'] = self.ios_width
        if self.theme:
            if hasattr(self.theme, 'to_alipay_dict'):
                params['theme'] = self.theme.to_alipay_dict()
            else:
                params['theme'] = self.theme
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsfeedMediaGiftInfo()
        if 'action' in d:
            o.action = d['action']
        if 'adr_height' in d:
            o.adr_height = d['adr_height']
        if 'adr_thumb' in d:
            o.adr_thumb = d['adr_thumb']
        if 'adr_width' in d:
            o.adr_width = d['adr_width']
        if 'ios_height' in d:
            o.ios_height = d['ios_height']
        if 'ios_thumb' in d:
            o.ios_thumb = d['ios_thumb']
        if 'ios_width' in d:
            o.ios_width = d['ios_width']
        if 'theme' in d:
            o.theme = d['theme']
        if 'type' in d:
            o.type = d['type']
        return o


