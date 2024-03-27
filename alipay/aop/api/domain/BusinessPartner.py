#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationAddress import OperationAddress


class BusinessPartner(object):

    def __init__(self):
        self._business_local_name = None
        self._business_name = None
        self._logo = None
        self._logo_type = None
        self._mcc = None
        self._operation_address = None

    @property
    def business_local_name(self):
        return self._business_local_name

    @business_local_name.setter
    def business_local_name(self, value):
        self._business_local_name = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def logo_type(self):
        return self._logo_type

    @logo_type.setter
    def logo_type(self, value):
        self._logo_type = value
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def operation_address(self):
        return self._operation_address

    @operation_address.setter
    def operation_address(self, value):
        if isinstance(value, OperationAddress):
            self._operation_address = value
        else:
            self._operation_address = OperationAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.business_local_name:
            if hasattr(self.business_local_name, 'to_alipay_dict'):
                params['business_local_name'] = self.business_local_name.to_alipay_dict()
            else:
                params['business_local_name'] = self.business_local_name
        if self.business_name:
            if hasattr(self.business_name, 'to_alipay_dict'):
                params['business_name'] = self.business_name.to_alipay_dict()
            else:
                params['business_name'] = self.business_name
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.logo_type:
            if hasattr(self.logo_type, 'to_alipay_dict'):
                params['logo_type'] = self.logo_type.to_alipay_dict()
            else:
                params['logo_type'] = self.logo_type
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.operation_address:
            if hasattr(self.operation_address, 'to_alipay_dict'):
                params['operation_address'] = self.operation_address.to_alipay_dict()
            else:
                params['operation_address'] = self.operation_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessPartner()
        if 'business_local_name' in d:
            o.business_local_name = d['business_local_name']
        if 'business_name' in d:
            o.business_name = d['business_name']
        if 'logo' in d:
            o.logo = d['logo']
        if 'logo_type' in d:
            o.logo_type = d['logo_type']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'operation_address' in d:
            o.operation_address = d['operation_address']
        return o


