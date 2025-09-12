#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TextLinkVO import TextLinkVO


class ImageTextMsgVO(object):

    def __init__(self):
        self._desc = None
        self._image = None
        self._image_id = None
        self._image_url = None
        self._text_link_list = None
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
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def text_link_list(self):
        return self._text_link_list

    @text_link_list.setter
    def text_link_list(self, value):
        if isinstance(value, list):
            self._text_link_list = list()
            for i in value:
                if isinstance(i, TextLinkVO):
                    self._text_link_list.append(i)
                else:
                    self._text_link_list.append(TextLinkVO.from_alipay_dict(i))
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
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.text_link_list:
            if isinstance(self.text_link_list, list):
                for i in range(0, len(self.text_link_list)):
                    element = self.text_link_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text_link_list[i] = element.to_alipay_dict()
            if hasattr(self.text_link_list, 'to_alipay_dict'):
                params['text_link_list'] = self.text_link_list.to_alipay_dict()
            else:
                params['text_link_list'] = self.text_link_list
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
        o = ImageTextMsgVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'image' in d:
            o.image = d['image']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'text_link_list' in d:
            o.text_link_list = d['text_link_list']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


