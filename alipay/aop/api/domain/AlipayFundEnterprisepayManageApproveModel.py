#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdentityInfo import IdentityInfo
from alipay.aop.api.domain.IdentityInfo import IdentityInfo


class AlipayFundEnterprisepayManageApproveModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._applicant_info = None
        self._approve_info = None
        self._biz_scene = None
        self._operation = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def applicant_info(self):
        return self._applicant_info

    @applicant_info.setter
    def applicant_info(self, value):
        if isinstance(value, IdentityInfo):
            self._applicant_info = value
        else:
            self._applicant_info = IdentityInfo.from_alipay_dict(value)
    @property
    def approve_info(self):
        return self._approve_info

    @approve_info.setter
    def approve_info(self, value):
        if isinstance(value, IdentityInfo):
            self._approve_info = value
        else:
            self._approve_info = IdentityInfo.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.applicant_info:
            if hasattr(self.applicant_info, 'to_alipay_dict'):
                params['applicant_info'] = self.applicant_info.to_alipay_dict()
            else:
                params['applicant_info'] = self.applicant_info
        if self.approve_info:
            if hasattr(self.approve_info, 'to_alipay_dict'):
                params['approve_info'] = self.approve_info.to_alipay_dict()
            else:
                params['approve_info'] = self.approve_info
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundEnterprisepayManageApproveModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'applicant_info' in d:
            o.applicant_info = d['applicant_info']
        if 'approve_info' in d:
            o.approve_info = d['approve_info']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'operation' in d:
            o.operation = d['operation']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


