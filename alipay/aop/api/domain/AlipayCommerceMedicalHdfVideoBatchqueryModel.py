#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfVideoBatchqueryModel(object):

    def __init__(self):
        self._auth = None
        self._auth_params = None
        self._biz = None
        self._expire_seconds = None
        self._owner_id = None
        self._video_id_list = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def auth_params(self):
        return self._auth_params

    @auth_params.setter
    def auth_params(self, value):
        self._auth_params = value
    @property
    def biz(self):
        return self._biz

    @biz.setter
    def biz(self, value):
        self._biz = value
    @property
    def expire_seconds(self):
        return self._expire_seconds

    @expire_seconds.setter
    def expire_seconds(self, value):
        self._expire_seconds = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def video_id_list(self):
        return self._video_id_list

    @video_id_list.setter
    def video_id_list(self, value):
        if isinstance(value, list):
            self._video_id_list = list()
            for i in value:
                self._video_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.auth:
            if hasattr(self.auth, 'to_alipay_dict'):
                params['auth'] = self.auth.to_alipay_dict()
            else:
                params['auth'] = self.auth
        if self.auth_params:
            if hasattr(self.auth_params, 'to_alipay_dict'):
                params['auth_params'] = self.auth_params.to_alipay_dict()
            else:
                params['auth_params'] = self.auth_params
        if self.biz:
            if hasattr(self.biz, 'to_alipay_dict'):
                params['biz'] = self.biz.to_alipay_dict()
            else:
                params['biz'] = self.biz
        if self.expire_seconds:
            if hasattr(self.expire_seconds, 'to_alipay_dict'):
                params['expire_seconds'] = self.expire_seconds.to_alipay_dict()
            else:
                params['expire_seconds'] = self.expire_seconds
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.video_id_list:
            if isinstance(self.video_id_list, list):
                for i in range(0, len(self.video_id_list)):
                    element = self.video_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_id_list[i] = element.to_alipay_dict()
            if hasattr(self.video_id_list, 'to_alipay_dict'):
                params['video_id_list'] = self.video_id_list.to_alipay_dict()
            else:
                params['video_id_list'] = self.video_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfVideoBatchqueryModel()
        if 'auth' in d:
            o.auth = d['auth']
        if 'auth_params' in d:
            o.auth_params = d['auth_params']
        if 'biz' in d:
            o.biz = d['biz']
        if 'expire_seconds' in d:
            o.expire_seconds = d['expire_seconds']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'video_id_list' in d:
            o.video_id_list = d['video_id_list']
        return o


