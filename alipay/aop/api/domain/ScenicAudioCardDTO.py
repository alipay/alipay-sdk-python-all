#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicAudioCardDTO(object):

    def __init__(self):
        self._audio_url = None
        self._img_url = None
        self._row_type = None
        self._tags = None
        self._text = None
        self._title = None

    @property
    def audio_url(self):
        return self._audio_url

    @audio_url.setter
    def audio_url(self, value):
        self._audio_url = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_url:
            if hasattr(self.audio_url, 'to_alipay_dict'):
                params['audio_url'] = self.audio_url.to_alipay_dict()
            else:
                params['audio_url'] = self.audio_url
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
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
        o = ScenicAudioCardDTO()
        if 'audio_url' in d:
            o.audio_url = d['audio_url']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'tags' in d:
            o.tags = d['tags']
        if 'text' in d:
            o.text = d['text']
        if 'title' in d:
            o.title = d['title']
        return o


