#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalConfigmItemDTO import ApprovalConfigmItemDTO


class AlipayCommerceEcApprovalConfigModifyModel(object):

    def __init__(self):
        self._approval_config_list = None
        self._enterprise_id = None
        self._expense_type_sub_category = None
        self._payment_type = None
        self._scene = None

    @property
    def approval_config_list(self):
        return self._approval_config_list

    @approval_config_list.setter
    def approval_config_list(self, value):
        if isinstance(value, list):
            self._approval_config_list = list()
            for i in value:
                if isinstance(i, ApprovalConfigmItemDTO):
                    self._approval_config_list.append(i)
                else:
                    self._approval_config_list.append(ApprovalConfigmItemDTO.from_alipay_dict(i))
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_config_list:
            if isinstance(self.approval_config_list, list):
                for i in range(0, len(self.approval_config_list)):
                    element = self.approval_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approval_config_list[i] = element.to_alipay_dict()
            if hasattr(self.approval_config_list, 'to_alipay_dict'):
                params['approval_config_list'] = self.approval_config_list.to_alipay_dict()
            else:
                params['approval_config_list'] = self.approval_config_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcApprovalConfigModifyModel()
        if 'approval_config_list' in d:
            o.approval_config_list = d['approval_config_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'scene' in d:
            o.scene = d['scene']
        return o


