#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPeriod import RentPeriod
from alipay.aop.api.domain.RentFile import RentFile


class RentFinancingExtInfo(object):

    def __init__(self):
        self._financing_amount = None
        self._financing_period = None
        self._financing_rate = None
        self._financing_rent_protocol = None
        self._fundraiser_id = None
        self._fundraiser_name = None
        self._fundraiser_open_id = None
        self._invest_id = None
        self._invest_open_id = None
        self._payee_account = None
        self._payee_account_open_id = None
        self._payee_memo = None
        self._repayment_type = None

    @property
    def financing_amount(self):
        return self._financing_amount

    @financing_amount.setter
    def financing_amount(self, value):
        self._financing_amount = value
    @property
    def financing_period(self):
        return self._financing_period

    @financing_period.setter
    def financing_period(self, value):
        if isinstance(value, RentPeriod):
            self._financing_period = value
        else:
            self._financing_period = RentPeriod.from_alipay_dict(value)
    @property
    def financing_rate(self):
        return self._financing_rate

    @financing_rate.setter
    def financing_rate(self, value):
        self._financing_rate = value
    @property
    def financing_rent_protocol(self):
        return self._financing_rent_protocol

    @financing_rent_protocol.setter
    def financing_rent_protocol(self, value):
        if isinstance(value, RentFile):
            self._financing_rent_protocol = value
        else:
            self._financing_rent_protocol = RentFile.from_alipay_dict(value)
    @property
    def fundraiser_id(self):
        return self._fundraiser_id

    @fundraiser_id.setter
    def fundraiser_id(self, value):
        self._fundraiser_id = value
    @property
    def fundraiser_name(self):
        return self._fundraiser_name

    @fundraiser_name.setter
    def fundraiser_name(self, value):
        self._fundraiser_name = value
    @property
    def fundraiser_open_id(self):
        return self._fundraiser_open_id

    @fundraiser_open_id.setter
    def fundraiser_open_id(self, value):
        self._fundraiser_open_id = value
    @property
    def invest_id(self):
        return self._invest_id

    @invest_id.setter
    def invest_id(self, value):
        self._invest_id = value
    @property
    def invest_open_id(self):
        return self._invest_open_id

    @invest_open_id.setter
    def invest_open_id(self, value):
        self._invest_open_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_account_open_id(self):
        return self._payee_account_open_id

    @payee_account_open_id.setter
    def payee_account_open_id(self, value):
        self._payee_account_open_id = value
    @property
    def payee_memo(self):
        return self._payee_memo

    @payee_memo.setter
    def payee_memo(self, value):
        self._payee_memo = value
    @property
    def repayment_type(self):
        return self._repayment_type

    @repayment_type.setter
    def repayment_type(self, value):
        self._repayment_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.financing_amount:
            if hasattr(self.financing_amount, 'to_alipay_dict'):
                params['financing_amount'] = self.financing_amount.to_alipay_dict()
            else:
                params['financing_amount'] = self.financing_amount
        if self.financing_period:
            if hasattr(self.financing_period, 'to_alipay_dict'):
                params['financing_period'] = self.financing_period.to_alipay_dict()
            else:
                params['financing_period'] = self.financing_period
        if self.financing_rate:
            if hasattr(self.financing_rate, 'to_alipay_dict'):
                params['financing_rate'] = self.financing_rate.to_alipay_dict()
            else:
                params['financing_rate'] = self.financing_rate
        if self.financing_rent_protocol:
            if hasattr(self.financing_rent_protocol, 'to_alipay_dict'):
                params['financing_rent_protocol'] = self.financing_rent_protocol.to_alipay_dict()
            else:
                params['financing_rent_protocol'] = self.financing_rent_protocol
        if self.fundraiser_id:
            if hasattr(self.fundraiser_id, 'to_alipay_dict'):
                params['fundraiser_id'] = self.fundraiser_id.to_alipay_dict()
            else:
                params['fundraiser_id'] = self.fundraiser_id
        if self.fundraiser_name:
            if hasattr(self.fundraiser_name, 'to_alipay_dict'):
                params['fundraiser_name'] = self.fundraiser_name.to_alipay_dict()
            else:
                params['fundraiser_name'] = self.fundraiser_name
        if self.fundraiser_open_id:
            if hasattr(self.fundraiser_open_id, 'to_alipay_dict'):
                params['fundraiser_open_id'] = self.fundraiser_open_id.to_alipay_dict()
            else:
                params['fundraiser_open_id'] = self.fundraiser_open_id
        if self.invest_id:
            if hasattr(self.invest_id, 'to_alipay_dict'):
                params['invest_id'] = self.invest_id.to_alipay_dict()
            else:
                params['invest_id'] = self.invest_id
        if self.invest_open_id:
            if hasattr(self.invest_open_id, 'to_alipay_dict'):
                params['invest_open_id'] = self.invest_open_id.to_alipay_dict()
            else:
                params['invest_open_id'] = self.invest_open_id
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_account_open_id:
            if hasattr(self.payee_account_open_id, 'to_alipay_dict'):
                params['payee_account_open_id'] = self.payee_account_open_id.to_alipay_dict()
            else:
                params['payee_account_open_id'] = self.payee_account_open_id
        if self.payee_memo:
            if hasattr(self.payee_memo, 'to_alipay_dict'):
                params['payee_memo'] = self.payee_memo.to_alipay_dict()
            else:
                params['payee_memo'] = self.payee_memo
        if self.repayment_type:
            if hasattr(self.repayment_type, 'to_alipay_dict'):
                params['repayment_type'] = self.repayment_type.to_alipay_dict()
            else:
                params['repayment_type'] = self.repayment_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentFinancingExtInfo()
        if 'financing_amount' in d:
            o.financing_amount = d['financing_amount']
        if 'financing_period' in d:
            o.financing_period = d['financing_period']
        if 'financing_rate' in d:
            o.financing_rate = d['financing_rate']
        if 'financing_rent_protocol' in d:
            o.financing_rent_protocol = d['financing_rent_protocol']
        if 'fundraiser_id' in d:
            o.fundraiser_id = d['fundraiser_id']
        if 'fundraiser_name' in d:
            o.fundraiser_name = d['fundraiser_name']
        if 'fundraiser_open_id' in d:
            o.fundraiser_open_id = d['fundraiser_open_id']
        if 'invest_id' in d:
            o.invest_id = d['invest_id']
        if 'invest_open_id' in d:
            o.invest_open_id = d['invest_open_id']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_account_open_id' in d:
            o.payee_account_open_id = d['payee_account_open_id']
        if 'payee_memo' in d:
            o.payee_memo = d['payee_memo']
        if 'repayment_type' in d:
            o.repayment_type = d['repayment_type']
        return o


