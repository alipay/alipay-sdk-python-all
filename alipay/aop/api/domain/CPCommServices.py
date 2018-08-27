#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CPCommServices(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._audit_desc = None
        self._audit_status = None
        self._category_name = None
        self._external_address_scan_result = None
        self._external_invoke_address = None
        self._gmt_created = None
        self._gmt_modified = None
        self._next_action = None
        self._qr_code_expires = None
        self._qr_code_image = None
        self._qr_code_type = None
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
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def external_address_scan_result(self):
        return self._external_address_scan_result

    @external_address_scan_result.setter
    def external_address_scan_result(self, value):
        self._external_address_scan_result = value
    @property
    def external_invoke_address(self):
        return self._external_invoke_address

    @external_invoke_address.setter
    def external_invoke_address(self, value):
        self._external_invoke_address = value
    @property
    def gmt_created(self):
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, value):
        self._gmt_created = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, value):
        self._next_action = value
    @property
    def qr_code_expires(self):
        return self._qr_code_expires

    @qr_code_expires.setter
    def qr_code_expires(self, value):
        self._qr_code_expires = value
    @property
    def qr_code_image(self):
        return self._qr_code_image

    @qr_code_image.setter
    def qr_code_image(self, value):
        self._qr_code_image = value
    @property
    def qr_code_type(self):
        return self._qr_code_type

    @qr_code_type.setter
    def qr_code_type(self, value):
        self._qr_code_type = value
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
        if self.audit_desc:
            if hasattr(self.audit_desc, 'to_alipay_dict'):
                params['audit_desc'] = self.audit_desc.to_alipay_dict()
            else:
                params['audit_desc'] = self.audit_desc
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.external_address_scan_result:
            if hasattr(self.external_address_scan_result, 'to_alipay_dict'):
                params['external_address_scan_result'] = self.external_address_scan_result.to_alipay_dict()
            else:
                params['external_address_scan_result'] = self.external_address_scan_result
        if self.external_invoke_address:
            if hasattr(self.external_invoke_address, 'to_alipay_dict'):
                params['external_invoke_address'] = self.external_invoke_address.to_alipay_dict()
            else:
                params['external_invoke_address'] = self.external_invoke_address
        if self.gmt_created:
            if hasattr(self.gmt_created, 'to_alipay_dict'):
                params['gmt_created'] = self.gmt_created.to_alipay_dict()
            else:
                params['gmt_created'] = self.gmt_created
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.next_action:
            if hasattr(self.next_action, 'to_alipay_dict'):
                params['next_action'] = self.next_action.to_alipay_dict()
            else:
                params['next_action'] = self.next_action
        if self.qr_code_expires:
            if hasattr(self.qr_code_expires, 'to_alipay_dict'):
                params['qr_code_expires'] = self.qr_code_expires.to_alipay_dict()
            else:
                params['qr_code_expires'] = self.qr_code_expires
        if self.qr_code_image:
            if hasattr(self.qr_code_image, 'to_alipay_dict'):
                params['qr_code_image'] = self.qr_code_image.to_alipay_dict()
            else:
                params['qr_code_image'] = self.qr_code_image
        if self.qr_code_type:
            if hasattr(self.qr_code_type, 'to_alipay_dict'):
                params['qr_code_type'] = self.qr_code_type.to_alipay_dict()
            else:
                params['qr_code_type'] = self.qr_code_type
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
        o = CPCommServices()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'audit_desc' in d:
            o.audit_desc = d['audit_desc']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'external_address_scan_result' in d:
            o.external_address_scan_result = d['external_address_scan_result']
        if 'external_invoke_address' in d:
            o.external_invoke_address = d['external_invoke_address']
        if 'gmt_created' in d:
            o.gmt_created = d['gmt_created']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'next_action' in d:
            o.next_action = d['next_action']
        if 'qr_code_expires' in d:
            o.qr_code_expires = d['qr_code_expires']
        if 'qr_code_image' in d:
            o.qr_code_image = d['qr_code_image']
        if 'qr_code_type' in d:
            o.qr_code_type = d['qr_code_type']
        if 'service_expires' in d:
            o.service_expires = d['service_expires']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'status' in d:
            o.status = d['status']
        return o


