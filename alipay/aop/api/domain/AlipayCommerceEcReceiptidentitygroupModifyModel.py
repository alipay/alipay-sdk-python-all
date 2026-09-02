#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptIdentityInfo import ReceiptIdentityInfo
from alipay.aop.api.domain.ReceiptIdentityInfo import ReceiptIdentityInfo


class AlipayCommerceEcReceiptidentitygroupModifyModel(object):

    def __init__(self):
        self._add_identity_list = None
        self._delete_identity_list = None
        self._enterprise_id = None
        self._identity_group_id = None
        self._identity_group_name = None

    @property
    def add_identity_list(self):
        return self._add_identity_list

    @add_identity_list.setter
    def add_identity_list(self, value):
        if isinstance(value, list):
            self._add_identity_list = list()
            for i in value:
                if isinstance(i, ReceiptIdentityInfo):
                    self._add_identity_list.append(i)
                else:
                    self._add_identity_list.append(ReceiptIdentityInfo.from_alipay_dict(i))
    @property
    def delete_identity_list(self):
        return self._delete_identity_list

    @delete_identity_list.setter
    def delete_identity_list(self, value):
        if isinstance(value, list):
            self._delete_identity_list = list()
            for i in value:
                if isinstance(i, ReceiptIdentityInfo):
                    self._delete_identity_list.append(i)
                else:
                    self._delete_identity_list.append(ReceiptIdentityInfo.from_alipay_dict(i))
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def identity_group_id(self):
        return self._identity_group_id

    @identity_group_id.setter
    def identity_group_id(self, value):
        self._identity_group_id = value
    @property
    def identity_group_name(self):
        return self._identity_group_name

    @identity_group_name.setter
    def identity_group_name(self, value):
        self._identity_group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_identity_list:
            if isinstance(self.add_identity_list, list):
                for i in range(0, len(self.add_identity_list)):
                    element = self.add_identity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_identity_list[i] = element.to_alipay_dict()
            if hasattr(self.add_identity_list, 'to_alipay_dict'):
                params['add_identity_list'] = self.add_identity_list.to_alipay_dict()
            else:
                params['add_identity_list'] = self.add_identity_list
        if self.delete_identity_list:
            if isinstance(self.delete_identity_list, list):
                for i in range(0, len(self.delete_identity_list)):
                    element = self.delete_identity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_identity_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_identity_list, 'to_alipay_dict'):
                params['delete_identity_list'] = self.delete_identity_list.to_alipay_dict()
            else:
                params['delete_identity_list'] = self.delete_identity_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.identity_group_id:
            if hasattr(self.identity_group_id, 'to_alipay_dict'):
                params['identity_group_id'] = self.identity_group_id.to_alipay_dict()
            else:
                params['identity_group_id'] = self.identity_group_id
        if self.identity_group_name:
            if hasattr(self.identity_group_name, 'to_alipay_dict'):
                params['identity_group_name'] = self.identity_group_name.to_alipay_dict()
            else:
                params['identity_group_name'] = self.identity_group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcReceiptidentitygroupModifyModel()
        if 'add_identity_list' in d:
            o.add_identity_list = d['add_identity_list']
        if 'delete_identity_list' in d:
            o.delete_identity_list = d['delete_identity_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'identity_group_id' in d:
            o.identity_group_id = d['identity_group_id']
        if 'identity_group_name' in d:
            o.identity_group_name = d['identity_group_name']
        return o


