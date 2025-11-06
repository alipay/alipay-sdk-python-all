#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmUserequitySyncModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._company_account = None
        self._equity_package_code = None
        self._out_biz_serial_no = None
        self._out_user_id = None
        self._project_tag = None
        self._tel_no = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def company_account(self):
        return self._company_account

    @company_account.setter
    def company_account(self, value):
        self._company_account = value
    @property
    def equity_package_code(self):
        return self._equity_package_code

    @equity_package_code.setter
    def equity_package_code(self, value):
        self._equity_package_code = value
    @property
    def out_biz_serial_no(self):
        return self._out_biz_serial_no

    @out_biz_serial_no.setter
    def out_biz_serial_no(self, value):
        self._out_biz_serial_no = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def project_tag(self):
        return self._project_tag

    @project_tag.setter
    def project_tag(self, value):
        self._project_tag = value
    @property
    def tel_no(self):
        return self._tel_no

    @tel_no.setter
    def tel_no(self, value):
        self._tel_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.company_account:
            if hasattr(self.company_account, 'to_alipay_dict'):
                params['company_account'] = self.company_account.to_alipay_dict()
            else:
                params['company_account'] = self.company_account
        if self.equity_package_code:
            if hasattr(self.equity_package_code, 'to_alipay_dict'):
                params['equity_package_code'] = self.equity_package_code.to_alipay_dict()
            else:
                params['equity_package_code'] = self.equity_package_code
        if self.out_biz_serial_no:
            if hasattr(self.out_biz_serial_no, 'to_alipay_dict'):
                params['out_biz_serial_no'] = self.out_biz_serial_no.to_alipay_dict()
            else:
                params['out_biz_serial_no'] = self.out_biz_serial_no
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.project_tag:
            if hasattr(self.project_tag, 'to_alipay_dict'):
                params['project_tag'] = self.project_tag.to_alipay_dict()
            else:
                params['project_tag'] = self.project_tag
        if self.tel_no:
            if hasattr(self.tel_no, 'to_alipay_dict'):
                params['tel_no'] = self.tel_no.to_alipay_dict()
            else:
                params['tel_no'] = self.tel_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmUserequitySyncModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'company_account' in d:
            o.company_account = d['company_account']
        if 'equity_package_code' in d:
            o.equity_package_code = d['equity_package_code']
        if 'out_biz_serial_no' in d:
            o.out_biz_serial_no = d['out_biz_serial_no']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'project_tag' in d:
            o.project_tag = d['project_tag']
        if 'tel_no' in d:
            o.tel_no = d['tel_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


