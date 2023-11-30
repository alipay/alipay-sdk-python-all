#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PucRoyaltyDetailInfo import PucRoyaltyDetailInfo


class PucExternalOrder(object):

    def __init__(self):
        self._address = None
        self._amount = None
        self._bill_date = None
        self._billkey = None
        self._biz_type = None
        self._business_param = None
        self._charge_inst = None
        self._contract_no = None
        self._extra_settle_entity_id = None
        self._name = None
        self._out_biz_no = None
        self._royalty_parameters = None
        self._sub_biz_type = None
        self._sys_service_provider_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def business_param(self):
        return self._business_param

    @business_param.setter
    def business_param(self, value):
        self._business_param = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def extra_settle_entity_id(self):
        return self._extra_settle_entity_id

    @extra_settle_entity_id.setter
    def extra_settle_entity_id(self, value):
        self._extra_settle_entity_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def royalty_parameters(self):
        return self._royalty_parameters

    @royalty_parameters.setter
    def royalty_parameters(self, value):
        if isinstance(value, list):
            self._royalty_parameters = list()
            for i in value:
                if isinstance(i, PucRoyaltyDetailInfo):
                    self._royalty_parameters.append(i)
                else:
                    self._royalty_parameters.append(PucRoyaltyDetailInfo.from_alipay_dict(i))
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.billkey:
            if hasattr(self.billkey, 'to_alipay_dict'):
                params['billkey'] = self.billkey.to_alipay_dict()
            else:
                params['billkey'] = self.billkey
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.business_param:
            if hasattr(self.business_param, 'to_alipay_dict'):
                params['business_param'] = self.business_param.to_alipay_dict()
            else:
                params['business_param'] = self.business_param
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.extra_settle_entity_id:
            if hasattr(self.extra_settle_entity_id, 'to_alipay_dict'):
                params['extra_settle_entity_id'] = self.extra_settle_entity_id.to_alipay_dict()
            else:
                params['extra_settle_entity_id'] = self.extra_settle_entity_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.royalty_parameters:
            if isinstance(self.royalty_parameters, list):
                for i in range(0, len(self.royalty_parameters)):
                    element = self.royalty_parameters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_parameters[i] = element.to_alipay_dict()
            if hasattr(self.royalty_parameters, 'to_alipay_dict'):
                params['royalty_parameters'] = self.royalty_parameters.to_alipay_dict()
            else:
                params['royalty_parameters'] = self.royalty_parameters
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PucExternalOrder()
        if 'address' in d:
            o.address = d['address']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'billkey' in d:
            o.billkey = d['billkey']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'business_param' in d:
            o.business_param = d['business_param']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'extra_settle_entity_id' in d:
            o.extra_settle_entity_id = d['extra_settle_entity_id']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'royalty_parameters' in d:
            o.royalty_parameters = d['royalty_parameters']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


