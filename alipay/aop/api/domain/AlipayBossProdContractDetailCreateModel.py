#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiContractFileSaDTO import OpenApiContractFileSaDTO
from alipay.aop.api.domain.OpenApiContractFileSaDTO import OpenApiContractFileSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiPartnerSaDTO import OpenApiPartnerSaDTO
from alipay.aop.api.domain.OpenApiPartnerSaDTO import OpenApiPartnerSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO


class AlipayBossProdContractDetailCreateModel(object):

    def __init__(self):
        self._applicant = None
        self._attach_files = None
        self._business = None
        self._business_scene = None
        self._contract_desc = None
        self._contract_files = None
        self._contract_name = None
        self._detail_url = None
        self._finance_people = None
        self._legal_people = None
        self._negotiators = None
        self._opposite_parts = None
        self._our_parts = None
        self._owners = None
        self._source_system_id = None
        self._tenant = None
        self._voucher_id = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._applicant = value
        else:
            self._applicant = OpenApiPersonSaDTO.from_alipay_dict(value)
    @property
    def attach_files(self):
        return self._attach_files

    @attach_files.setter
    def attach_files(self, value):
        if isinstance(value, list):
            self._attach_files = list()
            for i in value:
                if isinstance(i, OpenApiContractFileSaDTO):
                    self._attach_files.append(i)
                else:
                    self._attach_files.append(OpenApiContractFileSaDTO.from_alipay_dict(i))
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def contract_desc(self):
        return self._contract_desc

    @contract_desc.setter
    def contract_desc(self, value):
        self._contract_desc = value
    @property
    def contract_files(self):
        return self._contract_files

    @contract_files.setter
    def contract_files(self, value):
        if isinstance(value, list):
            self._contract_files = list()
            for i in value:
                if isinstance(i, OpenApiContractFileSaDTO):
                    self._contract_files.append(i)
                else:
                    self._contract_files.append(OpenApiContractFileSaDTO.from_alipay_dict(i))
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def finance_people(self):
        return self._finance_people

    @finance_people.setter
    def finance_people(self, value):
        if isinstance(value, list):
            self._finance_people = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._finance_people.append(i)
                else:
                    self._finance_people.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def legal_people(self):
        return self._legal_people

    @legal_people.setter
    def legal_people(self, value):
        if isinstance(value, list):
            self._legal_people = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._legal_people.append(i)
                else:
                    self._legal_people.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def negotiators(self):
        return self._negotiators

    @negotiators.setter
    def negotiators(self, value):
        if isinstance(value, list):
            self._negotiators = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._negotiators.append(i)
                else:
                    self._negotiators.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def opposite_parts(self):
        return self._opposite_parts

    @opposite_parts.setter
    def opposite_parts(self, value):
        if isinstance(value, list):
            self._opposite_parts = list()
            for i in value:
                if isinstance(i, OpenApiPartnerSaDTO):
                    self._opposite_parts.append(i)
                else:
                    self._opposite_parts.append(OpenApiPartnerSaDTO.from_alipay_dict(i))
    @property
    def our_parts(self):
        return self._our_parts

    @our_parts.setter
    def our_parts(self, value):
        if isinstance(value, list):
            self._our_parts = list()
            for i in value:
                if isinstance(i, OpenApiPartnerSaDTO):
                    self._our_parts.append(i)
                else:
                    self._our_parts.append(OpenApiPartnerSaDTO.from_alipay_dict(i))
    @property
    def owners(self):
        return self._owners

    @owners.setter
    def owners(self, value):
        if isinstance(value, list):
            self._owners = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._owners.append(i)
                else:
                    self._owners.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.attach_files:
            if isinstance(self.attach_files, list):
                for i in range(0, len(self.attach_files)):
                    element = self.attach_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attach_files[i] = element.to_alipay_dict()
            if hasattr(self.attach_files, 'to_alipay_dict'):
                params['attach_files'] = self.attach_files.to_alipay_dict()
            else:
                params['attach_files'] = self.attach_files
        if self.business:
            if hasattr(self.business, 'to_alipay_dict'):
                params['business'] = self.business.to_alipay_dict()
            else:
                params['business'] = self.business
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.contract_desc:
            if hasattr(self.contract_desc, 'to_alipay_dict'):
                params['contract_desc'] = self.contract_desc.to_alipay_dict()
            else:
                params['contract_desc'] = self.contract_desc
        if self.contract_files:
            if isinstance(self.contract_files, list):
                for i in range(0, len(self.contract_files)):
                    element = self.contract_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_files[i] = element.to_alipay_dict()
            if hasattr(self.contract_files, 'to_alipay_dict'):
                params['contract_files'] = self.contract_files.to_alipay_dict()
            else:
                params['contract_files'] = self.contract_files
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.finance_people:
            if isinstance(self.finance_people, list):
                for i in range(0, len(self.finance_people)):
                    element = self.finance_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.finance_people[i] = element.to_alipay_dict()
            if hasattr(self.finance_people, 'to_alipay_dict'):
                params['finance_people'] = self.finance_people.to_alipay_dict()
            else:
                params['finance_people'] = self.finance_people
        if self.legal_people:
            if isinstance(self.legal_people, list):
                for i in range(0, len(self.legal_people)):
                    element = self.legal_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_people[i] = element.to_alipay_dict()
            if hasattr(self.legal_people, 'to_alipay_dict'):
                params['legal_people'] = self.legal_people.to_alipay_dict()
            else:
                params['legal_people'] = self.legal_people
        if self.negotiators:
            if isinstance(self.negotiators, list):
                for i in range(0, len(self.negotiators)):
                    element = self.negotiators[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.negotiators[i] = element.to_alipay_dict()
            if hasattr(self.negotiators, 'to_alipay_dict'):
                params['negotiators'] = self.negotiators.to_alipay_dict()
            else:
                params['negotiators'] = self.negotiators
        if self.opposite_parts:
            if isinstance(self.opposite_parts, list):
                for i in range(0, len(self.opposite_parts)):
                    element = self.opposite_parts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.opposite_parts[i] = element.to_alipay_dict()
            if hasattr(self.opposite_parts, 'to_alipay_dict'):
                params['opposite_parts'] = self.opposite_parts.to_alipay_dict()
            else:
                params['opposite_parts'] = self.opposite_parts
        if self.our_parts:
            if isinstance(self.our_parts, list):
                for i in range(0, len(self.our_parts)):
                    element = self.our_parts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.our_parts[i] = element.to_alipay_dict()
            if hasattr(self.our_parts, 'to_alipay_dict'):
                params['our_parts'] = self.our_parts.to_alipay_dict()
            else:
                params['our_parts'] = self.our_parts
        if self.owners:
            if isinstance(self.owners, list):
                for i in range(0, len(self.owners)):
                    element = self.owners[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.owners[i] = element.to_alipay_dict()
            if hasattr(self.owners, 'to_alipay_dict'):
                params['owners'] = self.owners.to_alipay_dict()
            else:
                params['owners'] = self.owners
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdContractDetailCreateModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'attach_files' in d:
            o.attach_files = d['attach_files']
        if 'business' in d:
            o.business = d['business']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'contract_desc' in d:
            o.contract_desc = d['contract_desc']
        if 'contract_files' in d:
            o.contract_files = d['contract_files']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'finance_people' in d:
            o.finance_people = d['finance_people']
        if 'legal_people' in d:
            o.legal_people = d['legal_people']
        if 'negotiators' in d:
            o.negotiators = d['negotiators']
        if 'opposite_parts' in d:
            o.opposite_parts = d['opposite_parts']
        if 'our_parts' in d:
            o.our_parts = d['our_parts']
        if 'owners' in d:
            o.owners = d['owners']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


