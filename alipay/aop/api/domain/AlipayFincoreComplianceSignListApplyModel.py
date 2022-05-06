#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PeopleOpenApiDTO import PeopleOpenApiDTO
from alipay.aop.api.domain.SignApproveOpenApiDTO import SignApproveOpenApiDTO
from alipay.aop.api.domain.SignFileOpenApiDTO import SignFileOpenApiDTO
from alipay.aop.api.domain.SignPartyGroupOpenApiDTO import SignPartyGroupOpenApiDTO
from alipay.aop.api.domain.SignPartyGroupOpenApiDTO import SignPartyGroupOpenApiDTO
from alipay.aop.api.domain.PaperSealExtOpenApiRequest import PaperSealExtOpenApiRequest
from alipay.aop.api.domain.SignFileOpenApiDTO import SignFileOpenApiDTO


class AlipayFincoreComplianceSignListApplyModel(object):

    def __init__(self):
        self._applicant = None
        self._approve_info = None
        self._attachments = None
        self._business_id = None
        self._description = None
        self._effect_date = None
        self._effect_type = None
        self._emp_id = None
        self._end_date = None
        self._end_type = None
        self._is_test = None
        self._name = None
        self._other_sign_groups = None
        self._our_sign_group = None
        self._paper_seal_ext_request = None
        self._seal_order = None
        self._sign_files = None
        self._sign_method = None
        self._source_system_id = None
        self._tenant = None
        self._title = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, PeopleOpenApiDTO):
            self._applicant = value
        else:
            self._applicant = PeopleOpenApiDTO.from_alipay_dict(value)
    @property
    def approve_info(self):
        return self._approve_info

    @approve_info.setter
    def approve_info(self, value):
        if isinstance(value, SignApproveOpenApiDTO):
            self._approve_info = value
        else:
            self._approve_info = SignApproveOpenApiDTO.from_alipay_dict(value)
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, SignFileOpenApiDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(SignFileOpenApiDTO.from_alipay_dict(i))
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def effect_type(self):
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_type(self):
        return self._end_type

    @end_type.setter
    def end_type(self, value):
        self._end_type = value
    @property
    def is_test(self):
        return self._is_test

    @is_test.setter
    def is_test(self, value):
        self._is_test = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def other_sign_groups(self):
        return self._other_sign_groups

    @other_sign_groups.setter
    def other_sign_groups(self, value):
        if isinstance(value, list):
            self._other_sign_groups = list()
            for i in value:
                if isinstance(i, SignPartyGroupOpenApiDTO):
                    self._other_sign_groups.append(i)
                else:
                    self._other_sign_groups.append(SignPartyGroupOpenApiDTO.from_alipay_dict(i))
    @property
    def our_sign_group(self):
        return self._our_sign_group

    @our_sign_group.setter
    def our_sign_group(self, value):
        if isinstance(value, SignPartyGroupOpenApiDTO):
            self._our_sign_group = value
        else:
            self._our_sign_group = SignPartyGroupOpenApiDTO.from_alipay_dict(value)
    @property
    def paper_seal_ext_request(self):
        return self._paper_seal_ext_request

    @paper_seal_ext_request.setter
    def paper_seal_ext_request(self, value):
        if isinstance(value, PaperSealExtOpenApiRequest):
            self._paper_seal_ext_request = value
        else:
            self._paper_seal_ext_request = PaperSealExtOpenApiRequest.from_alipay_dict(value)
    @property
    def seal_order(self):
        return self._seal_order

    @seal_order.setter
    def seal_order(self, value):
        self._seal_order = value
    @property
    def sign_files(self):
        return self._sign_files

    @sign_files.setter
    def sign_files(self, value):
        if isinstance(value, list):
            self._sign_files = list()
            for i in value:
                if isinstance(i, SignFileOpenApiDTO):
                    self._sign_files.append(i)
                else:
                    self._sign_files.append(SignFileOpenApiDTO.from_alipay_dict(i))
    @property
    def sign_method(self):
        return self._sign_method

    @sign_method.setter
    def sign_method(self, value):
        self._sign_method = value
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.approve_info:
            if hasattr(self.approve_info, 'to_alipay_dict'):
                params['approve_info'] = self.approve_info.to_alipay_dict()
            else:
                params['approve_info'] = self.approve_info
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.effect_type:
            if hasattr(self.effect_type, 'to_alipay_dict'):
                params['effect_type'] = self.effect_type.to_alipay_dict()
            else:
                params['effect_type'] = self.effect_type
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_type:
            if hasattr(self.end_type, 'to_alipay_dict'):
                params['end_type'] = self.end_type.to_alipay_dict()
            else:
                params['end_type'] = self.end_type
        if self.is_test:
            if hasattr(self.is_test, 'to_alipay_dict'):
                params['is_test'] = self.is_test.to_alipay_dict()
            else:
                params['is_test'] = self.is_test
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.other_sign_groups:
            if isinstance(self.other_sign_groups, list):
                for i in range(0, len(self.other_sign_groups)):
                    element = self.other_sign_groups[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_sign_groups[i] = element.to_alipay_dict()
            if hasattr(self.other_sign_groups, 'to_alipay_dict'):
                params['other_sign_groups'] = self.other_sign_groups.to_alipay_dict()
            else:
                params['other_sign_groups'] = self.other_sign_groups
        if self.our_sign_group:
            if hasattr(self.our_sign_group, 'to_alipay_dict'):
                params['our_sign_group'] = self.our_sign_group.to_alipay_dict()
            else:
                params['our_sign_group'] = self.our_sign_group
        if self.paper_seal_ext_request:
            if hasattr(self.paper_seal_ext_request, 'to_alipay_dict'):
                params['paper_seal_ext_request'] = self.paper_seal_ext_request.to_alipay_dict()
            else:
                params['paper_seal_ext_request'] = self.paper_seal_ext_request
        if self.seal_order:
            if hasattr(self.seal_order, 'to_alipay_dict'):
                params['seal_order'] = self.seal_order.to_alipay_dict()
            else:
                params['seal_order'] = self.seal_order
        if self.sign_files:
            if isinstance(self.sign_files, list):
                for i in range(0, len(self.sign_files)):
                    element = self.sign_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_files[i] = element.to_alipay_dict()
            if hasattr(self.sign_files, 'to_alipay_dict'):
                params['sign_files'] = self.sign_files.to_alipay_dict()
            else:
                params['sign_files'] = self.sign_files
        if self.sign_method:
            if hasattr(self.sign_method, 'to_alipay_dict'):
                params['sign_method'] = self.sign_method.to_alipay_dict()
            else:
                params['sign_method'] = self.sign_method
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
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceSignListApplyModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'approve_info' in d:
            o.approve_info = d['approve_info']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'description' in d:
            o.description = d['description']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'effect_type' in d:
            o.effect_type = d['effect_type']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_type' in d:
            o.end_type = d['end_type']
        if 'is_test' in d:
            o.is_test = d['is_test']
        if 'name' in d:
            o.name = d['name']
        if 'other_sign_groups' in d:
            o.other_sign_groups = d['other_sign_groups']
        if 'our_sign_group' in d:
            o.our_sign_group = d['our_sign_group']
        if 'paper_seal_ext_request' in d:
            o.paper_seal_ext_request = d['paper_seal_ext_request']
        if 'seal_order' in d:
            o.seal_order = d['seal_order']
        if 'sign_files' in d:
            o.sign_files = d['sign_files']
        if 'sign_method' in d:
            o.sign_method = d['sign_method']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'title' in d:
            o.title = d['title']
        return o


