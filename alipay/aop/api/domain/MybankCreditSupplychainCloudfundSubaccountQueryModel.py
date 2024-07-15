#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCloudfundSubaccountQueryModel(object):

    def __init__(self):
        self._account_ext_no = None
        self._buyer = None
        self._ext_data = None
        self._isv_org_id = None

    @property
    def account_ext_no(self):
        return self._account_ext_no

    @account_ext_no.setter
    def account_ext_no(self, value):
        self._account_ext_no = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def isv_org_id(self):
        return self._isv_org_id

    @isv_org_id.setter
    def isv_org_id(self, value):
        self._isv_org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext_no:
            if hasattr(self.account_ext_no, 'to_alipay_dict'):
                params['account_ext_no'] = self.account_ext_no.to_alipay_dict()
            else:
                params['account_ext_no'] = self.account_ext_no
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.isv_org_id:
            if hasattr(self.isv_org_id, 'to_alipay_dict'):
                params['isv_org_id'] = self.isv_org_id.to_alipay_dict()
            else:
                params['isv_org_id'] = self.isv_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainCloudfundSubaccountQueryModel()
        if 'account_ext_no' in d:
            o.account_ext_no = d['account_ext_no']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'isv_org_id' in d:
            o.isv_org_id = d['isv_org_id']
        return o


