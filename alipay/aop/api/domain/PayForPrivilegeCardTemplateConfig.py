#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayForPrivilegeCardTemplateAuxiliaryItem import PayForPrivilegeCardTemplateAuxiliaryItem
from alipay.aop.api.domain.PayForPrivilegeCardTemplateHeaderConfig import PayForPrivilegeCardTemplateHeaderConfig
from alipay.aop.api.domain.PayForPrivilegeCardTemplateOperationItem import PayForPrivilegeCardTemplateOperationItem
from alipay.aop.api.domain.PayForPrivilegeCardTemplateSecondaryItem import PayForPrivilegeCardTemplateSecondaryItem


class PayForPrivilegeCardTemplateConfig(object):

    def __init__(self):
        self._auxiliary_item_list = None
        self._header = None
        self._operation_item_list = None
        self._secondary_item_list = None

    @property
    def auxiliary_item_list(self):
        return self._auxiliary_item_list

    @auxiliary_item_list.setter
    def auxiliary_item_list(self, value):
        if isinstance(value, list):
            self._auxiliary_item_list = list()
            for i in value:
                if isinstance(i, PayForPrivilegeCardTemplateAuxiliaryItem):
                    self._auxiliary_item_list.append(i)
                else:
                    self._auxiliary_item_list.append(PayForPrivilegeCardTemplateAuxiliaryItem.from_alipay_dict(i))
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, PayForPrivilegeCardTemplateHeaderConfig):
            self._header = value
        else:
            self._header = PayForPrivilegeCardTemplateHeaderConfig.from_alipay_dict(value)
    @property
    def operation_item_list(self):
        return self._operation_item_list

    @operation_item_list.setter
    def operation_item_list(self, value):
        if isinstance(value, list):
            self._operation_item_list = list()
            for i in value:
                if isinstance(i, PayForPrivilegeCardTemplateOperationItem):
                    self._operation_item_list.append(i)
                else:
                    self._operation_item_list.append(PayForPrivilegeCardTemplateOperationItem.from_alipay_dict(i))
    @property
    def secondary_item_list(self):
        return self._secondary_item_list

    @secondary_item_list.setter
    def secondary_item_list(self, value):
        if isinstance(value, list):
            self._secondary_item_list = list()
            for i in value:
                if isinstance(i, PayForPrivilegeCardTemplateSecondaryItem):
                    self._secondary_item_list.append(i)
                else:
                    self._secondary_item_list.append(PayForPrivilegeCardTemplateSecondaryItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auxiliary_item_list:
            if isinstance(self.auxiliary_item_list, list):
                for i in range(0, len(self.auxiliary_item_list)):
                    element = self.auxiliary_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auxiliary_item_list[i] = element.to_alipay_dict()
            if hasattr(self.auxiliary_item_list, 'to_alipay_dict'):
                params['auxiliary_item_list'] = self.auxiliary_item_list.to_alipay_dict()
            else:
                params['auxiliary_item_list'] = self.auxiliary_item_list
        if self.header:
            if hasattr(self.header, 'to_alipay_dict'):
                params['header'] = self.header.to_alipay_dict()
            else:
                params['header'] = self.header
        if self.operation_item_list:
            if isinstance(self.operation_item_list, list):
                for i in range(0, len(self.operation_item_list)):
                    element = self.operation_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_item_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_item_list, 'to_alipay_dict'):
                params['operation_item_list'] = self.operation_item_list.to_alipay_dict()
            else:
                params['operation_item_list'] = self.operation_item_list
        if self.secondary_item_list:
            if isinstance(self.secondary_item_list, list):
                for i in range(0, len(self.secondary_item_list)):
                    element = self.secondary_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.secondary_item_list[i] = element.to_alipay_dict()
            if hasattr(self.secondary_item_list, 'to_alipay_dict'):
                params['secondary_item_list'] = self.secondary_item_list.to_alipay_dict()
            else:
                params['secondary_item_list'] = self.secondary_item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayForPrivilegeCardTemplateConfig()
        if 'auxiliary_item_list' in d:
            o.auxiliary_item_list = d['auxiliary_item_list']
        if 'header' in d:
            o.header = d['header']
        if 'operation_item_list' in d:
            o.operation_item_list = d['operation_item_list']
        if 'secondary_item_list' in d:
            o.secondary_item_list = d['secondary_item_list']
        return o


