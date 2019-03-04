#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationPartnerSettleSignModel(object):

    def __init__(self):
        self._address = None
        self._channel_id = None
        self._city_code = None
        self._company_name = None
        self._contact_email = None
        self._contact_name = None
        self._contact_phone = None
        self._district_code = None
        self._province_code = None
        self._remark = None
        self._roles = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        if isinstance(value, list):
            self._roles = list()
            for i in value:
                self._roles.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.roles:
            if isinstance(self.roles, list):
                for i in range(0, len(self.roles)):
                    element = self.roles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.roles[i] = element.to_alipay_dict()
            if hasattr(self.roles, 'to_alipay_dict'):
                params['roles'] = self.roles.to_alipay_dict()
            else:
                params['roles'] = self.roles
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationPartnerSettleSignModel()
        if 'address' in d:
            o.address = d['address']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'roles' in d:
            o.roles = d['roles']
        return o


