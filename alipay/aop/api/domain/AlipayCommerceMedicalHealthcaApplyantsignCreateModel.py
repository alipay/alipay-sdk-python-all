#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntSignFile import AntSignFile
from alipay.aop.api.domain.AntSignUserInfo import AntSignUserInfo


class AlipayCommerceMedicalHealthcaApplyantsignCreateModel(object):

    def __init__(self):
        self._ant_sign_file_list = None
        self._ant_sign_user_info_list = None
        self._biz_type = None
        self._request_id = None

    @property
    def ant_sign_file_list(self):
        return self._ant_sign_file_list

    @ant_sign_file_list.setter
    def ant_sign_file_list(self, value):
        if isinstance(value, list):
            self._ant_sign_file_list = list()
            for i in value:
                if isinstance(i, AntSignFile):
                    self._ant_sign_file_list.append(i)
                else:
                    self._ant_sign_file_list.append(AntSignFile.from_alipay_dict(i))
    @property
    def ant_sign_user_info_list(self):
        return self._ant_sign_user_info_list

    @ant_sign_user_info_list.setter
    def ant_sign_user_info_list(self, value):
        if isinstance(value, list):
            self._ant_sign_user_info_list = list()
            for i in value:
                if isinstance(i, AntSignUserInfo):
                    self._ant_sign_user_info_list.append(i)
                else:
                    self._ant_sign_user_info_list.append(AntSignUserInfo.from_alipay_dict(i))
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_sign_file_list:
            if isinstance(self.ant_sign_file_list, list):
                for i in range(0, len(self.ant_sign_file_list)):
                    element = self.ant_sign_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_file_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_file_list, 'to_alipay_dict'):
                params['ant_sign_file_list'] = self.ant_sign_file_list.to_alipay_dict()
            else:
                params['ant_sign_file_list'] = self.ant_sign_file_list
        if self.ant_sign_user_info_list:
            if isinstance(self.ant_sign_user_info_list, list):
                for i in range(0, len(self.ant_sign_user_info_list)):
                    element = self.ant_sign_user_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_user_info_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_user_info_list, 'to_alipay_dict'):
                params['ant_sign_user_info_list'] = self.ant_sign_user_info_list.to_alipay_dict()
            else:
                params['ant_sign_user_info_list'] = self.ant_sign_user_info_list
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        o = AlipayCommerceMedicalHealthcaApplyantsignCreateModel()
        if 'ant_sign_file_list' in d:
            o.ant_sign_file_list = d['ant_sign_file_list']
        if 'ant_sign_user_info_list' in d:
            o.ant_sign_user_info_list = d['ant_sign_user_info_list']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


