#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniInstantiateInfo(object):

    def __init__(self):
        self._app_name = None
        self._latest_version = None
        self._latest_version_status = None
        self._logo_url = None
        self._mini_app_id = None
        self._qr_code_url = None
        self._status = None
        self._template_id = None
        self._template_name = None
        self._template_version = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def latest_version(self):
        return self._latest_version

    @latest_version.setter
    def latest_version(self, value):
        self._latest_version = value
    @property
    def latest_version_status(self):
        return self._latest_version_status

    @latest_version_status.setter
    def latest_version_status(self, value):
        self._latest_version_status = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.latest_version:
            if hasattr(self.latest_version, 'to_alipay_dict'):
                params['latest_version'] = self.latest_version.to_alipay_dict()
            else:
                params['latest_version'] = self.latest_version
        if self.latest_version_status:
            if hasattr(self.latest_version_status, 'to_alipay_dict'):
                params['latest_version_status'] = self.latest_version_status.to_alipay_dict()
            else:
                params['latest_version_status'] = self.latest_version_status
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniInstantiateInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'latest_version' in d:
            o.latest_version = d['latest_version']
        if 'latest_version_status' in d:
            o.latest_version_status = d['latest_version_status']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_version' in d:
            o.template_version = d['template_version']
        return o


