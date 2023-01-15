#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessWebAppDTO(object):

    def __init__(self):
        self._account = None
        self._app_status = None
        self._app_type = None
        self._ext_pictures = None
        self._icp_auth_pic = None
        self._icp_licence_pic = None
        self._memo = None
        self._password = None
        self._screenshot = None
        self._url = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def ext_pictures(self):
        return self._ext_pictures

    @ext_pictures.setter
    def ext_pictures(self, value):
        if isinstance(value, list):
            self._ext_pictures = list()
            for i in value:
                self._ext_pictures.append(i)
    @property
    def icp_auth_pic(self):
        return self._icp_auth_pic

    @icp_auth_pic.setter
    def icp_auth_pic(self, value):
        self._icp_auth_pic = value
    @property
    def icp_licence_pic(self):
        return self._icp_licence_pic

    @icp_licence_pic.setter
    def icp_licence_pic(self, value):
        self._icp_licence_pic = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def screenshot(self):
        return self._screenshot

    @screenshot.setter
    def screenshot(self, value):
        if isinstance(value, list):
            self._screenshot = list()
            for i in value:
                self._screenshot.append(i)
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.ext_pictures:
            if isinstance(self.ext_pictures, list):
                for i in range(0, len(self.ext_pictures)):
                    element = self.ext_pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_pictures[i] = element.to_alipay_dict()
            if hasattr(self.ext_pictures, 'to_alipay_dict'):
                params['ext_pictures'] = self.ext_pictures.to_alipay_dict()
            else:
                params['ext_pictures'] = self.ext_pictures
        if self.icp_auth_pic:
            if hasattr(self.icp_auth_pic, 'to_alipay_dict'):
                params['icp_auth_pic'] = self.icp_auth_pic.to_alipay_dict()
            else:
                params['icp_auth_pic'] = self.icp_auth_pic
        if self.icp_licence_pic:
            if hasattr(self.icp_licence_pic, 'to_alipay_dict'):
                params['icp_licence_pic'] = self.icp_licence_pic.to_alipay_dict()
            else:
                params['icp_licence_pic'] = self.icp_licence_pic
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.screenshot:
            if isinstance(self.screenshot, list):
                for i in range(0, len(self.screenshot)):
                    element = self.screenshot[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.screenshot[i] = element.to_alipay_dict()
            if hasattr(self.screenshot, 'to_alipay_dict'):
                params['screenshot'] = self.screenshot.to_alipay_dict()
            else:
                params['screenshot'] = self.screenshot
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
        o = BusinessWebAppDTO()
        if 'account' in d:
            o.account = d['account']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'ext_pictures' in d:
            o.ext_pictures = d['ext_pictures']
        if 'icp_auth_pic' in d:
            o.icp_auth_pic = d['icp_auth_pic']
        if 'icp_licence_pic' in d:
            o.icp_licence_pic = d['icp_licence_pic']
        if 'memo' in d:
            o.memo = d['memo']
        if 'password' in d:
            o.password = d['password']
        if 'screenshot' in d:
            o.screenshot = d['screenshot']
        if 'url' in d:
            o.url = d['url']
        return o


