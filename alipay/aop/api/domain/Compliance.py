#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Compliance(object):

    def __init__(self):
        self._compliance_check_status = None
        self._compliance_detail_code = None
        self._compliance_detail_msg = None
        self._evidence_type = None

    @property
    def compliance_check_status(self):
        return self._compliance_check_status

    @compliance_check_status.setter
    def compliance_check_status(self, value):
        self._compliance_check_status = value
    @property
    def compliance_detail_code(self):
        return self._compliance_detail_code

    @compliance_detail_code.setter
    def compliance_detail_code(self, value):
        self._compliance_detail_code = value
    @property
    def compliance_detail_msg(self):
        return self._compliance_detail_msg

    @compliance_detail_msg.setter
    def compliance_detail_msg(self, value):
        self._compliance_detail_msg = value
    @property
    def evidence_type(self):
        return self._evidence_type

    @evidence_type.setter
    def evidence_type(self, value):
        self._evidence_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.compliance_check_status:
            if hasattr(self.compliance_check_status, 'to_alipay_dict'):
                params['compliance_check_status'] = self.compliance_check_status.to_alipay_dict()
            else:
                params['compliance_check_status'] = self.compliance_check_status
        if self.compliance_detail_code:
            if hasattr(self.compliance_detail_code, 'to_alipay_dict'):
                params['compliance_detail_code'] = self.compliance_detail_code.to_alipay_dict()
            else:
                params['compliance_detail_code'] = self.compliance_detail_code
        if self.compliance_detail_msg:
            if hasattr(self.compliance_detail_msg, 'to_alipay_dict'):
                params['compliance_detail_msg'] = self.compliance_detail_msg.to_alipay_dict()
            else:
                params['compliance_detail_msg'] = self.compliance_detail_msg
        if self.evidence_type:
            if hasattr(self.evidence_type, 'to_alipay_dict'):
                params['evidence_type'] = self.evidence_type.to_alipay_dict()
            else:
                params['evidence_type'] = self.evidence_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Compliance()
        if 'compliance_check_status' in d:
            o.compliance_check_status = d['compliance_check_status']
        if 'compliance_detail_code' in d:
            o.compliance_detail_code = d['compliance_detail_code']
        if 'compliance_detail_msg' in d:
            o.compliance_detail_msg = d['compliance_detail_msg']
        if 'evidence_type' in d:
            o.evidence_type = d['evidence_type']
        return o


