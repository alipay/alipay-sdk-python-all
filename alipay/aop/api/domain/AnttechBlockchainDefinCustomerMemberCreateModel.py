#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DefiCustCompanyDTO import DefiCustCompanyDTO


class AnttechBlockchainDefinCustomerMemberCreateModel(object):

    def __init__(self):
        self._auth_type = None
        self._biz_product = None
        self._company_info = None
        self._did = None
        self._member_type = None
        self._role_types = None
        self._tenant_id = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, value):
        if isinstance(value, DefiCustCompanyDTO):
            self._company_info = value
        else:
            self._company_info = DefiCustCompanyDTO.from_alipay_dict(value)
    @property
    def did(self):
        return self._did

    @did.setter
    def did(self, value):
        self._did = value
    @property
    def member_type(self):
        return self._member_type

    @member_type.setter
    def member_type(self, value):
        self._member_type = value
    @property
    def role_types(self):
        return self._role_types

    @role_types.setter
    def role_types(self, value):
        if isinstance(value, list):
            self._role_types = list()
            for i in value:
                self._role_types.append(i)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.company_info:
            if hasattr(self.company_info, 'to_alipay_dict'):
                params['company_info'] = self.company_info.to_alipay_dict()
            else:
                params['company_info'] = self.company_info
        if self.did:
            if hasattr(self.did, 'to_alipay_dict'):
                params['did'] = self.did.to_alipay_dict()
            else:
                params['did'] = self.did
        if self.member_type:
            if hasattr(self.member_type, 'to_alipay_dict'):
                params['member_type'] = self.member_type.to_alipay_dict()
            else:
                params['member_type'] = self.member_type
        if self.role_types:
            if isinstance(self.role_types, list):
                for i in range(0, len(self.role_types)):
                    element = self.role_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_types[i] = element.to_alipay_dict()
            if hasattr(self.role_types, 'to_alipay_dict'):
                params['role_types'] = self.role_types.to_alipay_dict()
            else:
                params['role_types'] = self.role_types
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerMemberCreateModel()
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'company_info' in d:
            o.company_info = d['company_info']
        if 'did' in d:
            o.did = d['did']
        if 'member_type' in d:
            o.member_type = d['member_type']
        if 'role_types' in d:
            o.role_types = d['role_types']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


