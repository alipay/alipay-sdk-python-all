#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaDataStateDataSyncModel(object):

    def __init__(self):
        self._biz_data = None
        self._biz_state_code = None
        self._category_code = None
        self._out_biz_no = None
        self._out_principal_id = None
        self._service_id = None
        self._user_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def biz_state_code(self):
        return self._biz_state_code

    @biz_state_code.setter
    def biz_state_code(self, value):
        self._biz_state_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_principal_id(self):
        return self._out_principal_id

    @out_principal_id.setter
    def out_principal_id(self, value):
        self._out_principal_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biz_state_code:
            if hasattr(self.biz_state_code, 'to_alipay_dict'):
                params['biz_state_code'] = self.biz_state_code.to_alipay_dict()
            else:
                params['biz_state_code'] = self.biz_state_code
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_principal_id:
            if hasattr(self.out_principal_id, 'to_alipay_dict'):
                params['out_principal_id'] = self.out_principal_id.to_alipay_dict()
            else:
                params['out_principal_id'] = self.out_principal_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
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
        o = ZhimaDataStateDataSyncModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biz_state_code' in d:
            o.biz_state_code = d['biz_state_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_principal_id' in d:
            o.out_principal_id = d['out_principal_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


