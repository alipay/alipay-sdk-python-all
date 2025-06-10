#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalConfigmItemDTO import ApprovalConfigmItemDTO


class ApprovalConfigDTO(object):

    def __init__(self):
        self._approval_config_list = None
        self._config_id = None
        self._enterprise_id = None
        self._payment_type = None
        self._scene_category = None
        self._scene_sub_category = None

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
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def scene_category(self):
        return self._scene_category

    @scene_category.setter
    def scene_category(self, value):
        self._scene_category = value
    @property
    def scene_sub_category(self):
        return self._scene_sub_category

    @scene_sub_category.setter
    def scene_sub_category(self, value):
        self._scene_sub_category = value


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
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.scene_category:
            if hasattr(self.scene_category, 'to_alipay_dict'):
                params['scene_category'] = self.scene_category.to_alipay_dict()
            else:
                params['scene_category'] = self.scene_category
        if self.scene_sub_category:
            if hasattr(self.scene_sub_category, 'to_alipay_dict'):
                params['scene_sub_category'] = self.scene_sub_category.to_alipay_dict()
            else:
                params['scene_sub_category'] = self.scene_sub_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalConfigDTO()
        if 'approval_config_list' in d:
            o.approval_config_list = d['approval_config_list']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'scene_category' in d:
            o.scene_category = d['scene_category']
        if 'scene_sub_category' in d:
            o.scene_sub_category = d['scene_sub_category']
        return o


