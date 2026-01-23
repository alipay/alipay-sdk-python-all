#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PatternWord(object):

    def __init__(self):
        self._app_url = None
        self._icon_url = None
        self._mp_url = None
        self._pc_url = None
        self._touch_url = None
        self._word = None

    @property
    def app_url(self):
        return self._app_url

    @app_url.setter
    def app_url(self, value):
        self._app_url = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def mp_url(self):
        return self._mp_url

    @mp_url.setter
    def mp_url(self, value):
        self._mp_url = value
    @property
    def pc_url(self):
        return self._pc_url

    @pc_url.setter
    def pc_url(self, value):
        self._pc_url = value
    @property
    def touch_url(self):
        return self._touch_url

    @touch_url.setter
    def touch_url(self, value):
        self._touch_url = value
    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, value):
        self._word = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_url:
            if hasattr(self.app_url, 'to_alipay_dict'):
                params['app_url'] = self.app_url.to_alipay_dict()
            else:
                params['app_url'] = self.app_url
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.mp_url:
            if hasattr(self.mp_url, 'to_alipay_dict'):
                params['mp_url'] = self.mp_url.to_alipay_dict()
            else:
                params['mp_url'] = self.mp_url
        if self.pc_url:
            if hasattr(self.pc_url, 'to_alipay_dict'):
                params['pc_url'] = self.pc_url.to_alipay_dict()
            else:
                params['pc_url'] = self.pc_url
        if self.touch_url:
            if hasattr(self.touch_url, 'to_alipay_dict'):
                params['touch_url'] = self.touch_url.to_alipay_dict()
            else:
                params['touch_url'] = self.touch_url
        if self.word:
            if hasattr(self.word, 'to_alipay_dict'):
                params['word'] = self.word.to_alipay_dict()
            else:
                params['word'] = self.word
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PatternWord()
        if 'app_url' in d:
            o.app_url = d['app_url']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'mp_url' in d:
            o.mp_url = d['mp_url']
        if 'pc_url' in d:
            o.pc_url = d['pc_url']
        if 'touch_url' in d:
            o.touch_url = d['touch_url']
        if 'word' in d:
            o.word = d['word']
        return o


