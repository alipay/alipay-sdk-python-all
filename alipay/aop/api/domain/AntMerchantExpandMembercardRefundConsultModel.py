#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMembercardRefundConsultModel(object):

    def __init__(self):
        self._member_product_id = None
        self._user_id = None

    @property
    def member_product_id(self):
        return self._member_product_id

    @member_product_id.setter
    def member_product_id(self, value):
        self._member_product_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_product_id:
            if hasattr(self.member_product_id, 'to_alipay_dict'):
                params['member_product_id'] = self.member_product_id.to_alipay_dict()
            else:
                params['member_product_id'] = self.member_product_id
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
        o = AntMerchantExpandMembercardRefundConsultModel()
        if 'member_product_id' in d:
            o.member_product_id = d['member_product_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


