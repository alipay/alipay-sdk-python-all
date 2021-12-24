#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiMatterMemberDTO(object):

    def __init__(self):
        self._matter_code = None
        self._matter_type = None
        self._member_id = None
        self._member_role_enum = None
        self._name = None
        self._nick_name = None
        self._sub_matter_type = None
        self._tenant = None

    @property
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value
    @property
    def matter_type(self):
        return self._matter_type

    @matter_type.setter
    def matter_type(self, value):
        self._matter_type = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_role_enum(self):
        return self._member_role_enum

    @member_role_enum.setter
    def member_role_enum(self, value):
        self._member_role_enum = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def sub_matter_type(self):
        return self._sub_matter_type

    @sub_matter_type.setter
    def sub_matter_type(self, value):
        self._sub_matter_type = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        if self.matter_type:
            if hasattr(self.matter_type, 'to_alipay_dict'):
                params['matter_type'] = self.matter_type.to_alipay_dict()
            else:
                params['matter_type'] = self.matter_type
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.member_role_enum:
            if hasattr(self.member_role_enum, 'to_alipay_dict'):
                params['member_role_enum'] = self.member_role_enum.to_alipay_dict()
            else:
                params['member_role_enum'] = self.member_role_enum
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.sub_matter_type:
            if hasattr(self.sub_matter_type, 'to_alipay_dict'):
                params['sub_matter_type'] = self.sub_matter_type.to_alipay_dict()
            else:
                params['sub_matter_type'] = self.sub_matter_type
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiMatterMemberDTO()
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        if 'matter_type' in d:
            o.matter_type = d['matter_type']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'member_role_enum' in d:
            o.member_role_enum = d['member_role_enum']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'sub_matter_type' in d:
            o.sub_matter_type = d['sub_matter_type']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


