#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptIdentityInfo import ReceiptIdentityInfo


class AlipayCommerceEcReceiptidentitygroupCreateModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._identity_group_name = None
        self._identity_list = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def identity_group_name(self):
        return self._identity_group_name

    @identity_group_name.setter
    def identity_group_name(self, value):
        self._identity_group_name = value
    @property
    def identity_list(self):
        return self._identity_list

    @identity_list.setter
    def identity_list(self, value):
        if isinstance(value, list):
            self._identity_list = list()
            for i in value:
                if isinstance(i, ReceiptIdentityInfo):
                    self._identity_list.append(i)
                else:
                    self._identity_list.append(ReceiptIdentityInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.identity_group_name:
            if hasattr(self.identity_group_name, 'to_alipay_dict'):
                params['identity_group_name'] = self.identity_group_name.to_alipay_dict()
            else:
                params['identity_group_name'] = self.identity_group_name
        if self.identity_list:
            if isinstance(self.identity_list, list):
                for i in range(0, len(self.identity_list)):
                    element = self.identity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identity_list[i] = element.to_alipay_dict()
            if hasattr(self.identity_list, 'to_alipay_dict'):
                params['identity_list'] = self.identity_list.to_alipay_dict()
            else:
                params['identity_list'] = self.identity_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcReceiptidentitygroupCreateModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'identity_group_name' in d:
            o.identity_group_name = d['identity_group_name']
        if 'identity_list' in d:
            o.identity_list = d['identity_list']
        return o


