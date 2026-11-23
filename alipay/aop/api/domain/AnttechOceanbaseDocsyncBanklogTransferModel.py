#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankLogDTO import BankLogDTO


class AnttechOceanbaseDocsyncBanklogTransferModel(object):

    def __init__(self):
        self._account_no = None
        self._bank_log_dto = None
        self._business_code = None
        self._charge_amount = None
        self._charge_ccy = None
        self._crossccy_flag = None
        self._exchange = None
        self._fundlog_source = None
        self._id = None
        self._income_type = None
        self._inst_id = None
        self._ip_role_id = None
        self._link_no = None
        self._memo = None
        self._operator = None
        self._trading_partner_code = None
        self._trading_partner_type = None
        self._trans_dt = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def bank_log_dto(self):
        return self._bank_log_dto

    @bank_log_dto.setter
    def bank_log_dto(self, value):
        if isinstance(value, BankLogDTO):
            self._bank_log_dto = value
        else:
            self._bank_log_dto = BankLogDTO.from_alipay_dict(value)
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def charge_amount(self):
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, value):
        self._charge_amount = value
    @property
    def charge_ccy(self):
        return self._charge_ccy

    @charge_ccy.setter
    def charge_ccy(self, value):
        self._charge_ccy = value
    @property
    def crossccy_flag(self):
        return self._crossccy_flag

    @crossccy_flag.setter
    def crossccy_flag(self, value):
        self._crossccy_flag = value
    @property
    def exchange(self):
        return self._exchange

    @exchange.setter
    def exchange(self, value):
        self._exchange = value
    @property
    def fundlog_source(self):
        return self._fundlog_source

    @fundlog_source.setter
    def fundlog_source(self, value):
        self._fundlog_source = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def income_type(self):
        return self._income_type

    @income_type.setter
    def income_type(self, value):
        self._income_type = value
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
    @property
    def link_no(self):
        return self._link_no

    @link_no.setter
    def link_no(self, value):
        self._link_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def trading_partner_code(self):
        return self._trading_partner_code

    @trading_partner_code.setter
    def trading_partner_code(self, value):
        self._trading_partner_code = value
    @property
    def trading_partner_type(self):
        return self._trading_partner_type

    @trading_partner_type.setter
    def trading_partner_type(self, value):
        self._trading_partner_type = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.bank_log_dto:
            if hasattr(self.bank_log_dto, 'to_alipay_dict'):
                params['bank_log_dto'] = self.bank_log_dto.to_alipay_dict()
            else:
                params['bank_log_dto'] = self.bank_log_dto
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.charge_amount:
            if hasattr(self.charge_amount, 'to_alipay_dict'):
                params['charge_amount'] = self.charge_amount.to_alipay_dict()
            else:
                params['charge_amount'] = self.charge_amount
        if self.charge_ccy:
            if hasattr(self.charge_ccy, 'to_alipay_dict'):
                params['charge_ccy'] = self.charge_ccy.to_alipay_dict()
            else:
                params['charge_ccy'] = self.charge_ccy
        if self.crossccy_flag:
            if hasattr(self.crossccy_flag, 'to_alipay_dict'):
                params['crossccy_flag'] = self.crossccy_flag.to_alipay_dict()
            else:
                params['crossccy_flag'] = self.crossccy_flag
        if self.exchange:
            if hasattr(self.exchange, 'to_alipay_dict'):
                params['exchange'] = self.exchange.to_alipay_dict()
            else:
                params['exchange'] = self.exchange
        if self.fundlog_source:
            if hasattr(self.fundlog_source, 'to_alipay_dict'):
                params['fundlog_source'] = self.fundlog_source.to_alipay_dict()
            else:
                params['fundlog_source'] = self.fundlog_source
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.income_type:
            if hasattr(self.income_type, 'to_alipay_dict'):
                params['income_type'] = self.income_type.to_alipay_dict()
            else:
                params['income_type'] = self.income_type
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
        if self.link_no:
            if hasattr(self.link_no, 'to_alipay_dict'):
                params['link_no'] = self.link_no.to_alipay_dict()
            else:
                params['link_no'] = self.link_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.trading_partner_code:
            if hasattr(self.trading_partner_code, 'to_alipay_dict'):
                params['trading_partner_code'] = self.trading_partner_code.to_alipay_dict()
            else:
                params['trading_partner_code'] = self.trading_partner_code
        if self.trading_partner_type:
            if hasattr(self.trading_partner_type, 'to_alipay_dict'):
                params['trading_partner_type'] = self.trading_partner_type.to_alipay_dict()
            else:
                params['trading_partner_type'] = self.trading_partner_type
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseDocsyncBanklogTransferModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_log_dto' in d:
            o.bank_log_dto = d['bank_log_dto']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'charge_amount' in d:
            o.charge_amount = d['charge_amount']
        if 'charge_ccy' in d:
            o.charge_ccy = d['charge_ccy']
        if 'crossccy_flag' in d:
            o.crossccy_flag = d['crossccy_flag']
        if 'exchange' in d:
            o.exchange = d['exchange']
        if 'fundlog_source' in d:
            o.fundlog_source = d['fundlog_source']
        if 'id' in d:
            o.id = d['id']
        if 'income_type' in d:
            o.income_type = d['income_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'link_no' in d:
            o.link_no = d['link_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'trading_partner_code' in d:
            o.trading_partner_code = d['trading_partner_code']
        if 'trading_partner_type' in d:
            o.trading_partner_type = d['trading_partner_type']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        return o


