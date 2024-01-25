#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OBContractDTO import OBContractDTO


class OBCompanyDTO(object):

    def __init__(self):
        self._contract_list = None
        self._entity_id = None
        self._entity_name = None
        self._ma_check_status = None
        self._org_id = None
        self._work_order_permission = None

    @property
    def contract_list(self):
        return self._contract_list

    @contract_list.setter
    def contract_list(self, value):
        if isinstance(value, list):
            self._contract_list = list()
            for i in value:
                if isinstance(i, OBContractDTO):
                    self._contract_list.append(i)
                else:
                    self._contract_list.append(OBContractDTO.from_alipay_dict(i))
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def ma_check_status(self):
        return self._ma_check_status

    @ma_check_status.setter
    def ma_check_status(self, value):
        self._ma_check_status = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def work_order_permission(self):
        return self._work_order_permission

    @work_order_permission.setter
    def work_order_permission(self, value):
        self._work_order_permission = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_list:
            if isinstance(self.contract_list, list):
                for i in range(0, len(self.contract_list)):
                    element = self.contract_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_list, 'to_alipay_dict'):
                params['contract_list'] = self.contract_list.to_alipay_dict()
            else:
                params['contract_list'] = self.contract_list
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.ma_check_status:
            if hasattr(self.ma_check_status, 'to_alipay_dict'):
                params['ma_check_status'] = self.ma_check_status.to_alipay_dict()
            else:
                params['ma_check_status'] = self.ma_check_status
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.work_order_permission:
            if hasattr(self.work_order_permission, 'to_alipay_dict'):
                params['work_order_permission'] = self.work_order_permission.to_alipay_dict()
            else:
                params['work_order_permission'] = self.work_order_permission
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OBCompanyDTO()
        if 'contract_list' in d:
            o.contract_list = d['contract_list']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'ma_check_status' in d:
            o.ma_check_status = d['ma_check_status']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'work_order_permission' in d:
            o.work_order_permission = d['work_order_permission']
        return o


