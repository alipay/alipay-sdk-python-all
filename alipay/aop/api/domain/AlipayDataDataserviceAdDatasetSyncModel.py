#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdDatasetSyncModel(object):

    def __init__(self):
        self._biz_token = None
        self._data_id = None
        self._data_name = None
        self._data_src_type = None
        self._data_table_name = None
        self._data_type = None
        self._principal_id = None
        self._principal_tag = None
        self._status = None
        self._user_unique_type = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def data_src_type(self):
        return self._data_src_type

    @data_src_type.setter
    def data_src_type(self, value):
        self._data_src_type = value
    @property
    def data_table_name(self):
        return self._data_table_name

    @data_table_name.setter
    def data_table_name(self, value):
        self._data_table_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_unique_type(self):
        return self._user_unique_type

    @user_unique_type.setter
    def user_unique_type(self, value):
        self._user_unique_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.data_src_type:
            if hasattr(self.data_src_type, 'to_alipay_dict'):
                params['data_src_type'] = self.data_src_type.to_alipay_dict()
            else:
                params['data_src_type'] = self.data_src_type
        if self.data_table_name:
            if hasattr(self.data_table_name, 'to_alipay_dict'):
                params['data_table_name'] = self.data_table_name.to_alipay_dict()
            else:
                params['data_table_name'] = self.data_table_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_unique_type:
            if hasattr(self.user_unique_type, 'to_alipay_dict'):
                params['user_unique_type'] = self.user_unique_type.to_alipay_dict()
            else:
                params['user_unique_type'] = self.user_unique_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdDatasetSyncModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'data_src_type' in d:
            o.data_src_type = d['data_src_type']
        if 'data_table_name' in d:
            o.data_table_name = d['data_table_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'status' in d:
            o.status = d['status']
        if 'user_unique_type' in d:
            o.user_unique_type = d['user_unique_type']
        return o


