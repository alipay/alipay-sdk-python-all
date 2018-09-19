#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCardActivateurlApplyModel(object):

    def __init__(self):
        self._callback = None
        self._follow_app_id = None
        self._out_string = None
        self._template_id = None

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value
    @property
    def follow_app_id(self):
        return self._follow_app_id

    @follow_app_id.setter
    def follow_app_id(self, value):
        self._follow_app_id = value
    @property
    def out_string(self):
        return self._out_string

    @out_string.setter
    def out_string(self, value):
        self._out_string = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback:
            if hasattr(self.callback, 'to_alipay_dict'):
                params['callback'] = self.callback.to_alipay_dict()
            else:
                params['callback'] = self.callback
        if self.follow_app_id:
            if hasattr(self.follow_app_id, 'to_alipay_dict'):
                params['follow_app_id'] = self.follow_app_id.to_alipay_dict()
            else:
                params['follow_app_id'] = self.follow_app_id
        if self.out_string:
            if hasattr(self.out_string, 'to_alipay_dict'):
                params['out_string'] = self.out_string.to_alipay_dict()
            else:
                params['out_string'] = self.out_string
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardActivateurlApplyModel()
        if 'callback' in d:
            o.callback = d['callback']
        if 'follow_app_id' in d:
            o.follow_app_id = d['follow_app_id']
        if 'out_string' in d:
            o.out_string = d['out_string']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


