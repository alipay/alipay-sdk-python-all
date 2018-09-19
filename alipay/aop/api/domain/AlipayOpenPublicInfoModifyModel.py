#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicInfoModifyModel(object):

    def __init__(self):
        self._app_name = None
        self._auth_pic = None
        self._background_url = None
        self._introduction = None
        self._license_url = None
        self._logo_url = None
        self._public_greeting = None
        self._shop_pics = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def auth_pic(self):
        return self._auth_pic

    @auth_pic.setter
    def auth_pic(self, value):
        self._auth_pic = value
    @property
    def background_url(self):
        return self._background_url

    @background_url.setter
    def background_url(self, value):
        self._background_url = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def license_url(self):
        return self._license_url

    @license_url.setter
    def license_url(self, value):
        self._license_url = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def public_greeting(self):
        return self._public_greeting

    @public_greeting.setter
    def public_greeting(self, value):
        self._public_greeting = value
    @property
    def shop_pics(self):
        return self._shop_pics

    @shop_pics.setter
    def shop_pics(self, value):
        if isinstance(value, list):
            self._shop_pics = list()
            for i in value:
                self._shop_pics.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.auth_pic:
            if hasattr(self.auth_pic, 'to_alipay_dict'):
                params['auth_pic'] = self.auth_pic.to_alipay_dict()
            else:
                params['auth_pic'] = self.auth_pic
        if self.background_url:
            if hasattr(self.background_url, 'to_alipay_dict'):
                params['background_url'] = self.background_url.to_alipay_dict()
            else:
                params['background_url'] = self.background_url
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.license_url:
            if hasattr(self.license_url, 'to_alipay_dict'):
                params['license_url'] = self.license_url.to_alipay_dict()
            else:
                params['license_url'] = self.license_url
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.public_greeting:
            if hasattr(self.public_greeting, 'to_alipay_dict'):
                params['public_greeting'] = self.public_greeting.to_alipay_dict()
            else:
                params['public_greeting'] = self.public_greeting
        if self.shop_pics:
            if isinstance(self.shop_pics, list):
                for i in range(0, len(self.shop_pics)):
                    element = self.shop_pics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_pics[i] = element.to_alipay_dict()
            if hasattr(self.shop_pics, 'to_alipay_dict'):
                params['shop_pics'] = self.shop_pics.to_alipay_dict()
            else:
                params['shop_pics'] = self.shop_pics
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicInfoModifyModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'auth_pic' in d:
            o.auth_pic = d['auth_pic']
        if 'background_url' in d:
            o.background_url = d['background_url']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'license_url' in d:
            o.license_url = d['license_url']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'public_greeting' in d:
            o.public_greeting = d['public_greeting']
        if 'shop_pics' in d:
            o.shop_pics = d['shop_pics']
        return o


