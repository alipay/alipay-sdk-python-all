#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntSignFileRequest import AntSignFileRequest
from alipay.aop.api.domain.AntSignUserInfoRequest import AntSignUserInfoRequest


class AntSignTaskRequest(object):

    def __init__(self):
        self._ant_sign_file_request_list = None
        self._ant_sign_user_info_request_list = None
        self._description = None
        self._related_business = None
        self._sub_biz_no = None

    @property
    def ant_sign_file_request_list(self):
        return self._ant_sign_file_request_list

    @ant_sign_file_request_list.setter
    def ant_sign_file_request_list(self, value):
        if isinstance(value, list):
            self._ant_sign_file_request_list = list()
            for i in value:
                if isinstance(i, AntSignFileRequest):
                    self._ant_sign_file_request_list.append(i)
                else:
                    self._ant_sign_file_request_list.append(AntSignFileRequest.from_alipay_dict(i))
    @property
    def ant_sign_user_info_request_list(self):
        return self._ant_sign_user_info_request_list

    @ant_sign_user_info_request_list.setter
    def ant_sign_user_info_request_list(self, value):
        if isinstance(value, list):
            self._ant_sign_user_info_request_list = list()
            for i in value:
                if isinstance(i, AntSignUserInfoRequest):
                    self._ant_sign_user_info_request_list.append(i)
                else:
                    self._ant_sign_user_info_request_list.append(AntSignUserInfoRequest.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def related_business(self):
        return self._related_business

    @related_business.setter
    def related_business(self, value):
        self._related_business = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_sign_file_request_list:
            if isinstance(self.ant_sign_file_request_list, list):
                for i in range(0, len(self.ant_sign_file_request_list)):
                    element = self.ant_sign_file_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_file_request_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_file_request_list, 'to_alipay_dict'):
                params['ant_sign_file_request_list'] = self.ant_sign_file_request_list.to_alipay_dict()
            else:
                params['ant_sign_file_request_list'] = self.ant_sign_file_request_list
        if self.ant_sign_user_info_request_list:
            if isinstance(self.ant_sign_user_info_request_list, list):
                for i in range(0, len(self.ant_sign_user_info_request_list)):
                    element = self.ant_sign_user_info_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_user_info_request_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_user_info_request_list, 'to_alipay_dict'):
                params['ant_sign_user_info_request_list'] = self.ant_sign_user_info_request_list.to_alipay_dict()
            else:
                params['ant_sign_user_info_request_list'] = self.ant_sign_user_info_request_list
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.related_business:
            if hasattr(self.related_business, 'to_alipay_dict'):
                params['related_business'] = self.related_business.to_alipay_dict()
            else:
                params['related_business'] = self.related_business
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignTaskRequest()
        if 'ant_sign_file_request_list' in d:
            o.ant_sign_file_request_list = d['ant_sign_file_request_list']
        if 'ant_sign_user_info_request_list' in d:
            o.ant_sign_user_info_request_list = d['ant_sign_user_info_request_list']
        if 'description' in d:
            o.description = d['description']
        if 'related_business' in d:
            o.related_business = d['related_business']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        return o


