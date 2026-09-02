#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerModifyModel(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._belong_contractor_cert_no = None
        self._belong_family_head_cert_no = None
        self._farmer_id = None
        self._farmer_name = None
        self._is_contractor = None
        self._is_family_master = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def belong_contractor_cert_no(self):
        return self._belong_contractor_cert_no

    @belong_contractor_cert_no.setter
    def belong_contractor_cert_no(self, value):
        self._belong_contractor_cert_no = value
    @property
    def belong_family_head_cert_no(self):
        return self._belong_family_head_cert_no

    @belong_family_head_cert_no.setter
    def belong_family_head_cert_no(self, value):
        self._belong_family_head_cert_no = value
    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value
    @property
    def farmer_name(self):
        return self._farmer_name

    @farmer_name.setter
    def farmer_name(self, value):
        self._farmer_name = value
    @property
    def is_contractor(self):
        return self._is_contractor

    @is_contractor.setter
    def is_contractor(self, value):
        self._is_contractor = value
    @property
    def is_family_master(self):
        return self._is_family_master

    @is_family_master.setter
    def is_family_master(self, value):
        self._is_family_master = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.belong_contractor_cert_no:
            if hasattr(self.belong_contractor_cert_no, 'to_alipay_dict'):
                params['belong_contractor_cert_no'] = self.belong_contractor_cert_no.to_alipay_dict()
            else:
                params['belong_contractor_cert_no'] = self.belong_contractor_cert_no
        if self.belong_family_head_cert_no:
            if hasattr(self.belong_family_head_cert_no, 'to_alipay_dict'):
                params['belong_family_head_cert_no'] = self.belong_family_head_cert_no.to_alipay_dict()
            else:
                params['belong_family_head_cert_no'] = self.belong_family_head_cert_no
        if self.farmer_id:
            if hasattr(self.farmer_id, 'to_alipay_dict'):
                params['farmer_id'] = self.farmer_id.to_alipay_dict()
            else:
                params['farmer_id'] = self.farmer_id
        if self.farmer_name:
            if hasattr(self.farmer_name, 'to_alipay_dict'):
                params['farmer_name'] = self.farmer_name.to_alipay_dict()
            else:
                params['farmer_name'] = self.farmer_name
        if self.is_contractor:
            if hasattr(self.is_contractor, 'to_alipay_dict'):
                params['is_contractor'] = self.is_contractor.to_alipay_dict()
            else:
                params['is_contractor'] = self.is_contractor
        if self.is_family_master:
            if hasattr(self.is_family_master, 'to_alipay_dict'):
                params['is_family_master'] = self.is_family_master.to_alipay_dict()
            else:
                params['is_family_master'] = self.is_family_master
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerModifyModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'belong_contractor_cert_no' in d:
            o.belong_contractor_cert_no = d['belong_contractor_cert_no']
        if 'belong_family_head_cert_no' in d:
            o.belong_family_head_cert_no = d['belong_family_head_cert_no']
        if 'farmer_id' in d:
            o.farmer_id = d['farmer_id']
        if 'farmer_name' in d:
            o.farmer_name = d['farmer_name']
        if 'is_contractor' in d:
            o.is_contractor = d['is_contractor']
        if 'is_family_master' in d:
            o.is_family_master = d['is_family_master']
        return o


