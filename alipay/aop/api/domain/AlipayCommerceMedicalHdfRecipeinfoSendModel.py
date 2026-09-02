#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecipeInfo import RecipeInfo


class AlipayCommerceMedicalHdfRecipeinfoSendModel(object):

    def __init__(self):
        self._app_name = None
        self._event_code = None
        self._out_biz_id = None
        self._recipeinfo = None
        self._request_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def recipeinfo(self):
        return self._recipeinfo

    @recipeinfo.setter
    def recipeinfo(self, value):
        if isinstance(value, RecipeInfo):
            self._recipeinfo = value
        else:
            self._recipeinfo = RecipeInfo.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.recipeinfo:
            if hasattr(self.recipeinfo, 'to_alipay_dict'):
                params['recipeinfo'] = self.recipeinfo.to_alipay_dict()
            else:
                params['recipeinfo'] = self.recipeinfo
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfRecipeinfoSendModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'recipeinfo' in d:
            o.recipeinfo = d['recipeinfo']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


