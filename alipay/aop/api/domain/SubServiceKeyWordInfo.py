#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyWordInfo import KeyWordInfo


class SubServiceKeyWordInfo(object):

    def __init__(self):
        self._app_name = None
        self._keyword_info = None
        self._mini_app_id = None
        self._sub_service_code = None
        self._sub_service_desc = None
        self._sub_service_name = None
        self._sub_service_status = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def keyword_info(self):
        return self._keyword_info

    @keyword_info.setter
    def keyword_info(self, value):
        if isinstance(value, list):
            self._keyword_info = list()
            for i in value:
                if isinstance(i, KeyWordInfo):
                    self._keyword_info.append(i)
                else:
                    self._keyword_info.append(KeyWordInfo.from_alipay_dict(i))
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def sub_service_code(self):
        return self._sub_service_code

    @sub_service_code.setter
    def sub_service_code(self, value):
        self._sub_service_code = value
    @property
    def sub_service_desc(self):
        return self._sub_service_desc

    @sub_service_desc.setter
    def sub_service_desc(self, value):
        self._sub_service_desc = value
    @property
    def sub_service_name(self):
        return self._sub_service_name

    @sub_service_name.setter
    def sub_service_name(self, value):
        self._sub_service_name = value
    @property
    def sub_service_status(self):
        return self._sub_service_status

    @sub_service_status.setter
    def sub_service_status(self, value):
        self._sub_service_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.keyword_info:
            if isinstance(self.keyword_info, list):
                for i in range(0, len(self.keyword_info)):
                    element = self.keyword_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_info[i] = element.to_alipay_dict()
            if hasattr(self.keyword_info, 'to_alipay_dict'):
                params['keyword_info'] = self.keyword_info.to_alipay_dict()
            else:
                params['keyword_info'] = self.keyword_info
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.sub_service_code:
            if hasattr(self.sub_service_code, 'to_alipay_dict'):
                params['sub_service_code'] = self.sub_service_code.to_alipay_dict()
            else:
                params['sub_service_code'] = self.sub_service_code
        if self.sub_service_desc:
            if hasattr(self.sub_service_desc, 'to_alipay_dict'):
                params['sub_service_desc'] = self.sub_service_desc.to_alipay_dict()
            else:
                params['sub_service_desc'] = self.sub_service_desc
        if self.sub_service_name:
            if hasattr(self.sub_service_name, 'to_alipay_dict'):
                params['sub_service_name'] = self.sub_service_name.to_alipay_dict()
            else:
                params['sub_service_name'] = self.sub_service_name
        if self.sub_service_status:
            if hasattr(self.sub_service_status, 'to_alipay_dict'):
                params['sub_service_status'] = self.sub_service_status.to_alipay_dict()
            else:
                params['sub_service_status'] = self.sub_service_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubServiceKeyWordInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'keyword_info' in d:
            o.keyword_info = d['keyword_info']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'sub_service_code' in d:
            o.sub_service_code = d['sub_service_code']
        if 'sub_service_desc' in d:
            o.sub_service_desc = d['sub_service_desc']
        if 'sub_service_name' in d:
            o.sub_service_name = d['sub_service_name']
        if 'sub_service_status' in d:
            o.sub_service_status = d['sub_service_status']
        return o


