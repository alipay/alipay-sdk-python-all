#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileInfo import FileInfo


class AlipayFincoreComplianceRcsmartContentSubmitModel(object):

    def __init__(self):
        self._app_name = None
        self._app_token = None
        self._biz_code = None
        self._file_info_list = None
        self._request_id = None
        self._scene_code = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def file_info_list(self):
        return self._file_info_list

    @file_info_list.setter
    def file_info_list(self, value):
        if isinstance(value, list):
            self._file_info_list = list()
            for i in value:
                if isinstance(i, FileInfo):
                    self._file_info_list.append(i)
                else:
                    self._file_info_list.append(FileInfo.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.file_info_list:
            if isinstance(self.file_info_list, list):
                for i in range(0, len(self.file_info_list)):
                    element = self.file_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_info_list[i] = element.to_alipay_dict()
            if hasattr(self.file_info_list, 'to_alipay_dict'):
                params['file_info_list'] = self.file_info_list.to_alipay_dict()
            else:
                params['file_info_list'] = self.file_info_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcsmartContentSubmitModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'file_info_list' in d:
            o.file_info_list = d['file_info_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


