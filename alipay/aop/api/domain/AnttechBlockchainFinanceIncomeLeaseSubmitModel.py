#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Leaseholds import Leaseholds
from alipay.aop.api.domain.RelatedParties import RelatedParties


class AnttechBlockchainFinanceIncomeLeaseSubmitModel(object):

    def __init__(self):
        self._biz_no = None
        self._distribution_pro_no = None
        self._lease_contract_file_id = None
        self._lease_contract_no = None
        self._leaseholds = None
        self._related_parties = None
        self._rent_per_period_amount = None
        self._rent_settlement_period = None
        self._rent_settlement_period_unit = None
        self._rent_settlement_type = None
        self._rent_summary_amount = None
        self._trade_effect_time = None
        self._trade_expired_time = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def lease_contract_file_id(self):
        return self._lease_contract_file_id

    @lease_contract_file_id.setter
    def lease_contract_file_id(self, value):
        self._lease_contract_file_id = value
    @property
    def lease_contract_no(self):
        return self._lease_contract_no

    @lease_contract_no.setter
    def lease_contract_no(self, value):
        self._lease_contract_no = value
    @property
    def leaseholds(self):
        return self._leaseholds

    @leaseholds.setter
    def leaseholds(self, value):
        if isinstance(value, list):
            self._leaseholds = list()
            for i in value:
                if isinstance(i, Leaseholds):
                    self._leaseholds.append(i)
                else:
                    self._leaseholds.append(Leaseholds.from_alipay_dict(i))
    @property
    def related_parties(self):
        return self._related_parties

    @related_parties.setter
    def related_parties(self, value):
        if isinstance(value, list):
            self._related_parties = list()
            for i in value:
                if isinstance(i, RelatedParties):
                    self._related_parties.append(i)
                else:
                    self._related_parties.append(RelatedParties.from_alipay_dict(i))
    @property
    def rent_per_period_amount(self):
        return self._rent_per_period_amount

    @rent_per_period_amount.setter
    def rent_per_period_amount(self, value):
        self._rent_per_period_amount = value
    @property
    def rent_settlement_period(self):
        return self._rent_settlement_period

    @rent_settlement_period.setter
    def rent_settlement_period(self, value):
        self._rent_settlement_period = value
    @property
    def rent_settlement_period_unit(self):
        return self._rent_settlement_period_unit

    @rent_settlement_period_unit.setter
    def rent_settlement_period_unit(self, value):
        self._rent_settlement_period_unit = value
    @property
    def rent_settlement_type(self):
        return self._rent_settlement_type

    @rent_settlement_type.setter
    def rent_settlement_type(self, value):
        self._rent_settlement_type = value
    @property
    def rent_summary_amount(self):
        return self._rent_summary_amount

    @rent_summary_amount.setter
    def rent_summary_amount(self, value):
        self._rent_summary_amount = value
    @property
    def trade_effect_time(self):
        return self._trade_effect_time

    @trade_effect_time.setter
    def trade_effect_time(self, value):
        self._trade_effect_time = value
    @property
    def trade_expired_time(self):
        return self._trade_expired_time

    @trade_expired_time.setter
    def trade_expired_time(self, value):
        self._trade_expired_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.lease_contract_file_id:
            if hasattr(self.lease_contract_file_id, 'to_alipay_dict'):
                params['lease_contract_file_id'] = self.lease_contract_file_id.to_alipay_dict()
            else:
                params['lease_contract_file_id'] = self.lease_contract_file_id
        if self.lease_contract_no:
            if hasattr(self.lease_contract_no, 'to_alipay_dict'):
                params['lease_contract_no'] = self.lease_contract_no.to_alipay_dict()
            else:
                params['lease_contract_no'] = self.lease_contract_no
        if self.leaseholds:
            if isinstance(self.leaseholds, list):
                for i in range(0, len(self.leaseholds)):
                    element = self.leaseholds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leaseholds[i] = element.to_alipay_dict()
            if hasattr(self.leaseholds, 'to_alipay_dict'):
                params['leaseholds'] = self.leaseholds.to_alipay_dict()
            else:
                params['leaseholds'] = self.leaseholds
        if self.related_parties:
            if isinstance(self.related_parties, list):
                for i in range(0, len(self.related_parties)):
                    element = self.related_parties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_parties[i] = element.to_alipay_dict()
            if hasattr(self.related_parties, 'to_alipay_dict'):
                params['related_parties'] = self.related_parties.to_alipay_dict()
            else:
                params['related_parties'] = self.related_parties
        if self.rent_per_period_amount:
            if hasattr(self.rent_per_period_amount, 'to_alipay_dict'):
                params['rent_per_period_amount'] = self.rent_per_period_amount.to_alipay_dict()
            else:
                params['rent_per_period_amount'] = self.rent_per_period_amount
        if self.rent_settlement_period:
            if hasattr(self.rent_settlement_period, 'to_alipay_dict'):
                params['rent_settlement_period'] = self.rent_settlement_period.to_alipay_dict()
            else:
                params['rent_settlement_period'] = self.rent_settlement_period
        if self.rent_settlement_period_unit:
            if hasattr(self.rent_settlement_period_unit, 'to_alipay_dict'):
                params['rent_settlement_period_unit'] = self.rent_settlement_period_unit.to_alipay_dict()
            else:
                params['rent_settlement_period_unit'] = self.rent_settlement_period_unit
        if self.rent_settlement_type:
            if hasattr(self.rent_settlement_type, 'to_alipay_dict'):
                params['rent_settlement_type'] = self.rent_settlement_type.to_alipay_dict()
            else:
                params['rent_settlement_type'] = self.rent_settlement_type
        if self.rent_summary_amount:
            if hasattr(self.rent_summary_amount, 'to_alipay_dict'):
                params['rent_summary_amount'] = self.rent_summary_amount.to_alipay_dict()
            else:
                params['rent_summary_amount'] = self.rent_summary_amount
        if self.trade_effect_time:
            if hasattr(self.trade_effect_time, 'to_alipay_dict'):
                params['trade_effect_time'] = self.trade_effect_time.to_alipay_dict()
            else:
                params['trade_effect_time'] = self.trade_effect_time
        if self.trade_expired_time:
            if hasattr(self.trade_expired_time, 'to_alipay_dict'):
                params['trade_expired_time'] = self.trade_expired_time.to_alipay_dict()
            else:
                params['trade_expired_time'] = self.trade_expired_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceIncomeLeaseSubmitModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'lease_contract_file_id' in d:
            o.lease_contract_file_id = d['lease_contract_file_id']
        if 'lease_contract_no' in d:
            o.lease_contract_no = d['lease_contract_no']
        if 'leaseholds' in d:
            o.leaseholds = d['leaseholds']
        if 'related_parties' in d:
            o.related_parties = d['related_parties']
        if 'rent_per_period_amount' in d:
            o.rent_per_period_amount = d['rent_per_period_amount']
        if 'rent_settlement_period' in d:
            o.rent_settlement_period = d['rent_settlement_period']
        if 'rent_settlement_period_unit' in d:
            o.rent_settlement_period_unit = d['rent_settlement_period_unit']
        if 'rent_settlement_type' in d:
            o.rent_settlement_type = d['rent_settlement_type']
        if 'rent_summary_amount' in d:
            o.rent_summary_amount = d['rent_summary_amount']
        if 'trade_effect_time' in d:
            o.trade_effect_time = d['trade_effect_time']
        if 'trade_expired_time' in d:
            o.trade_expired_time = d['trade_expired_time']
        return o


