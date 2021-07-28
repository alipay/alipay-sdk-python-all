#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMerchantIndividualCreateModel(object):

    def __init__(self):
        self._business_license = None
        self._business_license_pic = None
        self._user_id = None

    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_license:
            if hasattr(self.business_license, 'to_alipay_dict'):
                params['business_license'] = self.business_license.to_alipay_dict()
            else:
                params['business_license'] = self.business_license
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
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
        o = AntMerchantExpandMerchantIndividualCreateModel()
        if 'business_license' in d:
            o.business_license = d['business_license']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


