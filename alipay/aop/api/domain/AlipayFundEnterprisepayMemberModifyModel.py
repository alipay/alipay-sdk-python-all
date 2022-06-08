#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundExtInfo import FundExtInfo


class AlipayFundEnterprisepayMemberModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._biz_scene = None
        self._fund_ext_info = None
        self._group_id_list = None
        self._operation_type_list = None
        self._product_code = None
        self._user_id = None

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
    def fund_ext_info(self):
        return self._fund_ext_info

    @fund_ext_info.setter
    def fund_ext_info(self, value):
        if isinstance(value, FundExtInfo):
            self._fund_ext_info = value
        else:
            self._fund_ext_info = FundExtInfo.from_alipay_dict(value)
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def operation_type_list(self):
        return self._operation_type_list

    @operation_type_list.setter
    def operation_type_list(self, value):
        if isinstance(value, list):
            self._operation_type_list = list()
            for i in value:
                self._operation_type_list.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.fund_ext_info:
            if hasattr(self.fund_ext_info, 'to_alipay_dict'):
                params['fund_ext_info'] = self.fund_ext_info.to_alipay_dict()
            else:
                params['fund_ext_info'] = self.fund_ext_info
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.operation_type_list:
            if isinstance(self.operation_type_list, list):
                for i in range(0, len(self.operation_type_list)):
                    element = self.operation_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_type_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_type_list, 'to_alipay_dict'):
                params['operation_type_list'] = self.operation_type_list.to_alipay_dict()
            else:
                params['operation_type_list'] = self.operation_type_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = AlipayFundEnterprisepayMemberModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'fund_ext_info' in d:
            o.fund_ext_info = d['fund_ext_info']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'operation_type_list' in d:
            o.operation_type_list = d['operation_type_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


