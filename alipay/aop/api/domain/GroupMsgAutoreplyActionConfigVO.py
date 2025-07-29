#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupMsgAutoreplyActionConfigVO(object):

    def __init__(self):
        self._image_id = None
        self._link = None
        self._link_desc = None
        self._link_image_id = None
        self._link_title = None
        self._msg_type = None
        self._text = None

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def link_desc(self):
        return self._link_desc

    @link_desc.setter
    def link_desc(self, value):
        self._link_desc = value
    @property
    def link_image_id(self):
        return self._link_image_id

    @link_image_id.setter
    def link_image_id(self, value):
        self._link_image_id = value
    @property
    def link_title(self):
        return self._link_title

    @link_title.setter
    def link_title(self, value):
        self._link_title = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.link_desc:
            if hasattr(self.link_desc, 'to_alipay_dict'):
                params['link_desc'] = self.link_desc.to_alipay_dict()
            else:
                params['link_desc'] = self.link_desc
        if self.link_image_id:
            if hasattr(self.link_image_id, 'to_alipay_dict'):
                params['link_image_id'] = self.link_image_id.to_alipay_dict()
            else:
                params['link_image_id'] = self.link_image_id
        if self.link_title:
            if hasattr(self.link_title, 'to_alipay_dict'):
                params['link_title'] = self.link_title.to_alipay_dict()
            else:
                params['link_title'] = self.link_title
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgAutoreplyActionConfigVO()
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'link' in d:
            o.link = d['link']
        if 'link_desc' in d:
            o.link_desc = d['link_desc']
        if 'link_image_id' in d:
            o.link_image_id = d['link_image_id']
        if 'link_title' in d:
            o.link_title = d['link_title']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'text' in d:
            o.text = d['text']
        return o


