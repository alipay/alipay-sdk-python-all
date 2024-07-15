#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantActivityVO(object):

    def __init__(self):
        self._action_name = None
        self._action_url = None
        self._crowd_code = None
        self._desc = None
        self._image_id = None
        self._title = None

    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
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
        o = AssistantActivityVO()
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'title' in d:
            o.title = d['title']
        return o


