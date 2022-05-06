#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdBaseInfoDTO import CrowdBaseInfoDTO


class DatadigitalFincloudFinsaasCrowdOdpsCreateModel(object):

    def __init__(self):
        self._crowd_base_info_dto = None
        self._operator_id = None
        self._operator_name = None
        self._organization = None
        self._tenant_code = None

    @property
    def crowd_base_info_dto(self):
        return self._crowd_base_info_dto

    @crowd_base_info_dto.setter
    def crowd_base_info_dto(self, value):
        if isinstance(value, CrowdBaseInfoDTO):
            self._crowd_base_info_dto = value
        else:
            self._crowd_base_info_dto = CrowdBaseInfoDTO.from_alipay_dict(value)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_base_info_dto:
            if hasattr(self.crowd_base_info_dto, 'to_alipay_dict'):
                params['crowd_base_info_dto'] = self.crowd_base_info_dto.to_alipay_dict()
            else:
                params['crowd_base_info_dto'] = self.crowd_base_info_dto
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.organization:
            if hasattr(self.organization, 'to_alipay_dict'):
                params['organization'] = self.organization.to_alipay_dict()
            else:
                params['organization'] = self.organization
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasCrowdOdpsCreateModel()
        if 'crowd_base_info_dto' in d:
            o.crowd_base_info_dto = d['crowd_base_info_dto']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'organization' in d:
            o.organization = d['organization']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


