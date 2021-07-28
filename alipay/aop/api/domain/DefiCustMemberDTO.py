#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DefiCustMemberDTO(object):

    def __init__(self):
        self._auth_status = None
        self._company_cert_no = None
        self._company_cert_type = None
        self._company_name = None
        self._id_map = None
        self._member_email = None
        self._member_id = None
        self._role_types = None
        self._status = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_cert_type(self):
        return self._company_cert_type

    @company_cert_type.setter
    def company_cert_type(self, value):
        self._company_cert_type = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def id_map(self):
        return self._id_map

    @id_map.setter
    def id_map(self, value):
        self._id_map = value
    @property
    def member_email(self):
        return self._member_email

    @member_email.setter
    def member_email(self, value):
        self._member_email = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_cert_type:
            if hasattr(self.company_cert_type, 'to_alipay_dict'):
                params['company_cert_type'] = self.company_cert_type.to_alipay_dict()
            else:
                params['company_cert_type'] = self.company_cert_type
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.id_map:
            if hasattr(self.id_map, 'to_alipay_dict'):
                params['id_map'] = self.id_map.to_alipay_dict()
            else:
                params['id_map'] = self.id_map
        if self.member_email:
            if hasattr(self.member_email, 'to_alipay_dict'):
                params['member_email'] = self.member_email.to_alipay_dict()
            else:
                params['member_email'] = self.member_email
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DefiCustMemberDTO()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_cert_type' in d:
            o.company_cert_type = d['company_cert_type']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'id_map' in d:
            o.id_map = d['id_map']
        if 'member_email' in d:
            o.member_email = d['member_email']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'role_types' in d:
            o.role_types = d['role_types']
        if 'status' in d:
            o.status = d['status']
        return o


