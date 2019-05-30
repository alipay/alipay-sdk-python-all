#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyPromotionDynamicurlGetModel(object):

    def __init__(self):
        self._arrangement_no = None
        self._dept_code = None
        self._op_ch_code = None
        self._passiver_cert_name = None
        self._passiver_cert_no = None
        self._passiver_id = None
        self._recmd_inst_ip_id = None
        self._recmd_inst_ip_role_id = None
        self._staff_id = None
        self._staff_type = None

    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def dept_code(self):
        return self._dept_code

    @dept_code.setter
    def dept_code(self, value):
        self._dept_code = value
    @property
    def op_ch_code(self):
        return self._op_ch_code

    @op_ch_code.setter
    def op_ch_code(self, value):
        self._op_ch_code = value
    @property
    def passiver_cert_name(self):
        return self._passiver_cert_name

    @passiver_cert_name.setter
    def passiver_cert_name(self, value):
        self._passiver_cert_name = value
    @property
    def passiver_cert_no(self):
        return self._passiver_cert_no

    @passiver_cert_no.setter
    def passiver_cert_no(self, value):
        self._passiver_cert_no = value
    @property
    def passiver_id(self):
        return self._passiver_id

    @passiver_id.setter
    def passiver_id(self, value):
        self._passiver_id = value
    @property
    def recmd_inst_ip_id(self):
        return self._recmd_inst_ip_id

    @recmd_inst_ip_id.setter
    def recmd_inst_ip_id(self, value):
        self._recmd_inst_ip_id = value
    @property
    def recmd_inst_ip_role_id(self):
        return self._recmd_inst_ip_role_id

    @recmd_inst_ip_role_id.setter
    def recmd_inst_ip_role_id(self, value):
        self._recmd_inst_ip_role_id = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
    @property
    def staff_type(self):
        return self._staff_type

    @staff_type.setter
    def staff_type(self, value):
        self._staff_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.dept_code:
            if hasattr(self.dept_code, 'to_alipay_dict'):
                params['dept_code'] = self.dept_code.to_alipay_dict()
            else:
                params['dept_code'] = self.dept_code
        if self.op_ch_code:
            if hasattr(self.op_ch_code, 'to_alipay_dict'):
                params['op_ch_code'] = self.op_ch_code.to_alipay_dict()
            else:
                params['op_ch_code'] = self.op_ch_code
        if self.passiver_cert_name:
            if hasattr(self.passiver_cert_name, 'to_alipay_dict'):
                params['passiver_cert_name'] = self.passiver_cert_name.to_alipay_dict()
            else:
                params['passiver_cert_name'] = self.passiver_cert_name
        if self.passiver_cert_no:
            if hasattr(self.passiver_cert_no, 'to_alipay_dict'):
                params['passiver_cert_no'] = self.passiver_cert_no.to_alipay_dict()
            else:
                params['passiver_cert_no'] = self.passiver_cert_no
        if self.passiver_id:
            if hasattr(self.passiver_id, 'to_alipay_dict'):
                params['passiver_id'] = self.passiver_id.to_alipay_dict()
            else:
                params['passiver_id'] = self.passiver_id
        if self.recmd_inst_ip_id:
            if hasattr(self.recmd_inst_ip_id, 'to_alipay_dict'):
                params['recmd_inst_ip_id'] = self.recmd_inst_ip_id.to_alipay_dict()
            else:
                params['recmd_inst_ip_id'] = self.recmd_inst_ip_id
        if self.recmd_inst_ip_role_id:
            if hasattr(self.recmd_inst_ip_role_id, 'to_alipay_dict'):
                params['recmd_inst_ip_role_id'] = self.recmd_inst_ip_role_id.to_alipay_dict()
            else:
                params['recmd_inst_ip_role_id'] = self.recmd_inst_ip_role_id
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        if self.staff_type:
            if hasattr(self.staff_type, 'to_alipay_dict'):
                params['staff_type'] = self.staff_type.to_alipay_dict()
            else:
                params['staff_type'] = self.staff_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyPromotionDynamicurlGetModel()
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'dept_code' in d:
            o.dept_code = d['dept_code']
        if 'op_ch_code' in d:
            o.op_ch_code = d['op_ch_code']
        if 'passiver_cert_name' in d:
            o.passiver_cert_name = d['passiver_cert_name']
        if 'passiver_cert_no' in d:
            o.passiver_cert_no = d['passiver_cert_no']
        if 'passiver_id' in d:
            o.passiver_id = d['passiver_id']
        if 'recmd_inst_ip_id' in d:
            o.recmd_inst_ip_id = d['recmd_inst_ip_id']
        if 'recmd_inst_ip_role_id' in d:
            o.recmd_inst_ip_role_id = d['recmd_inst_ip_role_id']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        if 'staff_type' in d:
            o.staff_type = d['staff_type']
        return o


