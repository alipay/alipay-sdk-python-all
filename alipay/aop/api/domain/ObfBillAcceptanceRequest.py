#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObfBillAcceptanceRequest(object):

    def __init__(self):
        self._amortization_rule = None
        self._bill_amount_cent = None
        self._bill_amount_currency_code = None
        self._bill_end_date = None
        self._bill_period = None
        self._bill_start_date = None
        self._channel_commodity_code = None
        self._channel_commodity_name = None
        self._customer_name = None
        self._idempotent_key = None
        self._ou_code = None
        self._our_contract_entity = None
        self._out_order_id = None
        self._properties = None
        self._settle_rate = None
        self._source_type = None
        self._source_uid = None
        self._strategy_identity = None
        self._tax_rate = None

    @property
    def amortization_rule(self):
        return self._amortization_rule

    @amortization_rule.setter
    def amortization_rule(self, value):
        self._amortization_rule = value
    @property
    def bill_amount_cent(self):
        return self._bill_amount_cent

    @bill_amount_cent.setter
    def bill_amount_cent(self, value):
        self._bill_amount_cent = value
    @property
    def bill_amount_currency_code(self):
        return self._bill_amount_currency_code

    @bill_amount_currency_code.setter
    def bill_amount_currency_code(self, value):
        self._bill_amount_currency_code = value
    @property
    def bill_end_date(self):
        return self._bill_end_date

    @bill_end_date.setter
    def bill_end_date(self, value):
        self._bill_end_date = value
    @property
    def bill_period(self):
        return self._bill_period

    @bill_period.setter
    def bill_period(self, value):
        self._bill_period = value
    @property
    def bill_start_date(self):
        return self._bill_start_date

    @bill_start_date.setter
    def bill_start_date(self, value):
        self._bill_start_date = value
    @property
    def channel_commodity_code(self):
        return self._channel_commodity_code

    @channel_commodity_code.setter
    def channel_commodity_code(self, value):
        self._channel_commodity_code = value
    @property
    def channel_commodity_name(self):
        return self._channel_commodity_name

    @channel_commodity_name.setter
    def channel_commodity_name(self, value):
        self._channel_commodity_name = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def idempotent_key(self):
        return self._idempotent_key

    @idempotent_key.setter
    def idempotent_key(self, value):
        self._idempotent_key = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def our_contract_entity(self):
        return self._our_contract_entity

    @our_contract_entity.setter
    def our_contract_entity(self, value):
        self._our_contract_entity = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def settle_rate(self):
        return self._settle_rate

    @settle_rate.setter
    def settle_rate(self, value):
        self._settle_rate = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def source_uid(self):
        return self._source_uid

    @source_uid.setter
    def source_uid(self, value):
        self._source_uid = value
    @property
    def strategy_identity(self):
        return self._strategy_identity

    @strategy_identity.setter
    def strategy_identity(self, value):
        self._strategy_identity = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.amortization_rule:
            if hasattr(self.amortization_rule, 'to_alipay_dict'):
                params['amortization_rule'] = self.amortization_rule.to_alipay_dict()
            else:
                params['amortization_rule'] = self.amortization_rule
        if self.bill_amount_cent:
            if hasattr(self.bill_amount_cent, 'to_alipay_dict'):
                params['bill_amount_cent'] = self.bill_amount_cent.to_alipay_dict()
            else:
                params['bill_amount_cent'] = self.bill_amount_cent
        if self.bill_amount_currency_code:
            if hasattr(self.bill_amount_currency_code, 'to_alipay_dict'):
                params['bill_amount_currency_code'] = self.bill_amount_currency_code.to_alipay_dict()
            else:
                params['bill_amount_currency_code'] = self.bill_amount_currency_code
        if self.bill_end_date:
            if hasattr(self.bill_end_date, 'to_alipay_dict'):
                params['bill_end_date'] = self.bill_end_date.to_alipay_dict()
            else:
                params['bill_end_date'] = self.bill_end_date
        if self.bill_period:
            if hasattr(self.bill_period, 'to_alipay_dict'):
                params['bill_period'] = self.bill_period.to_alipay_dict()
            else:
                params['bill_period'] = self.bill_period
        if self.bill_start_date:
            if hasattr(self.bill_start_date, 'to_alipay_dict'):
                params['bill_start_date'] = self.bill_start_date.to_alipay_dict()
            else:
                params['bill_start_date'] = self.bill_start_date
        if self.channel_commodity_code:
            if hasattr(self.channel_commodity_code, 'to_alipay_dict'):
                params['channel_commodity_code'] = self.channel_commodity_code.to_alipay_dict()
            else:
                params['channel_commodity_code'] = self.channel_commodity_code
        if self.channel_commodity_name:
            if hasattr(self.channel_commodity_name, 'to_alipay_dict'):
                params['channel_commodity_name'] = self.channel_commodity_name.to_alipay_dict()
            else:
                params['channel_commodity_name'] = self.channel_commodity_name
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.idempotent_key:
            if hasattr(self.idempotent_key, 'to_alipay_dict'):
                params['idempotent_key'] = self.idempotent_key.to_alipay_dict()
            else:
                params['idempotent_key'] = self.idempotent_key
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.our_contract_entity:
            if hasattr(self.our_contract_entity, 'to_alipay_dict'):
                params['our_contract_entity'] = self.our_contract_entity.to_alipay_dict()
            else:
                params['our_contract_entity'] = self.our_contract_entity
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.settle_rate:
            if hasattr(self.settle_rate, 'to_alipay_dict'):
                params['settle_rate'] = self.settle_rate.to_alipay_dict()
            else:
                params['settle_rate'] = self.settle_rate
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.source_uid:
            if hasattr(self.source_uid, 'to_alipay_dict'):
                params['source_uid'] = self.source_uid.to_alipay_dict()
            else:
                params['source_uid'] = self.source_uid
        if self.strategy_identity:
            if hasattr(self.strategy_identity, 'to_alipay_dict'):
                params['strategy_identity'] = self.strategy_identity.to_alipay_dict()
            else:
                params['strategy_identity'] = self.strategy_identity
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObfBillAcceptanceRequest()
        if 'amortization_rule' in d:
            o.amortization_rule = d['amortization_rule']
        if 'bill_amount_cent' in d:
            o.bill_amount_cent = d['bill_amount_cent']
        if 'bill_amount_currency_code' in d:
            o.bill_amount_currency_code = d['bill_amount_currency_code']
        if 'bill_end_date' in d:
            o.bill_end_date = d['bill_end_date']
        if 'bill_period' in d:
            o.bill_period = d['bill_period']
        if 'bill_start_date' in d:
            o.bill_start_date = d['bill_start_date']
        if 'channel_commodity_code' in d:
            o.channel_commodity_code = d['channel_commodity_code']
        if 'channel_commodity_name' in d:
            o.channel_commodity_name = d['channel_commodity_name']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'idempotent_key' in d:
            o.idempotent_key = d['idempotent_key']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'our_contract_entity' in d:
            o.our_contract_entity = d['our_contract_entity']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'properties' in d:
            o.properties = d['properties']
        if 'settle_rate' in d:
            o.settle_rate = d['settle_rate']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'source_uid' in d:
            o.source_uid = d['source_uid']
        if 'strategy_identity' in d:
            o.strategy_identity = d['strategy_identity']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


