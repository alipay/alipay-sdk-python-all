#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistSrcfgoventerAccessApproveModel(object):

    def __init__(self):
        self._cert_no = None
        self._gov_enter_name = None
        self._ip_id = None
        self._out_bsn_no = None
        self._prod_code = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def gov_enter_name(self):
        return self._gov_enter_name

    @gov_enter_name.setter
    def gov_enter_name(self, value):
        self._gov_enter_name = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def out_bsn_no(self):
        return self._out_bsn_no

    @out_bsn_no.setter
    def out_bsn_no(self, value):
        self._out_bsn_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.gov_enter_name:
            if hasattr(self.gov_enter_name, 'to_alipay_dict'):
                params['gov_enter_name'] = self.gov_enter_name.to_alipay_dict()
            else:
                params['gov_enter_name'] = self.gov_enter_name
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.out_bsn_no:
            if hasattr(self.out_bsn_no, 'to_alipay_dict'):
                params['out_bsn_no'] = self.out_bsn_no.to_alipay_dict()
            else:
                params['out_bsn_no'] = self.out_bsn_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistSrcfgoventerAccessApproveModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'gov_enter_name' in d:
            o.gov_enter_name = d['gov_enter_name']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'out_bsn_no' in d:
            o.out_bsn_no = d['out_bsn_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


