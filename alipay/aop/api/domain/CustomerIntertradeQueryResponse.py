#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerIntertradeQueryResponse(object):

    def __init__(self):
        self._bid = None
        self._cid = None
        self._customer_name = None
        self._fin_biz_entity = None
        self._internal_settlement_flag = None
        self._intertrade_ou_code = None
        self._intertrade_relation = None
        self._intertrade_type = None
        self._passport_id = None
        self._region = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def fin_biz_entity(self):
        return self._fin_biz_entity

    @fin_biz_entity.setter
    def fin_biz_entity(self, value):
        self._fin_biz_entity = value
    @property
    def internal_settlement_flag(self):
        return self._internal_settlement_flag

    @internal_settlement_flag.setter
    def internal_settlement_flag(self, value):
        self._internal_settlement_flag = value
    @property
    def intertrade_ou_code(self):
        return self._intertrade_ou_code

    @intertrade_ou_code.setter
    def intertrade_ou_code(self, value):
        self._intertrade_ou_code = value
    @property
    def intertrade_relation(self):
        return self._intertrade_relation

    @intertrade_relation.setter
    def intertrade_relation(self, value):
        self._intertrade_relation = value
    @property
    def intertrade_type(self):
        return self._intertrade_type

    @intertrade_type.setter
    def intertrade_type(self, value):
        self._intertrade_type = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.fin_biz_entity:
            if hasattr(self.fin_biz_entity, 'to_alipay_dict'):
                params['fin_biz_entity'] = self.fin_biz_entity.to_alipay_dict()
            else:
                params['fin_biz_entity'] = self.fin_biz_entity
        if self.internal_settlement_flag:
            if hasattr(self.internal_settlement_flag, 'to_alipay_dict'):
                params['internal_settlement_flag'] = self.internal_settlement_flag.to_alipay_dict()
            else:
                params['internal_settlement_flag'] = self.internal_settlement_flag
        if self.intertrade_ou_code:
            if hasattr(self.intertrade_ou_code, 'to_alipay_dict'):
                params['intertrade_ou_code'] = self.intertrade_ou_code.to_alipay_dict()
            else:
                params['intertrade_ou_code'] = self.intertrade_ou_code
        if self.intertrade_relation:
            if hasattr(self.intertrade_relation, 'to_alipay_dict'):
                params['intertrade_relation'] = self.intertrade_relation.to_alipay_dict()
            else:
                params['intertrade_relation'] = self.intertrade_relation
        if self.intertrade_type:
            if hasattr(self.intertrade_type, 'to_alipay_dict'):
                params['intertrade_type'] = self.intertrade_type.to_alipay_dict()
            else:
                params['intertrade_type'] = self.intertrade_type
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerIntertradeQueryResponse()
        if 'bid' in d:
            o.bid = d['bid']
        if 'cid' in d:
            o.cid = d['cid']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'fin_biz_entity' in d:
            o.fin_biz_entity = d['fin_biz_entity']
        if 'internal_settlement_flag' in d:
            o.internal_settlement_flag = d['internal_settlement_flag']
        if 'intertrade_ou_code' in d:
            o.intertrade_ou_code = d['intertrade_ou_code']
        if 'intertrade_relation' in d:
            o.intertrade_relation = d['intertrade_relation']
        if 'intertrade_type' in d:
            o.intertrade_type = d['intertrade_type']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'region' in d:
            o.region = d['region']
        return o


