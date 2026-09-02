#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceTpapreauthstatusNotifyModel(object):

    def __init__(self):
        self._deposit_amount = None
        self._ext_info = None
        self._open_id = None
        self._pre_auth_audit_status = None
        self._pre_auth_audit_status_msg = None
        self._pre_auth_no = None
        self._pre_auth_quota = None
        self._tpa_id = None
        self._user_id = None

    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pre_auth_audit_status(self):
        return self._pre_auth_audit_status

    @pre_auth_audit_status.setter
    def pre_auth_audit_status(self, value):
        self._pre_auth_audit_status = value
    @property
    def pre_auth_audit_status_msg(self):
        return self._pre_auth_audit_status_msg

    @pre_auth_audit_status_msg.setter
    def pre_auth_audit_status_msg(self, value):
        self._pre_auth_audit_status_msg = value
    @property
    def pre_auth_no(self):
        return self._pre_auth_no

    @pre_auth_no.setter
    def pre_auth_no(self, value):
        self._pre_auth_no = value
    @property
    def pre_auth_quota(self):
        return self._pre_auth_quota

    @pre_auth_quota.setter
    def pre_auth_quota(self, value):
        self._pre_auth_quota = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pre_auth_audit_status:
            if hasattr(self.pre_auth_audit_status, 'to_alipay_dict'):
                params['pre_auth_audit_status'] = self.pre_auth_audit_status.to_alipay_dict()
            else:
                params['pre_auth_audit_status'] = self.pre_auth_audit_status
        if self.pre_auth_audit_status_msg:
            if hasattr(self.pre_auth_audit_status_msg, 'to_alipay_dict'):
                params['pre_auth_audit_status_msg'] = self.pre_auth_audit_status_msg.to_alipay_dict()
            else:
                params['pre_auth_audit_status_msg'] = self.pre_auth_audit_status_msg
        if self.pre_auth_no:
            if hasattr(self.pre_auth_no, 'to_alipay_dict'):
                params['pre_auth_no'] = self.pre_auth_no.to_alipay_dict()
            else:
                params['pre_auth_no'] = self.pre_auth_no
        if self.pre_auth_quota:
            if hasattr(self.pre_auth_quota, 'to_alipay_dict'):
                params['pre_auth_quota'] = self.pre_auth_quota.to_alipay_dict()
            else:
                params['pre_auth_quota'] = self.pre_auth_quota
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpapreauthstatusNotifyModel()
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pre_auth_audit_status' in d:
            o.pre_auth_audit_status = d['pre_auth_audit_status']
        if 'pre_auth_audit_status_msg' in d:
            o.pre_auth_audit_status_msg = d['pre_auth_audit_status_msg']
        if 'pre_auth_no' in d:
            o.pre_auth_no = d['pre_auth_no']
        if 'pre_auth_quota' in d:
            o.pre_auth_quota = d['pre_auth_quota']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


