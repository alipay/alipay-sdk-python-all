#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalUserHomedoctorSyncModel(object):

    def __init__(self):
        self._aq_open_id = None
        self._doctor_cert_no = None
        self._doctor_cert_no_encrypt = None
        self._doctor_group = None
        self._doctor_id = None
        self._doctor_organization = None
        self._doctor_organization_id = None
        self._doctor_real_name = None
        self._doctor_real_name_encrypt = None
        self._encrypt_type = None
        self._sign_biz_id = None
        self._sign_biz_type = None
        self._sign_end_date = None
        self._sign_start_date = None
        self._source = None
        self._status = None
        self._user_cert_no = None
        self._user_cert_no_encrypt = None
        self._user_real_name = None
        self._user_real_name_encrypt = None

    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def doctor_cert_no(self):
        return self._doctor_cert_no

    @doctor_cert_no.setter
    def doctor_cert_no(self, value):
        self._doctor_cert_no = value
    @property
    def doctor_cert_no_encrypt(self):
        return self._doctor_cert_no_encrypt

    @doctor_cert_no_encrypt.setter
    def doctor_cert_no_encrypt(self, value):
        self._doctor_cert_no_encrypt = value
    @property
    def doctor_group(self):
        return self._doctor_group

    @doctor_group.setter
    def doctor_group(self, value):
        self._doctor_group = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_organization(self):
        return self._doctor_organization

    @doctor_organization.setter
    def doctor_organization(self, value):
        self._doctor_organization = value
    @property
    def doctor_organization_id(self):
        return self._doctor_organization_id

    @doctor_organization_id.setter
    def doctor_organization_id(self, value):
        self._doctor_organization_id = value
    @property
    def doctor_real_name(self):
        return self._doctor_real_name

    @doctor_real_name.setter
    def doctor_real_name(self, value):
        self._doctor_real_name = value
    @property
    def doctor_real_name_encrypt(self):
        return self._doctor_real_name_encrypt

    @doctor_real_name_encrypt.setter
    def doctor_real_name_encrypt(self, value):
        self._doctor_real_name_encrypt = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def sign_biz_id(self):
        return self._sign_biz_id

    @sign_biz_id.setter
    def sign_biz_id(self, value):
        self._sign_biz_id = value
    @property
    def sign_biz_type(self):
        return self._sign_biz_type

    @sign_biz_type.setter
    def sign_biz_type(self, value):
        self._sign_biz_type = value
    @property
    def sign_end_date(self):
        return self._sign_end_date

    @sign_end_date.setter
    def sign_end_date(self, value):
        self._sign_end_date = value
    @property
    def sign_start_date(self):
        return self._sign_start_date

    @sign_start_date.setter
    def sign_start_date(self, value):
        self._sign_start_date = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_no_encrypt(self):
        return self._user_cert_no_encrypt

    @user_cert_no_encrypt.setter
    def user_cert_no_encrypt(self, value):
        self._user_cert_no_encrypt = value
    @property
    def user_real_name(self):
        return self._user_real_name

    @user_real_name.setter
    def user_real_name(self, value):
        self._user_real_name = value
    @property
    def user_real_name_encrypt(self):
        return self._user_real_name_encrypt

    @user_real_name_encrypt.setter
    def user_real_name_encrypt(self, value):
        self._user_real_name_encrypt = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        if self.doctor_cert_no:
            if hasattr(self.doctor_cert_no, 'to_alipay_dict'):
                params['doctor_cert_no'] = self.doctor_cert_no.to_alipay_dict()
            else:
                params['doctor_cert_no'] = self.doctor_cert_no
        if self.doctor_cert_no_encrypt:
            if hasattr(self.doctor_cert_no_encrypt, 'to_alipay_dict'):
                params['doctor_cert_no_encrypt'] = self.doctor_cert_no_encrypt.to_alipay_dict()
            else:
                params['doctor_cert_no_encrypt'] = self.doctor_cert_no_encrypt
        if self.doctor_group:
            if hasattr(self.doctor_group, 'to_alipay_dict'):
                params['doctor_group'] = self.doctor_group.to_alipay_dict()
            else:
                params['doctor_group'] = self.doctor_group
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_organization:
            if hasattr(self.doctor_organization, 'to_alipay_dict'):
                params['doctor_organization'] = self.doctor_organization.to_alipay_dict()
            else:
                params['doctor_organization'] = self.doctor_organization
        if self.doctor_organization_id:
            if hasattr(self.doctor_organization_id, 'to_alipay_dict'):
                params['doctor_organization_id'] = self.doctor_organization_id.to_alipay_dict()
            else:
                params['doctor_organization_id'] = self.doctor_organization_id
        if self.doctor_real_name:
            if hasattr(self.doctor_real_name, 'to_alipay_dict'):
                params['doctor_real_name'] = self.doctor_real_name.to_alipay_dict()
            else:
                params['doctor_real_name'] = self.doctor_real_name
        if self.doctor_real_name_encrypt:
            if hasattr(self.doctor_real_name_encrypt, 'to_alipay_dict'):
                params['doctor_real_name_encrypt'] = self.doctor_real_name_encrypt.to_alipay_dict()
            else:
                params['doctor_real_name_encrypt'] = self.doctor_real_name_encrypt
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.sign_biz_id:
            if hasattr(self.sign_biz_id, 'to_alipay_dict'):
                params['sign_biz_id'] = self.sign_biz_id.to_alipay_dict()
            else:
                params['sign_biz_id'] = self.sign_biz_id
        if self.sign_biz_type:
            if hasattr(self.sign_biz_type, 'to_alipay_dict'):
                params['sign_biz_type'] = self.sign_biz_type.to_alipay_dict()
            else:
                params['sign_biz_type'] = self.sign_biz_type
        if self.sign_end_date:
            if hasattr(self.sign_end_date, 'to_alipay_dict'):
                params['sign_end_date'] = self.sign_end_date.to_alipay_dict()
            else:
                params['sign_end_date'] = self.sign_end_date
        if self.sign_start_date:
            if hasattr(self.sign_start_date, 'to_alipay_dict'):
                params['sign_start_date'] = self.sign_start_date.to_alipay_dict()
            else:
                params['sign_start_date'] = self.sign_start_date
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_cert_no_encrypt:
            if hasattr(self.user_cert_no_encrypt, 'to_alipay_dict'):
                params['user_cert_no_encrypt'] = self.user_cert_no_encrypt.to_alipay_dict()
            else:
                params['user_cert_no_encrypt'] = self.user_cert_no_encrypt
        if self.user_real_name:
            if hasattr(self.user_real_name, 'to_alipay_dict'):
                params['user_real_name'] = self.user_real_name.to_alipay_dict()
            else:
                params['user_real_name'] = self.user_real_name
        if self.user_real_name_encrypt:
            if hasattr(self.user_real_name_encrypt, 'to_alipay_dict'):
                params['user_real_name_encrypt'] = self.user_real_name_encrypt.to_alipay_dict()
            else:
                params['user_real_name_encrypt'] = self.user_real_name_encrypt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalUserHomedoctorSyncModel()
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        if 'doctor_cert_no' in d:
            o.doctor_cert_no = d['doctor_cert_no']
        if 'doctor_cert_no_encrypt' in d:
            o.doctor_cert_no_encrypt = d['doctor_cert_no_encrypt']
        if 'doctor_group' in d:
            o.doctor_group = d['doctor_group']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_organization' in d:
            o.doctor_organization = d['doctor_organization']
        if 'doctor_organization_id' in d:
            o.doctor_organization_id = d['doctor_organization_id']
        if 'doctor_real_name' in d:
            o.doctor_real_name = d['doctor_real_name']
        if 'doctor_real_name_encrypt' in d:
            o.doctor_real_name_encrypt = d['doctor_real_name_encrypt']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'sign_biz_id' in d:
            o.sign_biz_id = d['sign_biz_id']
        if 'sign_biz_type' in d:
            o.sign_biz_type = d['sign_biz_type']
        if 'sign_end_date' in d:
            o.sign_end_date = d['sign_end_date']
        if 'sign_start_date' in d:
            o.sign_start_date = d['sign_start_date']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_cert_no_encrypt' in d:
            o.user_cert_no_encrypt = d['user_cert_no_encrypt']
        if 'user_real_name' in d:
            o.user_real_name = d['user_real_name']
        if 'user_real_name_encrypt' in d:
            o.user_real_name_encrypt = d['user_real_name_encrypt']
        return o


