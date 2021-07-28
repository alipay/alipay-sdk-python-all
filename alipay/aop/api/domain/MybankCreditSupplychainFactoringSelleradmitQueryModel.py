#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainFactoringSelleradmitQueryModel(object):

    def __init__(self):
        self._buyer_alipay_id = None
        self._list_type = None
        self._pd_code = None
        self._seller_login_id = None

    @property
    def buyer_alipay_id(self):
        return self._buyer_alipay_id

    @buyer_alipay_id.setter
    def buyer_alipay_id(self, value):
        self._buyer_alipay_id = value
    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self, value):
        self._list_type = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_alipay_id:
            if hasattr(self.buyer_alipay_id, 'to_alipay_dict'):
                params['buyer_alipay_id'] = self.buyer_alipay_id.to_alipay_dict()
            else:
                params['buyer_alipay_id'] = self.buyer_alipay_id
        if self.list_type:
            if hasattr(self.list_type, 'to_alipay_dict'):
                params['list_type'] = self.list_type.to_alipay_dict()
            else:
                params['list_type'] = self.list_type
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainFactoringSelleradmitQueryModel()
        if 'buyer_alipay_id' in d:
            o.buyer_alipay_id = d['buyer_alipay_id']
        if 'list_type' in d:
            o.list_type = d['list_type']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        return o


