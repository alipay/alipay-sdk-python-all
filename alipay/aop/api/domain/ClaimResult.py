#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClaimResultPolicyInfo import ClaimResultPolicyInfo


class ClaimResult(object):

    def __init__(self):
        self._apply_no = None
        self._biz_no = None
        self._claim_no = None
        self._claim_status = None
        self._company_type = None
        self._mdtrt_id = None
        self._policy_info = None
        self._report_status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
    @property
    def policy_info(self):
        return self._policy_info

    @policy_info.setter
    def policy_info(self, value):
        if isinstance(value, ClaimResultPolicyInfo):
            self._policy_info = value
        else:
            self._policy_info = ClaimResultPolicyInfo.from_alipay_dict(value)
    @property
    def report_status(self):
        return self._report_status

    @report_status.setter
    def report_status(self, value):
        self._report_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.mdtrt_id:
            if hasattr(self.mdtrt_id, 'to_alipay_dict'):
                params['mdtrt_id'] = self.mdtrt_id.to_alipay_dict()
            else:
                params['mdtrt_id'] = self.mdtrt_id
        if self.policy_info:
            if hasattr(self.policy_info, 'to_alipay_dict'):
                params['policy_info'] = self.policy_info.to_alipay_dict()
            else:
                params['policy_info'] = self.policy_info
        if self.report_status:
            if hasattr(self.report_status, 'to_alipay_dict'):
                params['report_status'] = self.report_status.to_alipay_dict()
            else:
                params['report_status'] = self.report_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimResult()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'mdtrt_id' in d:
            o.mdtrt_id = d['mdtrt_id']
        if 'policy_info' in d:
            o.policy_info = d['policy_info']
        if 'report_status' in d:
            o.report_status = d['report_status']
        return o


