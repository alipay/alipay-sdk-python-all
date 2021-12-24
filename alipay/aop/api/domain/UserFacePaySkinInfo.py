#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserFacePaySkinInfo(object):

    def __init__(self):
        self._client_version_limit = None
        self._expire_date = None
        self._name = None
        self._setting_link = None
        self._skin_id = None
        self._status = None
        self._thumbnail = None

    @property
    def client_version_limit(self):
        return self._client_version_limit

    @client_version_limit.setter
    def client_version_limit(self, value):
        self._client_version_limit = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def setting_link(self):
        return self._setting_link

    @setting_link.setter
    def setting_link(self, value):
        self._setting_link = value
    @property
    def skin_id(self):
        return self._skin_id

    @skin_id.setter
    def skin_id(self, value):
        self._skin_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_version_limit:
            if hasattr(self.client_version_limit, 'to_alipay_dict'):
                params['client_version_limit'] = self.client_version_limit.to_alipay_dict()
            else:
                params['client_version_limit'] = self.client_version_limit
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.setting_link:
            if hasattr(self.setting_link, 'to_alipay_dict'):
                params['setting_link'] = self.setting_link.to_alipay_dict()
            else:
                params['setting_link'] = self.setting_link
        if self.skin_id:
            if hasattr(self.skin_id, 'to_alipay_dict'):
                params['skin_id'] = self.skin_id.to_alipay_dict()
            else:
                params['skin_id'] = self.skin_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.thumbnail:
            if hasattr(self.thumbnail, 'to_alipay_dict'):
                params['thumbnail'] = self.thumbnail.to_alipay_dict()
            else:
                params['thumbnail'] = self.thumbnail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserFacePaySkinInfo()
        if 'client_version_limit' in d:
            o.client_version_limit = d['client_version_limit']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'name' in d:
            o.name = d['name']
        if 'setting_link' in d:
            o.setting_link = d['setting_link']
        if 'skin_id' in d:
            o.skin_id = d['skin_id']
        if 'status' in d:
            o.status = d['status']
        if 'thumbnail' in d:
            o.thumbnail = d['thumbnail']
        return o


