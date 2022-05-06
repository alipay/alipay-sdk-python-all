#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotVspOrgUserWithVidAddUserInfoRequest import IotVspOrgUserWithVidAddUserInfoRequest


class AlipayOpenIotvspUserwithvidCreateModel(object):

    def __init__(self):
        self._component_out_id = None
        self._isv_pid = None
        self._org_out_id = None
        self._user_info_list = None

    @property
    def component_out_id(self):
        return self._component_out_id

    @component_out_id.setter
    def component_out_id(self, value):
        self._component_out_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def org_out_id(self):
        return self._org_out_id

    @org_out_id.setter
    def org_out_id(self, value):
        self._org_out_id = value
    @property
    def user_info_list(self):
        return self._user_info_list

    @user_info_list.setter
    def user_info_list(self, value):
        if isinstance(value, list):
            self._user_info_list = list()
            for i in value:
                if isinstance(i, IotVspOrgUserWithVidAddUserInfoRequest):
                    self._user_info_list.append(i)
                else:
                    self._user_info_list.append(IotVspOrgUserWithVidAddUserInfoRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.component_out_id:
            if hasattr(self.component_out_id, 'to_alipay_dict'):
                params['component_out_id'] = self.component_out_id.to_alipay_dict()
            else:
                params['component_out_id'] = self.component_out_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.org_out_id:
            if hasattr(self.org_out_id, 'to_alipay_dict'):
                params['org_out_id'] = self.org_out_id.to_alipay_dict()
            else:
                params['org_out_id'] = self.org_out_id
        if self.user_info_list:
            if isinstance(self.user_info_list, list):
                for i in range(0, len(self.user_info_list)):
                    element = self.user_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_info_list[i] = element.to_alipay_dict()
            if hasattr(self.user_info_list, 'to_alipay_dict'):
                params['user_info_list'] = self.user_info_list.to_alipay_dict()
            else:
                params['user_info_list'] = self.user_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotvspUserwithvidCreateModel()
        if 'component_out_id' in d:
            o.component_out_id = d['component_out_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'org_out_id' in d:
            o.org_out_id = d['org_out_id']
        if 'user_info_list' in d:
            o.user_info_list = d['user_info_list']
        return o


