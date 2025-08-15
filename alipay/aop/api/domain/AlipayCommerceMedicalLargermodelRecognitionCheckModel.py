#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelRecognitionCheckModel(object):

    def __init__(self):
        self._app_type = None
        self._business_type = None
        self._channel_type = None
        self._field_id = None
        self._org_id = None
        self._out_user_id = None
        self._out_user_type = None
        self._scene_code = None
        self._url = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def field_id(self):
        return self._field_id

    @field_id.setter
    def field_id(self, value):
        self._field_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.field_id:
            if hasattr(self.field_id, 'to_alipay_dict'):
                params['field_id'] = self.field_id.to_alipay_dict()
            else:
                params['field_id'] = self.field_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        o = AlipayCommerceMedicalLargermodelRecognitionCheckModel()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'field_id' in d:
            o.field_id = d['field_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'url' in d:
            o.url = d['url']
        return o


