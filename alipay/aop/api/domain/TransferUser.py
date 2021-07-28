#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferCredential import TransferCredential
from alipay.aop.api.domain.TransferAddressInfo import TransferAddressInfo
from alipay.aop.api.domain.TransferUserName import TransferUserName


class TransferUser(object):

    def __init__(self):
        self._birth_date = None
        self._credential = None
        self._nationality = None
        self._user_address = None
        self._user_email = None
        self._user_id = None
        self._user_name = None
        self._user_phone_no = None

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def credential(self):
        return self._credential

    @credential.setter
    def credential(self, value):
        if isinstance(value, TransferCredential):
            self._credential = value
        else:
            self._credential = TransferCredential.from_alipay_dict(value)
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        if isinstance(value, TransferAddressInfo):
            self._user_address = value
        else:
            self._user_address = TransferAddressInfo.from_alipay_dict(value)
    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if isinstance(value, TransferUserName):
            self._user_name = value
        else:
            self._user_name = TransferUserName.from_alipay_dict(value)
    @property
    def user_phone_no(self):
        return self._user_phone_no

    @user_phone_no.setter
    def user_phone_no(self, value):
        self._user_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.credential:
            if hasattr(self.credential, 'to_alipay_dict'):
                params['credential'] = self.credential.to_alipay_dict()
            else:
                params['credential'] = self.credential
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.user_address:
            if hasattr(self.user_address, 'to_alipay_dict'):
                params['user_address'] = self.user_address.to_alipay_dict()
            else:
                params['user_address'] = self.user_address
        if self.user_email:
            if hasattr(self.user_email, 'to_alipay_dict'):
                params['user_email'] = self.user_email.to_alipay_dict()
            else:
                params['user_email'] = self.user_email
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone_no:
            if hasattr(self.user_phone_no, 'to_alipay_dict'):
                params['user_phone_no'] = self.user_phone_no.to_alipay_dict()
            else:
                params['user_phone_no'] = self.user_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferUser()
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'credential' in d:
            o.credential = d['credential']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'user_address' in d:
            o.user_address = d['user_address']
        if 'user_email' in d:
            o.user_email = d['user_email']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone_no' in d:
            o.user_phone_no = d['user_phone_no']
        return o


