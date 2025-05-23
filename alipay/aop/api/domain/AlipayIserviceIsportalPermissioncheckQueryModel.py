#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsportalPermissioncheckQueryModel(object):

    def __init__(self):
        self._busvc_cloud_id = None
        self._busvc_id = None
        self._clv_user_id = None
        self._codes = None
        self._tnt_inst_id = None
        self._ur_id = None
        self._uri = None
        self._user_id = None

    @property
    def busvc_cloud_id(self):
        return self._busvc_cloud_id

    @busvc_cloud_id.setter
    def busvc_cloud_id(self, value):
        self._busvc_cloud_id = value
    @property
    def busvc_id(self):
        return self._busvc_id

    @busvc_id.setter
    def busvc_id(self, value):
        self._busvc_id = value
    @property
    def clv_user_id(self):
        return self._clv_user_id

    @clv_user_id.setter
    def clv_user_id(self, value):
        self._clv_user_id = value
    @property
    def codes(self):
        return self._codes

    @codes.setter
    def codes(self, value):
        if isinstance(value, list):
            self._codes = list()
            for i in value:
                self._codes.append(i)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def ur_id(self):
        return self._ur_id

    @ur_id.setter
    def ur_id(self, value):
        self._ur_id = value
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.busvc_cloud_id:
            if hasattr(self.busvc_cloud_id, 'to_alipay_dict'):
                params['busvc_cloud_id'] = self.busvc_cloud_id.to_alipay_dict()
            else:
                params['busvc_cloud_id'] = self.busvc_cloud_id
        if self.busvc_id:
            if hasattr(self.busvc_id, 'to_alipay_dict'):
                params['busvc_id'] = self.busvc_id.to_alipay_dict()
            else:
                params['busvc_id'] = self.busvc_id
        if self.clv_user_id:
            if hasattr(self.clv_user_id, 'to_alipay_dict'):
                params['clv_user_id'] = self.clv_user_id.to_alipay_dict()
            else:
                params['clv_user_id'] = self.clv_user_id
        if self.codes:
            if isinstance(self.codes, list):
                for i in range(0, len(self.codes)):
                    element = self.codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.codes[i] = element.to_alipay_dict()
            if hasattr(self.codes, 'to_alipay_dict'):
                params['codes'] = self.codes.to_alipay_dict()
            else:
                params['codes'] = self.codes
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.ur_id:
            if hasattr(self.ur_id, 'to_alipay_dict'):
                params['ur_id'] = self.ur_id.to_alipay_dict()
            else:
                params['ur_id'] = self.ur_id
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = self.uri.to_alipay_dict()
            else:
                params['uri'] = self.uri
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
        o = AlipayIserviceIsportalPermissioncheckQueryModel()
        if 'busvc_cloud_id' in d:
            o.busvc_cloud_id = d['busvc_cloud_id']
        if 'busvc_id' in d:
            o.busvc_id = d['busvc_id']
        if 'clv_user_id' in d:
            o.clv_user_id = d['clv_user_id']
        if 'codes' in d:
            o.codes = d['codes']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'ur_id' in d:
            o.ur_id = d['ur_id']
        if 'uri' in d:
            o.uri = d['uri']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


