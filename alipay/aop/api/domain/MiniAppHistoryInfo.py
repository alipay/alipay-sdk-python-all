#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppHistoryInfo(object):

    def __init__(self):
        self._ext_info = None
        self._icon_url = None
        self._link = None
        self._mini_app_id = None
        self._name = None
        self._slogan = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.slogan:
            if hasattr(self.slogan, 'to_alipay_dict'):
                params['slogan'] = self.slogan.to_alipay_dict()
            else:
                params['slogan'] = self.slogan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppHistoryInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'link' in d:
            o.link = d['link']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'name' in d:
            o.name = d['name']
        if 'slogan' in d:
            o.slogan = d['slogan']
        return o


