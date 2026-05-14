#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclingFarmerItemRequest import RecyclingFarmerItemRequest
from alipay.aop.api.domain.RecyclingProxyRequest import RecyclingProxyRequest


class AlipayCommerceEcRecyclinginvoiceFarmerCreateModel(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._cert_no = None
        self._farmer_item_list = None
        self._farmer_name = None
        self._farmer_type_list = None
        self._is_family_master = None
        self._recycling_proxy = None

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
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def farmer_item_list(self):
        return self._farmer_item_list

    @farmer_item_list.setter
    def farmer_item_list(self, value):
        if isinstance(value, list):
            self._farmer_item_list = list()
            for i in value:
                if isinstance(i, RecyclingFarmerItemRequest):
                    self._farmer_item_list.append(i)
                else:
                    self._farmer_item_list.append(RecyclingFarmerItemRequest.from_alipay_dict(i))
    @property
    def farmer_name(self):
        return self._farmer_name

    @farmer_name.setter
    def farmer_name(self, value):
        self._farmer_name = value
    @property
    def farmer_type_list(self):
        return self._farmer_type_list

    @farmer_type_list.setter
    def farmer_type_list(self, value):
        if isinstance(value, list):
            self._farmer_type_list = list()
            for i in value:
                self._farmer_type_list.append(i)
    @property
    def is_family_master(self):
        return self._is_family_master

    @is_family_master.setter
    def is_family_master(self, value):
        self._is_family_master = value
    @property
    def recycling_proxy(self):
        return self._recycling_proxy

    @recycling_proxy.setter
    def recycling_proxy(self, value):
        if isinstance(value, RecyclingProxyRequest):
            self._recycling_proxy = value
        else:
            self._recycling_proxy = RecyclingProxyRequest.from_alipay_dict(value)


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
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.farmer_item_list:
            if isinstance(self.farmer_item_list, list):
                for i in range(0, len(self.farmer_item_list)):
                    element = self.farmer_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.farmer_item_list[i] = element.to_alipay_dict()
            if hasattr(self.farmer_item_list, 'to_alipay_dict'):
                params['farmer_item_list'] = self.farmer_item_list.to_alipay_dict()
            else:
                params['farmer_item_list'] = self.farmer_item_list
        if self.farmer_name:
            if hasattr(self.farmer_name, 'to_alipay_dict'):
                params['farmer_name'] = self.farmer_name.to_alipay_dict()
            else:
                params['farmer_name'] = self.farmer_name
        if self.farmer_type_list:
            if isinstance(self.farmer_type_list, list):
                for i in range(0, len(self.farmer_type_list)):
                    element = self.farmer_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.farmer_type_list[i] = element.to_alipay_dict()
            if hasattr(self.farmer_type_list, 'to_alipay_dict'):
                params['farmer_type_list'] = self.farmer_type_list.to_alipay_dict()
            else:
                params['farmer_type_list'] = self.farmer_type_list
        if self.is_family_master:
            if hasattr(self.is_family_master, 'to_alipay_dict'):
                params['is_family_master'] = self.is_family_master.to_alipay_dict()
            else:
                params['is_family_master'] = self.is_family_master
        if self.recycling_proxy:
            if hasattr(self.recycling_proxy, 'to_alipay_dict'):
                params['recycling_proxy'] = self.recycling_proxy.to_alipay_dict()
            else:
                params['recycling_proxy'] = self.recycling_proxy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerCreateModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'farmer_item_list' in d:
            o.farmer_item_list = d['farmer_item_list']
        if 'farmer_name' in d:
            o.farmer_name = d['farmer_name']
        if 'farmer_type_list' in d:
            o.farmer_type_list = d['farmer_type_list']
        if 'is_family_master' in d:
            o.is_family_master = d['is_family_master']
        if 'recycling_proxy' in d:
            o.recycling_proxy = d['recycling_proxy']
        return o


