#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodWhitelistQueryModel(object):

    def __init__(self):
        self._app_project_id = None
        self._group_type = None
        self._group_value = None
        self._user_identify_type = None
        self._user_identify_value = None

    @property
    def app_project_id(self):
        return self._app_project_id

    @app_project_id.setter
    def app_project_id(self, value):
        self._app_project_id = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def group_value(self):
        return self._group_value

    @group_value.setter
    def group_value(self, value):
        self._group_value = value
    @property
    def user_identify_type(self):
        return self._user_identify_type

    @user_identify_type.setter
    def user_identify_type(self, value):
        self._user_identify_type = value
    @property
    def user_identify_value(self):
        return self._user_identify_value

    @user_identify_value.setter
    def user_identify_value(self, value):
        self._user_identify_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_project_id:
            if hasattr(self.app_project_id, 'to_alipay_dict'):
                params['app_project_id'] = self.app_project_id.to_alipay_dict()
            else:
                params['app_project_id'] = self.app_project_id
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.group_value:
            if hasattr(self.group_value, 'to_alipay_dict'):
                params['group_value'] = self.group_value.to_alipay_dict()
            else:
                params['group_value'] = self.group_value
        if self.user_identify_type:
            if hasattr(self.user_identify_type, 'to_alipay_dict'):
                params['user_identify_type'] = self.user_identify_type.to_alipay_dict()
            else:
                params['user_identify_type'] = self.user_identify_type
        if self.user_identify_value:
            if hasattr(self.user_identify_value, 'to_alipay_dict'):
                params['user_identify_value'] = self.user_identify_value.to_alipay_dict()
            else:
                params['user_identify_value'] = self.user_identify_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodWhitelistQueryModel()
        if 'app_project_id' in d:
            o.app_project_id = d['app_project_id']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'group_value' in d:
            o.group_value = d['group_value']
        if 'user_identify_type' in d:
            o.user_identify_type = d['user_identify_type']
        if 'user_identify_value' in d:
            o.user_identify_value = d['user_identify_value']
        return o


