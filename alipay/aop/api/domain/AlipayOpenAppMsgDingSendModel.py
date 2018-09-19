#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMsgDingSendModel(object):

    def __init__(self):
        self._agent_id = None
        self._content = None
        self._goto_url = None
        self._image_url = None
        self._msg_type = None
        self._receiver = None
        self._title = None
        self._user_ids = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = self.goto_url.to_alipay_dict()
            else:
                params['goto_url'] = self.goto_url
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMsgDingSendModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'content' in d:
            o.content = d['content']
        if 'goto_url' in d:
            o.goto_url = d['goto_url']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'title' in d:
            o.title = d['title']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


