#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterPhotoUploadModel(object):

    def __init__(self):
        self._cert_no = None
        self._encrypted = None
        self._open_id = None
        self._photo_url = None
        self._user_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def encrypted(self):
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def photo_url(self):
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        self._photo_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.encrypted:
            if hasattr(self.encrypted, 'to_alipay_dict'):
                params['encrypted'] = self.encrypted.to_alipay_dict()
            else:
                params['encrypted'] = self.encrypted
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.photo_url:
            if hasattr(self.photo_url, 'to_alipay_dict'):
                params['photo_url'] = self.photo_url.to_alipay_dict()
            else:
                params['photo_url'] = self.photo_url
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterPhotoUploadModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'encrypted' in d:
            o.encrypted = d['encrypted']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'photo_url' in d:
            o.photo_url = d['photo_url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


