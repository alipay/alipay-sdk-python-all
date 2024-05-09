#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TinyAppMsgVO(object):

    def __init__(self):
        self._desc = None
        self._image = None
        self._tiny_app_id = None
        self._tiny_app_logo = None
        self._tiny_app_name = None
        self._title = None
        self._url = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value
    @property
    def tiny_app_logo(self):
        return self._tiny_app_logo

    @tiny_app_logo.setter
    def tiny_app_logo(self, value):
        self._tiny_app_logo = value
    @property
    def tiny_app_name(self):
        return self._tiny_app_name

    @tiny_app_name.setter
    def tiny_app_name(self, value):
        self._tiny_app_name = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        if self.tiny_app_logo:
            if hasattr(self.tiny_app_logo, 'to_alipay_dict'):
                params['tiny_app_logo'] = self.tiny_app_logo.to_alipay_dict()
            else:
                params['tiny_app_logo'] = self.tiny_app_logo
        if self.tiny_app_name:
            if hasattr(self.tiny_app_name, 'to_alipay_dict'):
                params['tiny_app_name'] = self.tiny_app_name.to_alipay_dict()
            else:
                params['tiny_app_name'] = self.tiny_app_name
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TinyAppMsgVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'image' in d:
            o.image = d['image']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        if 'tiny_app_logo' in d:
            o.tiny_app_logo = d['tiny_app_logo']
        if 'tiny_app_name' in d:
            o.tiny_app_name = d['tiny_app_name']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


