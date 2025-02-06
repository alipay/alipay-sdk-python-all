#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmCrmClueSyncModel(object):

    def __init__(self):
        self._contact_name = None
        self._ext_info = None
        self._external_contact_id = None
        self._mobile_phone = None
        self._open_notify = None
        self._tenant_id = None
        self._use_virtual_phone = None
        self._virtual_phone = None
        self._virtual_phone_type = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_contact_id(self):
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, value):
        self._external_contact_id = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def open_notify(self):
        return self._open_notify

    @open_notify.setter
    def open_notify(self, value):
        self._open_notify = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def use_virtual_phone(self):
        return self._use_virtual_phone

    @use_virtual_phone.setter
    def use_virtual_phone(self, value):
        self._use_virtual_phone = value
    @property
    def virtual_phone(self):
        return self._virtual_phone

    @virtual_phone.setter
    def virtual_phone(self, value):
        self._virtual_phone = value
    @property
    def virtual_phone_type(self):
        return self._virtual_phone_type

    @virtual_phone_type.setter
    def virtual_phone_type(self, value):
        self._virtual_phone_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_contact_id:
            if hasattr(self.external_contact_id, 'to_alipay_dict'):
                params['external_contact_id'] = self.external_contact_id.to_alipay_dict()
            else:
                params['external_contact_id'] = self.external_contact_id
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.open_notify:
            if hasattr(self.open_notify, 'to_alipay_dict'):
                params['open_notify'] = self.open_notify.to_alipay_dict()
            else:
                params['open_notify'] = self.open_notify
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.use_virtual_phone:
            if hasattr(self.use_virtual_phone, 'to_alipay_dict'):
                params['use_virtual_phone'] = self.use_virtual_phone.to_alipay_dict()
            else:
                params['use_virtual_phone'] = self.use_virtual_phone
        if self.virtual_phone:
            if hasattr(self.virtual_phone, 'to_alipay_dict'):
                params['virtual_phone'] = self.virtual_phone.to_alipay_dict()
            else:
                params['virtual_phone'] = self.virtual_phone
        if self.virtual_phone_type:
            if hasattr(self.virtual_phone_type, 'to_alipay_dict'):
                params['virtual_phone_type'] = self.virtual_phone_type.to_alipay_dict()
            else:
                params['virtual_phone_type'] = self.virtual_phone_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmCrmClueSyncModel()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_contact_id' in d:
            o.external_contact_id = d['external_contact_id']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'open_notify' in d:
            o.open_notify = d['open_notify']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'use_virtual_phone' in d:
            o.use_virtual_phone = d['use_virtual_phone']
        if 'virtual_phone' in d:
            o.virtual_phone = d['virtual_phone']
        if 'virtual_phone_type' in d:
            o.virtual_phone_type = d['virtual_phone_type']
        return o


