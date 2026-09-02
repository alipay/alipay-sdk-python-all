#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PluginPrivacyFields import PluginPrivacyFields
from alipay.aop.api.domain.SdkPrivacyFields import SdkPrivacyFields
from alipay.aop.api.domain.SystemPermissionPrivacyFields import SystemPermissionPrivacyFields
from alipay.aop.api.domain.SystemPrivacyField import SystemPrivacyField
from alipay.aop.api.domain.UserDefinePrivacyPolicyField import UserDefinePrivacyPolicyField


class AlipayOpenMiniPrivacyOnlineversionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPrivacyOnlineversionQueryResponse, self).__init__()
        self._contact_email = None
        self._contact_phone = None
        self._plugin_privacy_fields = None
        self._reply_cycle = None
        self._sdk_privacy_fields = None
        self._storage_location = None
        self._system_permission_privacy_fields = None
        self._system_privacy_fields = None
        self._user_custom_file = None
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
    def plugin_privacy_fields(self):
        return self._plugin_privacy_fields

    @plugin_privacy_fields.setter
    def plugin_privacy_fields(self, value):
        if isinstance(value, list):
            self._plugin_privacy_fields = list()
            for i in value:
                if isinstance(i, PluginPrivacyFields):
                    self._plugin_privacy_fields.append(i)
                else:
                    self._plugin_privacy_fields.append(PluginPrivacyFields.from_alipay_dict(i))
    @property
    def reply_cycle(self):
        return self._reply_cycle

    @reply_cycle.setter
    def reply_cycle(self, value):
        self._reply_cycle = value
    @property
    def sdk_privacy_fields(self):
        return self._sdk_privacy_fields

    @sdk_privacy_fields.setter
    def sdk_privacy_fields(self, value):
        if isinstance(value, list):
            self._sdk_privacy_fields = list()
            for i in value:
                if isinstance(i, SdkPrivacyFields):
                    self._sdk_privacy_fields.append(i)
                else:
                    self._sdk_privacy_fields.append(SdkPrivacyFields.from_alipay_dict(i))
    @property
    def storage_location(self):
        return self._storage_location

    @storage_location.setter
    def storage_location(self, value):
        self._storage_location = value
    @property
    def system_permission_privacy_fields(self):
        return self._system_permission_privacy_fields

    @system_permission_privacy_fields.setter
    def system_permission_privacy_fields(self, value):
        if isinstance(value, list):
            self._system_permission_privacy_fields = list()
            for i in value:
                if isinstance(i, SystemPermissionPrivacyFields):
                    self._system_permission_privacy_fields.append(i)
                else:
                    self._system_permission_privacy_fields.append(SystemPermissionPrivacyFields.from_alipay_dict(i))
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
    def user_custom_file(self):
        return self._user_custom_file

    @user_custom_file.setter
    def user_custom_file(self, value):
        self._user_custom_file = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPrivacyOnlineversionQueryResponse, self).parse_response_content(response_content)
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'plugin_privacy_fields' in response:
            self.plugin_privacy_fields = response['plugin_privacy_fields']
        if 'reply_cycle' in response:
            self.reply_cycle = response['reply_cycle']
        if 'sdk_privacy_fields' in response:
            self.sdk_privacy_fields = response['sdk_privacy_fields']
        if 'storage_location' in response:
            self.storage_location = response['storage_location']
        if 'system_permission_privacy_fields' in response:
            self.system_permission_privacy_fields = response['system_permission_privacy_fields']
        if 'system_privacy_fields' in response:
            self.system_privacy_fields = response['system_privacy_fields']
        if 'user_custom_file' in response:
            self.user_custom_file = response['user_custom_file']
        if 'user_define_privacy_fields' in response:
            self.user_define_privacy_fields = response['user_define_privacy_fields']
