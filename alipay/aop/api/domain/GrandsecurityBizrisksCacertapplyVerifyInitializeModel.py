#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaCertApplyUser import CaCertApplyUser


class GrandsecurityBizrisksCacertapplyVerifyInitializeModel(object):

    def __init__(self):
        self._business_id = None
        self._ext_params = None
        self._product_list = None
        self._user = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        self._product_list = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, CaCertApplyUser):
            self._user = value
        else:
            self._user = CaCertApplyUser.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.product_list:
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrandsecurityBizrisksCacertapplyVerifyInitializeModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'user' in d:
            o.user = d['user']
        return o


