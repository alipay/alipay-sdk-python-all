#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DrugDTO import DrugDTO


class AlipayInsSceneHealthDrugcatalogueBatchqueryModel(object):

    def __init__(self):
        self._ant_ser_contract_no = None
        self._disease_name_list = None
        self._emergency = None
        self._general_name_list = None
        self._item_name_list = None
        self._pre_select_drug_list = None

    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value
    @property
    def disease_name_list(self):
        return self._disease_name_list

    @disease_name_list.setter
    def disease_name_list(self, value):
        if isinstance(value, list):
            self._disease_name_list = list()
            for i in value:
                self._disease_name_list.append(i)
    @property
    def emergency(self):
        return self._emergency

    @emergency.setter
    def emergency(self, value):
        self._emergency = value
    @property
    def general_name_list(self):
        return self._general_name_list

    @general_name_list.setter
    def general_name_list(self, value):
        if isinstance(value, list):
            self._general_name_list = list()
            for i in value:
                self._general_name_list.append(i)
    @property
    def item_name_list(self):
        return self._item_name_list

    @item_name_list.setter
    def item_name_list(self, value):
        if isinstance(value, list):
            self._item_name_list = list()
            for i in value:
                self._item_name_list.append(i)
    @property
    def pre_select_drug_list(self):
        return self._pre_select_drug_list

    @pre_select_drug_list.setter
    def pre_select_drug_list(self, value):
        if isinstance(value, list):
            self._pre_select_drug_list = list()
            for i in value:
                if isinstance(i, DrugDTO):
                    self._pre_select_drug_list.append(i)
                else:
                    self._pre_select_drug_list.append(DrugDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
        if self.disease_name_list:
            if isinstance(self.disease_name_list, list):
                for i in range(0, len(self.disease_name_list)):
                    element = self.disease_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disease_name_list[i] = element.to_alipay_dict()
            if hasattr(self.disease_name_list, 'to_alipay_dict'):
                params['disease_name_list'] = self.disease_name_list.to_alipay_dict()
            else:
                params['disease_name_list'] = self.disease_name_list
        if self.emergency:
            if hasattr(self.emergency, 'to_alipay_dict'):
                params['emergency'] = self.emergency.to_alipay_dict()
            else:
                params['emergency'] = self.emergency
        if self.general_name_list:
            if isinstance(self.general_name_list, list):
                for i in range(0, len(self.general_name_list)):
                    element = self.general_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.general_name_list[i] = element.to_alipay_dict()
            if hasattr(self.general_name_list, 'to_alipay_dict'):
                params['general_name_list'] = self.general_name_list.to_alipay_dict()
            else:
                params['general_name_list'] = self.general_name_list
        if self.item_name_list:
            if isinstance(self.item_name_list, list):
                for i in range(0, len(self.item_name_list)):
                    element = self.item_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_name_list[i] = element.to_alipay_dict()
            if hasattr(self.item_name_list, 'to_alipay_dict'):
                params['item_name_list'] = self.item_name_list.to_alipay_dict()
            else:
                params['item_name_list'] = self.item_name_list
        if self.pre_select_drug_list:
            if isinstance(self.pre_select_drug_list, list):
                for i in range(0, len(self.pre_select_drug_list)):
                    element = self.pre_select_drug_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pre_select_drug_list[i] = element.to_alipay_dict()
            if hasattr(self.pre_select_drug_list, 'to_alipay_dict'):
                params['pre_select_drug_list'] = self.pre_select_drug_list.to_alipay_dict()
            else:
                params['pre_select_drug_list'] = self.pre_select_drug_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneHealthDrugcatalogueBatchqueryModel()
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        if 'disease_name_list' in d:
            o.disease_name_list = d['disease_name_list']
        if 'emergency' in d:
            o.emergency = d['emergency']
        if 'general_name_list' in d:
            o.general_name_list = d['general_name_list']
        if 'item_name_list' in d:
            o.item_name_list = d['item_name_list']
        if 'pre_select_drug_list' in d:
            o.pre_select_drug_list = d['pre_select_drug_list']
        return o


