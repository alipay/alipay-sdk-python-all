#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdIrisVerifyModel(object):

    def __init__(self):
        self._biz_token = None
        self._ext_info = None
        self._group_id = None
        self._iris_str = None
        self._operate_type = None
        self._out_app_flag = None
        self._out_biz_no = None
        self._person_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def iris_str(self):
        return self._iris_str

    @iris_str.setter
    def iris_str(self, value):
        self._iris_str = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_app_flag(self):
        return self._out_app_flag

    @out_app_flag.setter
    def out_app_flag(self, value):
        self._out_app_flag = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.iris_str:
            if hasattr(self.iris_str, 'to_alipay_dict'):
                params['iris_str'] = self.iris_str.to_alipay_dict()
            else:
                params['iris_str'] = self.iris_str
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_app_flag:
            if hasattr(self.out_app_flag, 'to_alipay_dict'):
                params['out_app_flag'] = self.out_app_flag.to_alipay_dict()
            else:
                params['out_app_flag'] = self.out_app_flag
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.person_id:
            if hasattr(self.person_id, 'to_alipay_dict'):
                params['person_id'] = self.person_id.to_alipay_dict()
            else:
                params['person_id'] = self.person_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIrisVerifyModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'iris_str' in d:
            o.iris_str = d['iris_str']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_app_flag' in d:
            o.out_app_flag = d['out_app_flag']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'person_id' in d:
            o.person_id = d['person_id']
        return o


