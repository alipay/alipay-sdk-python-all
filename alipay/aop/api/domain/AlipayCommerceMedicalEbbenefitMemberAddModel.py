#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEbbenefitMemberAddModel(object):

    def __init__(self):
        self._address = None
        self._binding_hdf_service = None
        self._city_code = None
        self._eb_user_id = None
        self._member_birthday = None
        self._member_cert_type = None
        self._member_gender = None
        self._member_id = None
        self._member_id_no = None
        self._member_name = None
        self._member_phone_no = None
        self._out_member_id = None
        self._out_user_id = None
        self._rel = None
        self._sync_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def binding_hdf_service(self):
        return self._binding_hdf_service

    @binding_hdf_service.setter
    def binding_hdf_service(self, value):
        self._binding_hdf_service = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def eb_user_id(self):
        return self._eb_user_id

    @eb_user_id.setter
    def eb_user_id(self, value):
        self._eb_user_id = value
    @property
    def member_birthday(self):
        return self._member_birthday

    @member_birthday.setter
    def member_birthday(self, value):
        self._member_birthday = value
    @property
    def member_cert_type(self):
        return self._member_cert_type

    @member_cert_type.setter
    def member_cert_type(self, value):
        self._member_cert_type = value
    @property
    def member_gender(self):
        return self._member_gender

    @member_gender.setter
    def member_gender(self, value):
        self._member_gender = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_id_no(self):
        return self._member_id_no

    @member_id_no.setter
    def member_id_no(self, value):
        self._member_id_no = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def member_phone_no(self):
        return self._member_phone_no

    @member_phone_no.setter
    def member_phone_no(self, value):
        self._member_phone_no = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def rel(self):
        return self._rel

    @rel.setter
    def rel(self, value):
        self._rel = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.binding_hdf_service:
            if hasattr(self.binding_hdf_service, 'to_alipay_dict'):
                params['binding_hdf_service'] = self.binding_hdf_service.to_alipay_dict()
            else:
                params['binding_hdf_service'] = self.binding_hdf_service
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.eb_user_id:
            if hasattr(self.eb_user_id, 'to_alipay_dict'):
                params['eb_user_id'] = self.eb_user_id.to_alipay_dict()
            else:
                params['eb_user_id'] = self.eb_user_id
        if self.member_birthday:
            if hasattr(self.member_birthday, 'to_alipay_dict'):
                params['member_birthday'] = self.member_birthday.to_alipay_dict()
            else:
                params['member_birthday'] = self.member_birthday
        if self.member_cert_type:
            if hasattr(self.member_cert_type, 'to_alipay_dict'):
                params['member_cert_type'] = self.member_cert_type.to_alipay_dict()
            else:
                params['member_cert_type'] = self.member_cert_type
        if self.member_gender:
            if hasattr(self.member_gender, 'to_alipay_dict'):
                params['member_gender'] = self.member_gender.to_alipay_dict()
            else:
                params['member_gender'] = self.member_gender
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.member_id_no:
            if hasattr(self.member_id_no, 'to_alipay_dict'):
                params['member_id_no'] = self.member_id_no.to_alipay_dict()
            else:
                params['member_id_no'] = self.member_id_no
        if self.member_name:
            if hasattr(self.member_name, 'to_alipay_dict'):
                params['member_name'] = self.member_name.to_alipay_dict()
            else:
                params['member_name'] = self.member_name
        if self.member_phone_no:
            if hasattr(self.member_phone_no, 'to_alipay_dict'):
                params['member_phone_no'] = self.member_phone_no.to_alipay_dict()
            else:
                params['member_phone_no'] = self.member_phone_no
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.rel:
            if hasattr(self.rel, 'to_alipay_dict'):
                params['rel'] = self.rel.to_alipay_dict()
            else:
                params['rel'] = self.rel
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEbbenefitMemberAddModel()
        if 'address' in d:
            o.address = d['address']
        if 'binding_hdf_service' in d:
            o.binding_hdf_service = d['binding_hdf_service']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'eb_user_id' in d:
            o.eb_user_id = d['eb_user_id']
        if 'member_birthday' in d:
            o.member_birthday = d['member_birthday']
        if 'member_cert_type' in d:
            o.member_cert_type = d['member_cert_type']
        if 'member_gender' in d:
            o.member_gender = d['member_gender']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'member_id_no' in d:
            o.member_id_no = d['member_id_no']
        if 'member_name' in d:
            o.member_name = d['member_name']
        if 'member_phone_no' in d:
            o.member_phone_no = d['member_phone_no']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'rel' in d:
            o.rel = d['rel']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


