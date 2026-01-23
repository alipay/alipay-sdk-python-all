#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmUserequityQueryModel(object):

    def __init__(self):
        self._equity_basics_code = None
        self._equity_package_code = None
        self._out_biz_serial_no = None
        self._out_user_id = None
        self._project_tag = None
        self._user_id = None

    @property
    def equity_basics_code(self):
        return self._equity_basics_code

    @equity_basics_code.setter
    def equity_basics_code(self, value):
        self._equity_basics_code = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.equity_basics_code:
            if hasattr(self.equity_basics_code, 'to_alipay_dict'):
                params['equity_basics_code'] = self.equity_basics_code.to_alipay_dict()
            else:
                params['equity_basics_code'] = self.equity_basics_code
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
        o = AlipayCommerceMedicalHmUserequityQueryModel()
        if 'equity_basics_code' in d:
            o.equity_basics_code = d['equity_basics_code']
        if 'equity_package_code' in d:
            o.equity_package_code = d['equity_package_code']
        if 'out_biz_serial_no' in d:
            o.out_biz_serial_no = d['out_biz_serial_no']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'project_tag' in d:
            o.project_tag = d['project_tag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


