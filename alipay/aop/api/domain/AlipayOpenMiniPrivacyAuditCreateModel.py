#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SystemPrivacyField import SystemPrivacyField
from alipay.aop.api.domain.UserDefinePrivacyPolicyField import UserDefinePrivacyPolicyField


class AlipayOpenMiniPrivacyAuditCreateModel(object):

    def __init__(self):
        self._contact_email = None
        self._contact_phone = None
        self._public_type = None
        self._reply_cycle = None
        self._storage_location = None
        self._system_privacy_fields = None
        self._user_define_privacy_fields = None

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def public_type(self):
        return self._public_type

    @public_type.setter
    def public_type(self, value):
        self._public_type = value
    @property
    def reply_cycle(self):
        return self._reply_cycle

    @reply_cycle.setter
    def reply_cycle(self, value):
        self._reply_cycle = value
    @property
    def storage_location(self):
        return self._storage_location

    @storage_location.setter
    def storage_location(self, value):
        self._storage_location = value
    @property
    def system_privacy_fields(self):
        return self._system_privacy_fields

    @system_privacy_fields.setter
    def system_privacy_fields(self, value):
        if isinstance(value, list):
            self._system_privacy_fields = list()
            for i in value:
                if isinstance(i, SystemPrivacyField):
                    self._system_privacy_fields.append(i)
                else:
                    self._system_privacy_fields.append(SystemPrivacyField.from_alipay_dict(i))
    @property
    def user_define_privacy_fields(self):
        return self._user_define_privacy_fields

    @user_define_privacy_fields.setter
    def user_define_privacy_fields(self, value):
        if isinstance(value, list):
            self._user_define_privacy_fields = list()
            for i in value:
                if isinstance(i, UserDefinePrivacyPolicyField):
                    self._user_define_privacy_fields.append(i)
                else:
                    self._user_define_privacy_fields.append(UserDefinePrivacyPolicyField.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.public_type:
            if hasattr(self.public_type, 'to_alipay_dict'):
                params['public_type'] = self.public_type.to_alipay_dict()
            else:
                params['public_type'] = self.public_type
        if self.reply_cycle:
            if hasattr(self.reply_cycle, 'to_alipay_dict'):
                params['reply_cycle'] = self.reply_cycle.to_alipay_dict()
            else:
                params['reply_cycle'] = self.reply_cycle
        if self.storage_location:
            if hasattr(self.storage_location, 'to_alipay_dict'):
                params['storage_location'] = self.storage_location.to_alipay_dict()
            else:
                params['storage_location'] = self.storage_location
        if self.system_privacy_fields:
            if isinstance(self.system_privacy_fields, list):
                for i in range(0, len(self.system_privacy_fields)):
                    element = self.system_privacy_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.system_privacy_fields[i] = element.to_alipay_dict()
            if hasattr(self.system_privacy_fields, 'to_alipay_dict'):
                params['system_privacy_fields'] = self.system_privacy_fields.to_alipay_dict()
            else:
                params['system_privacy_fields'] = self.system_privacy_fields
        if self.user_define_privacy_fields:
            if isinstance(self.user_define_privacy_fields, list):
                for i in range(0, len(self.user_define_privacy_fields)):
                    element = self.user_define_privacy_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_define_privacy_fields[i] = element.to_alipay_dict()
            if hasattr(self.user_define_privacy_fields, 'to_alipay_dict'):
                params['user_define_privacy_fields'] = self.user_define_privacy_fields.to_alipay_dict()
            else:
                params['user_define_privacy_fields'] = self.user_define_privacy_fields
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPrivacyAuditCreateModel()
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'public_type' in d:
            o.public_type = d['public_type']
        if 'reply_cycle' in d:
            o.reply_cycle = d['reply_cycle']
        if 'storage_location' in d:
            o.storage_location = d['storage_location']
        if 'system_privacy_fields' in d:
            o.system_privacy_fields = d['system_privacy_fields']
        if 'user_define_privacy_fields' in d:
            o.user_define_privacy_fields = d['user_define_privacy_fields']
        return o


