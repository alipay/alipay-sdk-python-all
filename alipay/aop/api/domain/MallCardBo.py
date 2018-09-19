#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallCardBo(object):

    def __init__(self):
        self._benefit_desc = None
        self._card_logo_url = None
        self._ext_info = None
        self._level_show_name = None
        self._template_id = None
        self._title = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        if isinstance(value, list):
            self._benefit_desc = list()
            for i in value:
                self._benefit_desc.append(i)
    @property
    def card_logo_url(self):
        return self._card_logo_url

    @card_logo_url.setter
    def card_logo_url(self, value):
        self._card_logo_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def level_show_name(self):
        return self._level_show_name

    @level_show_name.setter
    def level_show_name(self, value):
        self._level_show_name = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if isinstance(self.benefit_desc, list):
                for i in range(0, len(self.benefit_desc)):
                    element = self.benefit_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_desc[i] = element.to_alipay_dict()
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.card_logo_url:
            if hasattr(self.card_logo_url, 'to_alipay_dict'):
                params['card_logo_url'] = self.card_logo_url.to_alipay_dict()
            else:
                params['card_logo_url'] = self.card_logo_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.level_show_name:
            if hasattr(self.level_show_name, 'to_alipay_dict'):
                params['level_show_name'] = self.level_show_name.to_alipay_dict()
            else:
                params['level_show_name'] = self.level_show_name
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
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
        o = MallCardBo()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'card_logo_url' in d:
            o.card_logo_url = d['card_logo_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'level_show_name' in d:
            o.level_show_name = d['level_show_name']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'title' in d:
            o.title = d['title']
        return o


