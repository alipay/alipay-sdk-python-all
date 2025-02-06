#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoiRecord(object):

    def __init__(self):
        self._img_url = None
        self._tag = None
        self._title = None
        self._via_flag = None

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def via_flag(self):
        return self._via_flag

    @via_flag.setter
    def via_flag(self, value):
        self._via_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.via_flag:
            if hasattr(self.via_flag, 'to_alipay_dict'):
                params['via_flag'] = self.via_flag.to_alipay_dict()
            else:
                params['via_flag'] = self.via_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiRecord()
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'tag' in d:
            o.tag = d['tag']
        if 'title' in d:
            o.title = d['title']
        if 'via_flag' in d:
            o.via_flag = d['via_flag']
        return o


