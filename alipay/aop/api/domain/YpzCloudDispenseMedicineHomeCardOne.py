#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YpzCloudDispenseMedicineCardNode import YpzCloudDispenseMedicineCardNode


class YpzCloudDispenseMedicineHomeCardOne(object):

    def __init__(self):
        self._button_text = None
        self._card_type = None
        self._description = None
        self._main_title = None
        self._node_list = None
        self._redirect_url = None
        self._title = None
        self._unique_id = None

    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
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
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
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
        if self.main_title:
            if hasattr(self.main_title, 'to_alipay_dict'):
                params['main_title'] = self.main_title.to_alipay_dict()
            else:
                params['main_title'] = self.main_title
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
        o = YpzCloudDispenseMedicineHomeCardOne()
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'description' in d:
            o.description = d['description']
        if 'main_title' in d:
            o.main_title = d['main_title']
        if 'node_list' in d:
            o.node_list = d['node_list']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'title' in d:
            o.title = d['title']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


