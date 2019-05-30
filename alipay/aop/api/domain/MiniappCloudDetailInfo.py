#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniappCloudDetailInfo(object):

    def __init__(self):
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._category_names = None
        self._create_time = None
        self._mini_appid = None

    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def category_names(self):
        return self._category_names

    @category_names.setter
    def category_names(self, value):
        self._category_names = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def mini_appid(self):
        return self._mini_appid

    @mini_appid.setter
    def mini_appid(self, value):
        self._mini_appid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_english_name:
            if hasattr(self.app_english_name, 'to_alipay_dict'):
                params['app_english_name'] = self.app_english_name.to_alipay_dict()
            else:
                params['app_english_name'] = self.app_english_name
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.category_names:
            if hasattr(self.category_names, 'to_alipay_dict'):
                params['category_names'] = self.category_names.to_alipay_dict()
            else:
                params['category_names'] = self.category_names
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.mini_appid:
            if hasattr(self.mini_appid, 'to_alipay_dict'):
                params['mini_appid'] = self.mini_appid.to_alipay_dict()
            else:
                params['mini_appid'] = self.mini_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniappCloudDetailInfo()
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_english_name' in d:
            o.app_english_name = d['app_english_name']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'category_names' in d:
            o.category_names = d['category_names']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'mini_appid' in d:
            o.mini_appid = d['mini_appid']
        return o


