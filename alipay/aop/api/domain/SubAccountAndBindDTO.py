#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankSubAccountBaseInfoDTO import BankSubAccountBaseInfoDTO


class SubAccountAndBindDTO(object):

    def __init__(self):
        self._bank_sub_account_base_info_dto = None
        self._biz_unique_id = None
        self._biz_unique_type = None
        self._inst_id = None
        self._ip_role_id = None

    @property
    def bank_sub_account_base_info_dto(self):
        return self._bank_sub_account_base_info_dto

    @bank_sub_account_base_info_dto.setter
    def bank_sub_account_base_info_dto(self, value):
        if isinstance(value, BankSubAccountBaseInfoDTO):
            self._bank_sub_account_base_info_dto = value
        else:
            self._bank_sub_account_base_info_dto = BankSubAccountBaseInfoDTO.from_alipay_dict(value)
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def biz_unique_type(self):
        return self._biz_unique_type

    @biz_unique_type.setter
    def biz_unique_type(self, value):
        self._biz_unique_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_sub_account_base_info_dto:
            if hasattr(self.bank_sub_account_base_info_dto, 'to_alipay_dict'):
                params['bank_sub_account_base_info_dto'] = self.bank_sub_account_base_info_dto.to_alipay_dict()
            else:
                params['bank_sub_account_base_info_dto'] = self.bank_sub_account_base_info_dto
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.biz_unique_type:
            if hasattr(self.biz_unique_type, 'to_alipay_dict'):
                params['biz_unique_type'] = self.biz_unique_type.to_alipay_dict()
            else:
                params['biz_unique_type'] = self.biz_unique_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountAndBindDTO()
        if 'bank_sub_account_base_info_dto' in d:
            o.bank_sub_account_base_info_dto = d['bank_sub_account_base_info_dto']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'biz_unique_type' in d:
            o.biz_unique_type = d['biz_unique_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        return o


