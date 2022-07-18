#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdentityDTO import IdentityDTO
from alipay.aop.api.domain.IdentityDTO import IdentityDTO
from alipay.aop.api.domain.LocationDTO import LocationDTO


class AlipayBossProdAntlegalchainFilenotaryCreateModel(object):

    def __init__(self):
        self._app_code = None
        self._business_line_code = None
        self._business_unique_id = None
        self._customer = None
        self._entity = None
        self._file_id = None
        self._location = None
        self._scene_code = None
        self._submitter_name = None
        self._submitter_uid = None
        self._tenant = None
        self._token_key = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def business_unique_id(self):
        return self._business_unique_id

    @business_unique_id.setter
    def business_unique_id(self, value):
        self._business_unique_id = value
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, IdentityDTO):
            self._customer = value
        else:
            self._customer = IdentityDTO.from_alipay_dict(value)
    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        if isinstance(value, IdentityDTO):
            self._entity = value
        else:
            self._entity = IdentityDTO.from_alipay_dict(value)
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, LocationDTO):
            self._location = value
        else:
            self._location = LocationDTO.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def submitter_name(self):
        return self._submitter_name

    @submitter_name.setter
    def submitter_name(self, value):
        self._submitter_name = value
    @property
    def submitter_uid(self):
        return self._submitter_uid

    @submitter_uid.setter
    def submitter_uid(self, value):
        self._submitter_uid = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def token_key(self):
        return self._token_key

    @token_key.setter
    def token_key(self, value):
        self._token_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
        if self.business_unique_id:
            if hasattr(self.business_unique_id, 'to_alipay_dict'):
                params['business_unique_id'] = self.business_unique_id.to_alipay_dict()
            else:
                params['business_unique_id'] = self.business_unique_id
        if self.customer:
            if hasattr(self.customer, 'to_alipay_dict'):
                params['customer'] = self.customer.to_alipay_dict()
            else:
                params['customer'] = self.customer
        if self.entity:
            if hasattr(self.entity, 'to_alipay_dict'):
                params['entity'] = self.entity.to_alipay_dict()
            else:
                params['entity'] = self.entity
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.submitter_name:
            if hasattr(self.submitter_name, 'to_alipay_dict'):
                params['submitter_name'] = self.submitter_name.to_alipay_dict()
            else:
                params['submitter_name'] = self.submitter_name
        if self.submitter_uid:
            if hasattr(self.submitter_uid, 'to_alipay_dict'):
                params['submitter_uid'] = self.submitter_uid.to_alipay_dict()
            else:
                params['submitter_uid'] = self.submitter_uid
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.token_key:
            if hasattr(self.token_key, 'to_alipay_dict'):
                params['token_key'] = self.token_key.to_alipay_dict()
            else:
                params['token_key'] = self.token_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainFilenotaryCreateModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'business_unique_id' in d:
            o.business_unique_id = d['business_unique_id']
        if 'customer' in d:
            o.customer = d['customer']
        if 'entity' in d:
            o.entity = d['entity']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'location' in d:
            o.location = d['location']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'submitter_name' in d:
            o.submitter_name = d['submitter_name']
        if 'submitter_uid' in d:
            o.submitter_uid = d['submitter_uid']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'token_key' in d:
            o.token_key = d['token_key']
        return o


