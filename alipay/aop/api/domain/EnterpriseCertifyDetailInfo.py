#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseCertifyDetailInfo(object):

    def __init__(self):
        self._certify_end_time = None
        self._certify_order_no = None
        self._credit_code = None
        self._enterprise_name = None
        self._legal_representative_id_no_postfix = None
        self._legal_representative_name = None
        self._out_request_no = None
        self._status = None
        self._status_desc = None

    @property
    def certify_end_time(self):
        return self._certify_end_time

    @certify_end_time.setter
    def certify_end_time(self, value):
        self._certify_end_time = value
    @property
    def certify_order_no(self):
        return self._certify_order_no

    @certify_order_no.setter
    def certify_order_no(self, value):
        self._certify_order_no = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def legal_representative_id_no_postfix(self):
        return self._legal_representative_id_no_postfix

    @legal_representative_id_no_postfix.setter
    def legal_representative_id_no_postfix(self, value):
        self._legal_representative_id_no_postfix = value
    @property
    def legal_representative_name(self):
        return self._legal_representative_name

    @legal_representative_name.setter
    def legal_representative_name(self, value):
        self._legal_representative_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_end_time:
            if hasattr(self.certify_end_time, 'to_alipay_dict'):
                params['certify_end_time'] = self.certify_end_time.to_alipay_dict()
            else:
                params['certify_end_time'] = self.certify_end_time
        if self.certify_order_no:
            if hasattr(self.certify_order_no, 'to_alipay_dict'):
                params['certify_order_no'] = self.certify_order_no.to_alipay_dict()
            else:
                params['certify_order_no'] = self.certify_order_no
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.legal_representative_id_no_postfix:
            if hasattr(self.legal_representative_id_no_postfix, 'to_alipay_dict'):
                params['legal_representative_id_no_postfix'] = self.legal_representative_id_no_postfix.to_alipay_dict()
            else:
                params['legal_representative_id_no_postfix'] = self.legal_representative_id_no_postfix
        if self.legal_representative_name:
            if hasattr(self.legal_representative_name, 'to_alipay_dict'):
                params['legal_representative_name'] = self.legal_representative_name.to_alipay_dict()
            else:
                params['legal_representative_name'] = self.legal_representative_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseCertifyDetailInfo()
        if 'certify_end_time' in d:
            o.certify_end_time = d['certify_end_time']
        if 'certify_order_no' in d:
            o.certify_order_no = d['certify_order_no']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'legal_representative_id_no_postfix' in d:
            o.legal_representative_id_no_postfix = d['legal_representative_id_no_postfix']
        if 'legal_representative_name' in d:
            o.legal_representative_name = d['legal_representative_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


