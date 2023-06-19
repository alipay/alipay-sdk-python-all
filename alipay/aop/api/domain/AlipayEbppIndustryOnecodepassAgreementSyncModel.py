#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryOnecodepassAgreementSyncModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_type = None
        self._cert_type = None
        self._open_id = None
        self._status = None
        self._status_code = None
        self._status_msg = None
        self._sync_action = None
        self._uid = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def status_msg(self):
        return self._status_msg

    @status_msg.setter
    def status_msg(self, value):
        self._status_msg = value
    @property
    def sync_action(self):
        return self._sync_action

    @sync_action.setter
    def sync_action(self, value):
        self._sync_action = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.status_msg:
            if hasattr(self.status_msg, 'to_alipay_dict'):
                params['status_msg'] = self.status_msg.to_alipay_dict()
            else:
                params['status_msg'] = self.status_msg
        if self.sync_action:
            if hasattr(self.sync_action, 'to_alipay_dict'):
                params['sync_action'] = self.sync_action.to_alipay_dict()
            else:
                params['sync_action'] = self.sync_action
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryOnecodepassAgreementSyncModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'status_msg' in d:
            o.status_msg = d['status_msg']
        if 'sync_action' in d:
            o.sync_action = d['sync_action']
        if 'uid' in d:
            o.uid = d['uid']
        return o


