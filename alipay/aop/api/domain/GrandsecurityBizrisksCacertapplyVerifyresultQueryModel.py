#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GrandsecurityBizrisksCacertapplyVerifyresultQueryModel(object):

    def __init__(self):
        self._ext_params = None
        self._user_no = None
        self._verify_id = None

    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def user_no(self):
        return self._user_no

    @user_no.setter
    def user_no(self, value):
        self._user_no = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.user_no:
            if hasattr(self.user_no, 'to_alipay_dict'):
                params['user_no'] = self.user_no.to_alipay_dict()
            else:
                params['user_no'] = self.user_no
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrandsecurityBizrisksCacertapplyVerifyresultQueryModel()
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'user_no' in d:
            o.user_no = d['user_no']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


