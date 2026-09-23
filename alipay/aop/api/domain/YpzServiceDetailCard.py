#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YpzServiceDetailCardExt import YpzServiceDetailCardExt
from alipay.aop.api.domain.YpzCloudDispenseMedicineCardNode import YpzCloudDispenseMedicineCardNode


class YpzServiceDetailCard(object):

    def __init__(self):
        self._button_text = None
        self._button_text_left = None
        self._button_text_right = None
        self._card_type = None
        self._description = None
        self._ext = None
        self._image_url = None
        self._node_list = None
        self._redirect_url = None
        self._redirect_url_left = None
        self._redirect_url_right = None
        self._status = None
        self._status_text = None
        self._title = None
        self._unique_id = None

    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def button_text_left(self):
        return self._button_text_left

    @button_text_left.setter
    def button_text_left(self, value):
        self._button_text_left = value
    @property
    def button_text_right(self):
        return self._button_text_right

    @button_text_right.setter
    def button_text_right(self, value):
        self._button_text_right = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        if isinstance(value, YpzServiceDetailCardExt):
            self._ext = value
        else:
            self._ext = YpzServiceDetailCardExt.from_alipay_dict(value)
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, YpzCloudDispenseMedicineCardNode):
                    self._node_list.append(i)
                else:
                    self._node_list.append(YpzCloudDispenseMedicineCardNode.from_alipay_dict(i))
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def redirect_url_left(self):
        return self._redirect_url_left

    @redirect_url_left.setter
    def redirect_url_left(self, value):
        self._redirect_url_left = value
    @property
    def redirect_url_right(self):
        return self._redirect_url_right

    @redirect_url_right.setter
    def redirect_url_right(self, value):
        self._redirect_url_right = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_text(self):
        return self._status_text

    @status_text.setter
    def status_text(self, value):
        self._status_text = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.button_text_left:
            if hasattr(self.button_text_left, 'to_alipay_dict'):
                params['button_text_left'] = self.button_text_left.to_alipay_dict()
            else:
                params['button_text_left'] = self.button_text_left
        if self.button_text_right:
            if hasattr(self.button_text_right, 'to_alipay_dict'):
                params['button_text_right'] = self.button_text_right.to_alipay_dict()
            else:
                params['button_text_right'] = self.button_text_right
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.node_list:
            if isinstance(self.node_list, list):
                for i in range(0, len(self.node_list)):
                    element = self.node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_list[i] = element.to_alipay_dict()
            if hasattr(self.node_list, 'to_alipay_dict'):
                params['node_list'] = self.node_list.to_alipay_dict()
            else:
                params['node_list'] = self.node_list
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.redirect_url_left:
            if hasattr(self.redirect_url_left, 'to_alipay_dict'):
                params['redirect_url_left'] = self.redirect_url_left.to_alipay_dict()
            else:
                params['redirect_url_left'] = self.redirect_url_left
        if self.redirect_url_right:
            if hasattr(self.redirect_url_right, 'to_alipay_dict'):
                params['redirect_url_right'] = self.redirect_url_right.to_alipay_dict()
            else:
                params['redirect_url_right'] = self.redirect_url_right
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_text:
            if hasattr(self.status_text, 'to_alipay_dict'):
                params['status_text'] = self.status_text.to_alipay_dict()
            else:
                params['status_text'] = self.status_text
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzServiceDetailCard()
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'button_text_left' in d:
            o.button_text_left = d['button_text_left']
        if 'button_text_right' in d:
            o.button_text_right = d['button_text_right']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'description' in d:
            o.description = d['description']
        if 'ext' in d:
            o.ext = d['ext']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'node_list' in d:
            o.node_list = d['node_list']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'redirect_url_left' in d:
            o.redirect_url_left = d['redirect_url_left']
        if 'redirect_url_right' in d:
            o.redirect_url_right = d['redirect_url_right']
        if 'status' in d:
            o.status = d['status']
        if 'status_text' in d:
            o.status_text = d['status_text']
        if 'title' in d:
            o.title = d['title']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


