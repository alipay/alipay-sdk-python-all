#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeBasicserviceModifyModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._community_id = None
        self._external_invoke_address = None
        self._service_expires = None
        self._service_type = None
        self._status = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def external_invoke_address(self):
        return self._external_invoke_address

    @external_invoke_address.setter
    def external_invoke_address(self, value):
        self._external_invoke_address = value
    @property
    def service_expires(self):
        return self._service_expires

    @service_expires.setter
    def service_expires(self, value):
        self._service_expires = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.external_invoke_address:
            if hasattr(self.external_invoke_address, 'to_alipay_dict'):
                params['external_invoke_address'] = self.external_invoke_address.to_alipay_dict()
            else:
                params['external_invoke_address'] = self.external_invoke_address
        if self.service_expires:
            if hasattr(self.service_expires, 'to_alipay_dict'):
                params['service_expires'] = self.service_expires.to_alipay_dict()
            else:
                params['service_expires'] = self.service_expires
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
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
        o = AlipayEcoCplifeBasicserviceModifyModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'external_invoke_address' in d:
            o.external_invoke_address = d['external_invoke_address']
        if 'service_expires' in d:
            o.service_expires = d['service_expires']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'status' in d:
            o.status = d['status']
        return o


