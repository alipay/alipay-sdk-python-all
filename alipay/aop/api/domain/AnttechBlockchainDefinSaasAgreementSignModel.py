#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasAgreementSignModel(object):

    def __init__(self):
        self._entity_type = None
        self._legal_person_cert_no = None
        self._legal_person_name = None
        self._name = None
        self._out_member_id = None
        self._platform_member_id = None
        self._unified_social_credit_code = None

    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_member_id = value
        else:
            self._out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasAgreementSignModel()
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'name' in d:
            o.name = d['name']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        return o


