#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseAddressDeleteModel(object):

    def __init__(self):
        self._address_id_list = None
        self._enterprise_id = None

    @property
    def address_id_list(self):
        return self._address_id_list

    @address_id_list.setter
    def address_id_list(self, value):
        if isinstance(value, list):
            self._address_id_list = list()
            for i in value:
                self._address_id_list.append(i)
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_id_list:
            if isinstance(self.address_id_list, list):
                for i in range(0, len(self.address_id_list)):
                    element = self.address_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.address_id_list[i] = element.to_alipay_dict()
            if hasattr(self.address_id_list, 'to_alipay_dict'):
                params['address_id_list'] = self.address_id_list.to_alipay_dict()
            else:
                params['address_id_list'] = self.address_id_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseAddressDeleteModel()
        if 'address_id_list' in d:
            o.address_id_list = d['address_id_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


