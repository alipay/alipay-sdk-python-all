#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetSubFeedbackInfo import AssetSubFeedbackInfo


class AssetCallbackInfo(object):

    def __init__(self):
        self._biz_action = None
        self._biz_key_value = None
        self._callback_infos = None
        self._error_code = None
        self._error_desc = None
        self._success = None

    @property
    def biz_action(self):
        return self._biz_action

    @biz_action.setter
    def biz_action(self, value):
        self._biz_action = value
    @property
    def biz_key_value(self):
        return self._biz_key_value

    @biz_key_value.setter
    def biz_key_value(self, value):
        self._biz_key_value = value
    @property
    def callback_infos(self):
        return self._callback_infos

    @callback_infos.setter
    def callback_infos(self, value):
        if isinstance(value, list):
            self._callback_infos = list()
            for i in value:
                if isinstance(i, AssetSubFeedbackInfo):
                    self._callback_infos.append(i)
                else:
                    self._callback_infos.append(AssetSubFeedbackInfo.from_alipay_dict(i))
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_action:
            if hasattr(self.biz_action, 'to_alipay_dict'):
                params['biz_action'] = self.biz_action.to_alipay_dict()
            else:
                params['biz_action'] = self.biz_action
        if self.biz_key_value:
            if hasattr(self.biz_key_value, 'to_alipay_dict'):
                params['biz_key_value'] = self.biz_key_value.to_alipay_dict()
            else:
                params['biz_key_value'] = self.biz_key_value
        if self.callback_infos:
            if isinstance(self.callback_infos, list):
                for i in range(0, len(self.callback_infos)):
                    element = self.callback_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.callback_infos[i] = element.to_alipay_dict()
            if hasattr(self.callback_infos, 'to_alipay_dict'):
                params['callback_infos'] = self.callback_infos.to_alipay_dict()
            else:
                params['callback_infos'] = self.callback_infos
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetCallbackInfo()
        if 'biz_action' in d:
            o.biz_action = d['biz_action']
        if 'biz_key_value' in d:
            o.biz_key_value = d['biz_key_value']
        if 'callback_infos' in d:
            o.callback_infos = d['callback_infos']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'success' in d:
            o.success = d['success']
        return o


