#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimReportSeltInfoModel(object):

    def __init__(self):
        self._acct_pay_amount = None
        self._admission_date = None
        self._cash_pay_amount = None
        self._discharge_ate = None
        self._hifp_pay_amout = None
        self._inquery_id = None
        self._med_type = None
        self._medfee_sumamt = None
        self._medical_org_id = None
        self._medical_org_name = None
        self._medins_type_name = None
        self._othfund_pay_amount = None
        self._self_pay_amount = None
        self._selt_time = None
        self._setl_id = None

    @property
    def acct_pay_amount(self):
        return self._acct_pay_amount

    @acct_pay_amount.setter
    def acct_pay_amount(self, value):
        self._acct_pay_amount = value
    @property
    def admission_date(self):
        return self._admission_date

    @admission_date.setter
    def admission_date(self, value):
        self._admission_date = value
    @property
    def cash_pay_amount(self):
        return self._cash_pay_amount

    @cash_pay_amount.setter
    def cash_pay_amount(self, value):
        self._cash_pay_amount = value
    @property
    def discharge_ate(self):
        return self._discharge_ate

    @discharge_ate.setter
    def discharge_ate(self, value):
        self._discharge_ate = value
    @property
    def hifp_pay_amout(self):
        return self._hifp_pay_amout

    @hifp_pay_amout.setter
    def hifp_pay_amout(self, value):
        self._hifp_pay_amout = value
    @property
    def inquery_id(self):
        return self._inquery_id

    @inquery_id.setter
    def inquery_id(self, value):
        self._inquery_id = value
    @property
    def med_type(self):
        return self._med_type

    @med_type.setter
    def med_type(self, value):
        self._med_type = value
    @property
    def medfee_sumamt(self):
        return self._medfee_sumamt

    @medfee_sumamt.setter
    def medfee_sumamt(self, value):
        self._medfee_sumamt = value
    @property
    def medical_org_id(self):
        return self._medical_org_id

    @medical_org_id.setter
    def medical_org_id(self, value):
        self._medical_org_id = value
    @property
    def medical_org_name(self):
        return self._medical_org_name

    @medical_org_name.setter
    def medical_org_name(self, value):
        self._medical_org_name = value
    @property
    def medins_type_name(self):
        return self._medins_type_name

    @medins_type_name.setter
    def medins_type_name(self, value):
        self._medins_type_name = value
    @property
    def othfund_pay_amount(self):
        return self._othfund_pay_amount

    @othfund_pay_amount.setter
    def othfund_pay_amount(self, value):
        self._othfund_pay_amount = value
    @property
    def self_pay_amount(self):
        return self._self_pay_amount

    @self_pay_amount.setter
    def self_pay_amount(self, value):
        self._self_pay_amount = value
    @property
    def selt_time(self):
        return self._selt_time

    @selt_time.setter
    def selt_time(self, value):
        self._selt_time = value
    @property
    def setl_id(self):
        return self._setl_id

    @setl_id.setter
    def setl_id(self, value):
        self._setl_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acct_pay_amount:
            if hasattr(self.acct_pay_amount, 'to_alipay_dict'):
                params['acct_pay_amount'] = self.acct_pay_amount.to_alipay_dict()
            else:
                params['acct_pay_amount'] = self.acct_pay_amount
        if self.admission_date:
            if hasattr(self.admission_date, 'to_alipay_dict'):
                params['admission_date'] = self.admission_date.to_alipay_dict()
            else:
                params['admission_date'] = self.admission_date
        if self.cash_pay_amount:
            if hasattr(self.cash_pay_amount, 'to_alipay_dict'):
                params['cash_pay_amount'] = self.cash_pay_amount.to_alipay_dict()
            else:
                params['cash_pay_amount'] = self.cash_pay_amount
        if self.discharge_ate:
            if hasattr(self.discharge_ate, 'to_alipay_dict'):
                params['discharge_ate'] = self.discharge_ate.to_alipay_dict()
            else:
                params['discharge_ate'] = self.discharge_ate
        if self.hifp_pay_amout:
            if hasattr(self.hifp_pay_amout, 'to_alipay_dict'):
                params['hifp_pay_amout'] = self.hifp_pay_amout.to_alipay_dict()
            else:
                params['hifp_pay_amout'] = self.hifp_pay_amout
        if self.inquery_id:
            if hasattr(self.inquery_id, 'to_alipay_dict'):
                params['inquery_id'] = self.inquery_id.to_alipay_dict()
            else:
                params['inquery_id'] = self.inquery_id
        if self.med_type:
            if hasattr(self.med_type, 'to_alipay_dict'):
                params['med_type'] = self.med_type.to_alipay_dict()
            else:
                params['med_type'] = self.med_type
        if self.medfee_sumamt:
            if hasattr(self.medfee_sumamt, 'to_alipay_dict'):
                params['medfee_sumamt'] = self.medfee_sumamt.to_alipay_dict()
            else:
                params['medfee_sumamt'] = self.medfee_sumamt
        if self.medical_org_id:
            if hasattr(self.medical_org_id, 'to_alipay_dict'):
                params['medical_org_id'] = self.medical_org_id.to_alipay_dict()
            else:
                params['medical_org_id'] = self.medical_org_id
        if self.medical_org_name:
            if hasattr(self.medical_org_name, 'to_alipay_dict'):
                params['medical_org_name'] = self.medical_org_name.to_alipay_dict()
            else:
                params['medical_org_name'] = self.medical_org_name
        if self.medins_type_name:
            if hasattr(self.medins_type_name, 'to_alipay_dict'):
                params['medins_type_name'] = self.medins_type_name.to_alipay_dict()
            else:
                params['medins_type_name'] = self.medins_type_name
        if self.othfund_pay_amount:
            if hasattr(self.othfund_pay_amount, 'to_alipay_dict'):
                params['othfund_pay_amount'] = self.othfund_pay_amount.to_alipay_dict()
            else:
                params['othfund_pay_amount'] = self.othfund_pay_amount
        if self.self_pay_amount:
            if hasattr(self.self_pay_amount, 'to_alipay_dict'):
                params['self_pay_amount'] = self.self_pay_amount.to_alipay_dict()
            else:
                params['self_pay_amount'] = self.self_pay_amount
        if self.selt_time:
            if hasattr(self.selt_time, 'to_alipay_dict'):
                params['selt_time'] = self.selt_time.to_alipay_dict()
            else:
                params['selt_time'] = self.selt_time
        if self.setl_id:
            if hasattr(self.setl_id, 'to_alipay_dict'):
                params['setl_id'] = self.setl_id.to_alipay_dict()
            else:
                params['setl_id'] = self.setl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimReportSeltInfoModel()
        if 'acct_pay_amount' in d:
            o.acct_pay_amount = d['acct_pay_amount']
        if 'admission_date' in d:
            o.admission_date = d['admission_date']
        if 'cash_pay_amount' in d:
            o.cash_pay_amount = d['cash_pay_amount']
        if 'discharge_ate' in d:
            o.discharge_ate = d['discharge_ate']
        if 'hifp_pay_amout' in d:
            o.hifp_pay_amout = d['hifp_pay_amout']
        if 'inquery_id' in d:
            o.inquery_id = d['inquery_id']
        if 'med_type' in d:
            o.med_type = d['med_type']
        if 'medfee_sumamt' in d:
            o.medfee_sumamt = d['medfee_sumamt']
        if 'medical_org_id' in d:
            o.medical_org_id = d['medical_org_id']
        if 'medical_org_name' in d:
            o.medical_org_name = d['medical_org_name']
        if 'medins_type_name' in d:
            o.medins_type_name = d['medins_type_name']
        if 'othfund_pay_amount' in d:
            o.othfund_pay_amount = d['othfund_pay_amount']
        if 'self_pay_amount' in d:
            o.self_pay_amount = d['self_pay_amount']
        if 'selt_time' in d:
            o.selt_time = d['selt_time']
        if 'setl_id' in d:
            o.setl_id = d['setl_id']
        return o


