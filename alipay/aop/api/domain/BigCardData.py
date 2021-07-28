#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BigCardData(object):

    def __init__(self):
        self._action_text = None
        self._biz_code = None
        self._biz_data = None
        self._biz_title = None
        self._color = None
        self._image_url = None
        self._left_image_url = None
        self._left_target_url = None
        self._left_title = None
        self._right_image_url = None
        self._right_target_url = None
        self._right_title = None
        self._sub_title = None
        self._target_url = None
        self._tool_type = None

    @property
    def action_text(self):
        return self._action_text

    @action_text.setter
    def action_text(self, value):
        self._action_text = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def biz_title(self):
        return self._biz_title

    @biz_title.setter
    def biz_title(self, value):
        self._biz_title = value
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def left_image_url(self):
        return self._left_image_url

    @left_image_url.setter
    def left_image_url(self, value):
        self._left_image_url = value
    @property
    def left_target_url(self):
        return self._left_target_url

    @left_target_url.setter
    def left_target_url(self, value):
        self._left_target_url = value
    @property
    def left_title(self):
        return self._left_title

    @left_title.setter
    def left_title(self, value):
        self._left_title = value
    @property
    def right_image_url(self):
        return self._right_image_url

    @right_image_url.setter
    def right_image_url(self, value):
        self._right_image_url = value
    @property
    def right_target_url(self):
        return self._right_target_url

    @right_target_url.setter
    def right_target_url(self, value):
        self._right_target_url = value
    @property
    def right_title(self):
        return self._right_title

    @right_title.setter
    def right_title(self, value):
        self._right_title = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def tool_type(self):
        return self._tool_type

    @tool_type.setter
    def tool_type(self, value):
        self._tool_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_text:
            if hasattr(self.action_text, 'to_alipay_dict'):
                params['action_text'] = self.action_text.to_alipay_dict()
            else:
                params['action_text'] = self.action_text
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biz_title:
            if hasattr(self.biz_title, 'to_alipay_dict'):
                params['biz_title'] = self.biz_title.to_alipay_dict()
            else:
                params['biz_title'] = self.biz_title
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.left_image_url:
            if hasattr(self.left_image_url, 'to_alipay_dict'):
                params['left_image_url'] = self.left_image_url.to_alipay_dict()
            else:
                params['left_image_url'] = self.left_image_url
        if self.left_target_url:
            if hasattr(self.left_target_url, 'to_alipay_dict'):
                params['left_target_url'] = self.left_target_url.to_alipay_dict()
            else:
                params['left_target_url'] = self.left_target_url
        if self.left_title:
            if hasattr(self.left_title, 'to_alipay_dict'):
                params['left_title'] = self.left_title.to_alipay_dict()
            else:
                params['left_title'] = self.left_title
        if self.right_image_url:
            if hasattr(self.right_image_url, 'to_alipay_dict'):
                params['right_image_url'] = self.right_image_url.to_alipay_dict()
            else:
                params['right_image_url'] = self.right_image_url
        if self.right_target_url:
            if hasattr(self.right_target_url, 'to_alipay_dict'):
                params['right_target_url'] = self.right_target_url.to_alipay_dict()
            else:
                params['right_target_url'] = self.right_target_url
        if self.right_title:
            if hasattr(self.right_title, 'to_alipay_dict'):
                params['right_title'] = self.right_title.to_alipay_dict()
            else:
                params['right_title'] = self.right_title
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.tool_type:
            if hasattr(self.tool_type, 'to_alipay_dict'):
                params['tool_type'] = self.tool_type.to_alipay_dict()
            else:
                params['tool_type'] = self.tool_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BigCardData()
        if 'action_text' in d:
            o.action_text = d['action_text']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biz_title' in d:
            o.biz_title = d['biz_title']
        if 'color' in d:
            o.color = d['color']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'left_image_url' in d:
            o.left_image_url = d['left_image_url']
        if 'left_target_url' in d:
            o.left_target_url = d['left_target_url']
        if 'left_title' in d:
            o.left_title = d['left_title']
        if 'right_image_url' in d:
            o.right_image_url = d['right_image_url']
        if 'right_target_url' in d:
            o.right_target_url = d['right_target_url']
        if 'right_title' in d:
            o.right_title = d['right_title']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'tool_type' in d:
            o.tool_type = d['tool_type']
        return o


