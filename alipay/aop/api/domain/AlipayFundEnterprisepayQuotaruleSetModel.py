#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO


class AlipayFundEnterprisepayQuotaruleSetModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._biz_scene = None
        self._member_id = None
        self._open_id = None
        self._operation_type = None
        self._product_code = None
        self._quota_list = None

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
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def quota_list(self):
        return self._quota_list

    @quota_list.setter
    def quota_list(self, value):
        if isinstance(value, list):
            self._quota_list = list()
            for i in value:
                if isinstance(i, JointAccountQuotaDTO):
                    self._quota_list.append(i)
                else:
                    self._quota_list.append(JointAccountQuotaDTO.from_alipay_dict(i))


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
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.quota_list:
            if isinstance(self.quota_list, list):
                for i in range(0, len(self.quota_list)):
                    element = self.quota_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quota_list[i] = element.to_alipay_dict()
            if hasattr(self.quota_list, 'to_alipay_dict'):
                params['quota_list'] = self.quota_list.to_alipay_dict()
            else:
                params['quota_list'] = self.quota_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundEnterprisepayQuotaruleSetModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'quota_list' in d:
            o.quota_list = d['quota_list']
        return o


