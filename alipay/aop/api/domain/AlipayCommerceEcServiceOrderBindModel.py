#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceAbility import ServiceAbility


class AlipayCommerceEcServiceOrderBindModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._buyer_id = None
        self._buyer_role_type = None
        self._enterprise_id = None
        self._related_service_id = None
        self._service_ability_info_list = None
        self._service_id = None

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
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_role_type(self):
        return self._buyer_role_type

    @buyer_role_type.setter
    def buyer_role_type(self, value):
        self._buyer_role_type = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def related_service_id(self):
        return self._related_service_id

    @related_service_id.setter
    def related_service_id(self, value):
        self._related_service_id = value
    @property
    def service_ability_info_list(self):
        return self._service_ability_info_list

    @service_ability_info_list.setter
    def service_ability_info_list(self, value):
        if isinstance(value, list):
            self._service_ability_info_list = list()
            for i in value:
                if isinstance(i, ServiceAbility):
                    self._service_ability_info_list.append(i)
                else:
                    self._service_ability_info_list.append(ServiceAbility.from_alipay_dict(i))
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


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
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_role_type:
            if hasattr(self.buyer_role_type, 'to_alipay_dict'):
                params['buyer_role_type'] = self.buyer_role_type.to_alipay_dict()
            else:
                params['buyer_role_type'] = self.buyer_role_type
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.related_service_id:
            if hasattr(self.related_service_id, 'to_alipay_dict'):
                params['related_service_id'] = self.related_service_id.to_alipay_dict()
            else:
                params['related_service_id'] = self.related_service_id
        if self.service_ability_info_list:
            if isinstance(self.service_ability_info_list, list):
                for i in range(0, len(self.service_ability_info_list)):
                    element = self.service_ability_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_ability_info_list[i] = element.to_alipay_dict()
            if hasattr(self.service_ability_info_list, 'to_alipay_dict'):
                params['service_ability_info_list'] = self.service_ability_info_list.to_alipay_dict()
            else:
                params['service_ability_info_list'] = self.service_ability_info_list
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcServiceOrderBindModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_role_type' in d:
            o.buyer_role_type = d['buyer_role_type']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'related_service_id' in d:
            o.related_service_id = d['related_service_id']
        if 'service_ability_info_list' in d:
            o.service_ability_info_list = d['service_ability_info_list']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


