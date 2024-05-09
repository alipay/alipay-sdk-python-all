#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ImageTextMsgVO import ImageTextMsgVO
from alipay.aop.api.domain.TinyAppMsgVO import TinyAppMsgVO


class GroupMsgVO(object):

    def __init__(self):
        self._image_text_msg_content = None
        self._msg_type = None
        self._tiny_app_msg_content = None

    @property
    def image_text_msg_content(self):
        return self._image_text_msg_content

    @image_text_msg_content.setter
    def image_text_msg_content(self, value):
        if isinstance(value, ImageTextMsgVO):
            self._image_text_msg_content = value
        else:
            self._image_text_msg_content = ImageTextMsgVO.from_alipay_dict(value)
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def tiny_app_msg_content(self):
        return self._tiny_app_msg_content

    @tiny_app_msg_content.setter
    def tiny_app_msg_content(self, value):
        if isinstance(value, TinyAppMsgVO):
            self._tiny_app_msg_content = value
        else:
            self._tiny_app_msg_content = TinyAppMsgVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.image_text_msg_content:
            if hasattr(self.image_text_msg_content, 'to_alipay_dict'):
                params['image_text_msg_content'] = self.image_text_msg_content.to_alipay_dict()
            else:
                params['image_text_msg_content'] = self.image_text_msg_content
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.tiny_app_msg_content:
            if hasattr(self.tiny_app_msg_content, 'to_alipay_dict'):
                params['tiny_app_msg_content'] = self.tiny_app_msg_content.to_alipay_dict()
            else:
                params['tiny_app_msg_content'] = self.tiny_app_msg_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgVO()
        if 'image_text_msg_content' in d:
            o.image_text_msg_content = d['image_text_msg_content']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'tiny_app_msg_content' in d:
            o.tiny_app_msg_content = d['tiny_app_msg_content']
        return o


