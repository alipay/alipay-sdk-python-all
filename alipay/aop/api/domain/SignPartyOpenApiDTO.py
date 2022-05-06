#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressOpenApiDTO import AddressOpenApiDTO


class SignPartyOpenApiDTO(object):

    def __init__(self):
        self._address = None
        self._alipay_account = None
        self._corp_type = None
        self._email = None
        self._identity_id = None
        self._party_name = None
        self._party_type = None
        self._personal_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, AddressOpenApiDTO):
            self._address = value
        else:
            self._address = AddressOpenApiDTO.from_alipay_dict(value)
    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def corp_type(self):
        return self._corp_type

    @corp_type.setter
    def corp_type(self, value):
        self._corp_type = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def party_name(self):
        return self._party_name

    @party_name.setter
    def party_name(self, value):
        self._party_name = value
    @property
    def party_type(self):
        return self._party_type

    @party_type.setter
    def party_type(self, value):
        self._party_type = value
    @property
    def personal_type(self):
        return self._personal_type

    @personal_type.setter
    def personal_type(self, value):
        self._personal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.corp_type:
            if hasattr(self.corp_type, 'to_alipay_dict'):
                params['corp_type'] = self.corp_type.to_alipay_dict()
            else:
                params['corp_type'] = self.corp_type
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.party_name:
            if hasattr(self.party_name, 'to_alipay_dict'):
                params['party_name'] = self.party_name.to_alipay_dict()
            else:
                params['party_name'] = self.party_name
        if self.party_type:
            if hasattr(self.party_type, 'to_alipay_dict'):
                params['party_type'] = self.party_type.to_alipay_dict()
            else:
                params['party_type'] = self.party_type
        if self.personal_type:
            if hasattr(self.personal_type, 'to_alipay_dict'):
                params['personal_type'] = self.personal_type.to_alipay_dict()
            else:
                params['personal_type'] = self.personal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignPartyOpenApiDTO()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'corp_type' in d:
            o.corp_type = d['corp_type']
        if 'email' in d:
            o.email = d['email']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'party_name' in d:
            o.party_name = d['party_name']
        if 'party_type' in d:
            o.party_type = d['party_type']
        if 'personal_type' in d:
            o.personal_type = d['personal_type']
        return o


