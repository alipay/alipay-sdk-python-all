#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcocheckYzPolicyCheckDetail(object):

    def __init__(self):
        self._app_code = None
        self._app_online_check = None
        self._mau = None
        self._msg_check = None
        self._post_check = None
        self._scan_check = None
        self._searchkeyword_check = None
        self._service_apply_check = None
        self._service_apply_check_fail_reason = None
        self._thirdparty_app_check = None
        self._valid_trans_amount = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def app_online_check(self):
        return self._app_online_check

    @app_online_check.setter
    def app_online_check(self, value):
        self._app_online_check = value
    @property
    def mau(self):
        return self._mau

    @mau.setter
    def mau(self, value):
        self._mau = value
    @property
    def msg_check(self):
        return self._msg_check

    @msg_check.setter
    def msg_check(self, value):
        self._msg_check = value
    @property
    def post_check(self):
        return self._post_check

    @post_check.setter
    def post_check(self, value):
        self._post_check = value
    @property
    def scan_check(self):
        return self._scan_check

    @scan_check.setter
    def scan_check(self, value):
        self._scan_check = value
    @property
    def searchkeyword_check(self):
        return self._searchkeyword_check

    @searchkeyword_check.setter
    def searchkeyword_check(self, value):
        self._searchkeyword_check = value
    @property
    def service_apply_check(self):
        return self._service_apply_check

    @service_apply_check.setter
    def service_apply_check(self, value):
        self._service_apply_check = value
    @property
    def service_apply_check_fail_reason(self):
        return self._service_apply_check_fail_reason

    @service_apply_check_fail_reason.setter
    def service_apply_check_fail_reason(self, value):
        self._service_apply_check_fail_reason = value
    @property
    def thirdparty_app_check(self):
        return self._thirdparty_app_check

    @thirdparty_app_check.setter
    def thirdparty_app_check(self, value):
        self._thirdparty_app_check = value
    @property
    def valid_trans_amount(self):
        return self._valid_trans_amount

    @valid_trans_amount.setter
    def valid_trans_amount(self, value):
        self._valid_trans_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.app_online_check:
            if hasattr(self.app_online_check, 'to_alipay_dict'):
                params['app_online_check'] = self.app_online_check.to_alipay_dict()
            else:
                params['app_online_check'] = self.app_online_check
        if self.mau:
            if hasattr(self.mau, 'to_alipay_dict'):
                params['mau'] = self.mau.to_alipay_dict()
            else:
                params['mau'] = self.mau
        if self.msg_check:
            if hasattr(self.msg_check, 'to_alipay_dict'):
                params['msg_check'] = self.msg_check.to_alipay_dict()
            else:
                params['msg_check'] = self.msg_check
        if self.post_check:
            if hasattr(self.post_check, 'to_alipay_dict'):
                params['post_check'] = self.post_check.to_alipay_dict()
            else:
                params['post_check'] = self.post_check
        if self.scan_check:
            if hasattr(self.scan_check, 'to_alipay_dict'):
                params['scan_check'] = self.scan_check.to_alipay_dict()
            else:
                params['scan_check'] = self.scan_check
        if self.searchkeyword_check:
            if hasattr(self.searchkeyword_check, 'to_alipay_dict'):
                params['searchkeyword_check'] = self.searchkeyword_check.to_alipay_dict()
            else:
                params['searchkeyword_check'] = self.searchkeyword_check
        if self.service_apply_check:
            if hasattr(self.service_apply_check, 'to_alipay_dict'):
                params['service_apply_check'] = self.service_apply_check.to_alipay_dict()
            else:
                params['service_apply_check'] = self.service_apply_check
        if self.service_apply_check_fail_reason:
            if hasattr(self.service_apply_check_fail_reason, 'to_alipay_dict'):
                params['service_apply_check_fail_reason'] = self.service_apply_check_fail_reason.to_alipay_dict()
            else:
                params['service_apply_check_fail_reason'] = self.service_apply_check_fail_reason
        if self.thirdparty_app_check:
            if hasattr(self.thirdparty_app_check, 'to_alipay_dict'):
                params['thirdparty_app_check'] = self.thirdparty_app_check.to_alipay_dict()
            else:
                params['thirdparty_app_check'] = self.thirdparty_app_check
        if self.valid_trans_amount:
            if hasattr(self.valid_trans_amount, 'to_alipay_dict'):
                params['valid_trans_amount'] = self.valid_trans_amount.to_alipay_dict()
            else:
                params['valid_trans_amount'] = self.valid_trans_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcocheckYzPolicyCheckDetail()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'app_online_check' in d:
            o.app_online_check = d['app_online_check']
        if 'mau' in d:
            o.mau = d['mau']
        if 'msg_check' in d:
            o.msg_check = d['msg_check']
        if 'post_check' in d:
            o.post_check = d['post_check']
        if 'scan_check' in d:
            o.scan_check = d['scan_check']
        if 'searchkeyword_check' in d:
            o.searchkeyword_check = d['searchkeyword_check']
        if 'service_apply_check' in d:
            o.service_apply_check = d['service_apply_check']
        if 'service_apply_check_fail_reason' in d:
            o.service_apply_check_fail_reason = d['service_apply_check_fail_reason']
        if 'thirdparty_app_check' in d:
            o.thirdparty_app_check = d['thirdparty_app_check']
        if 'valid_trans_amount' in d:
            o.valid_trans_amount = d['valid_trans_amount']
        return o


