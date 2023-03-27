#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlCollectionCreateDebtDTO import AlCollectionCreateDebtDTO
from alipay.aop.api.domain.AlCollectionReceiveBaseInfoDTO import AlCollectionReceiveBaseInfoDTO
from alipay.aop.api.domain.ContractInfoDTO import ContractInfoDTO
from alipay.aop.api.domain.OppositeSubjectDTO import OppositeSubjectDTO
from alipay.aop.api.domain.OurSubjectInfoDTO import OurSubjectInfoDTO


class AntLinkeAlcollectioncenterCreateModel(object):

    def __init__(self):
        self._al_collection_create_debt = None
        self._app_name = None
        self._base_info = None
        self._contract_info = None
        self._operator = None
        self._opposite_subject_dto = None
        self._our_subject_info = None
        self._tenant = None

    @property
    def al_collection_create_debt(self):
        return self._al_collection_create_debt

    @al_collection_create_debt.setter
    def al_collection_create_debt(self, value):
        if isinstance(value, AlCollectionCreateDebtDTO):
            self._al_collection_create_debt = value
        else:
            self._al_collection_create_debt = AlCollectionCreateDebtDTO.from_alipay_dict(value)
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, AlCollectionReceiveBaseInfoDTO):
            self._base_info = value
        else:
            self._base_info = AlCollectionReceiveBaseInfoDTO.from_alipay_dict(value)
    @property
    def contract_info(self):
        return self._contract_info

    @contract_info.setter
    def contract_info(self, value):
        if isinstance(value, ContractInfoDTO):
            self._contract_info = value
        else:
            self._contract_info = ContractInfoDTO.from_alipay_dict(value)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def opposite_subject_dto(self):
        return self._opposite_subject_dto

    @opposite_subject_dto.setter
    def opposite_subject_dto(self, value):
        if isinstance(value, OppositeSubjectDTO):
            self._opposite_subject_dto = value
        else:
            self._opposite_subject_dto = OppositeSubjectDTO.from_alipay_dict(value)
    @property
    def our_subject_info(self):
        return self._our_subject_info

    @our_subject_info.setter
    def our_subject_info(self, value):
        if isinstance(value, OurSubjectInfoDTO):
            self._our_subject_info = value
        else:
            self._our_subject_info = OurSubjectInfoDTO.from_alipay_dict(value)
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.al_collection_create_debt:
            if hasattr(self.al_collection_create_debt, 'to_alipay_dict'):
                params['al_collection_create_debt'] = self.al_collection_create_debt.to_alipay_dict()
            else:
                params['al_collection_create_debt'] = self.al_collection_create_debt
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.contract_info:
            if hasattr(self.contract_info, 'to_alipay_dict'):
                params['contract_info'] = self.contract_info.to_alipay_dict()
            else:
                params['contract_info'] = self.contract_info
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.opposite_subject_dto:
            if hasattr(self.opposite_subject_dto, 'to_alipay_dict'):
                params['opposite_subject_dto'] = self.opposite_subject_dto.to_alipay_dict()
            else:
                params['opposite_subject_dto'] = self.opposite_subject_dto
        if self.our_subject_info:
            if hasattr(self.our_subject_info, 'to_alipay_dict'):
                params['our_subject_info'] = self.our_subject_info.to_alipay_dict()
            else:
                params['our_subject_info'] = self.our_subject_info
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeAlcollectioncenterCreateModel()
        if 'al_collection_create_debt' in d:
            o.al_collection_create_debt = d['al_collection_create_debt']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'contract_info' in d:
            o.contract_info = d['contract_info']
        if 'operator' in d:
            o.operator = d['operator']
        if 'opposite_subject_dto' in d:
            o.opposite_subject_dto = d['opposite_subject_dto']
        if 'our_subject_info' in d:
            o.our_subject_info = d['our_subject_info']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


