#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SeltInfoList(object):

    def __init__(self):
        self._advance_pay = None
        self._claim_amount = None
        self._claim_detail = None
        self._claim_status_desc = None
        self._fund_opst_ac_nbr = None
        self._fund_opst_ac_type = None
        self._fund_opst_org_nm = None
        self._personal_pay = None
        self._repay_time = None
        self._selt_id = None
        self._withdraw_no = None

    @property
    def advance_pay(self):
        return self._advance_pay

    @advance_pay.setter
    def advance_pay(self, value):
        self._advance_pay = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_detail(self):
        return self._claim_detail

    @claim_detail.setter
    def claim_detail(self, value):
        self._claim_detail = value
    @property
    def claim_status_desc(self):
        return self._claim_status_desc

    @claim_status_desc.setter
    def claim_status_desc(self, value):
        self._claim_status_desc = value
    @property
    def fund_opst_ac_nbr(self):
        return self._fund_opst_ac_nbr

    @fund_opst_ac_nbr.setter
    def fund_opst_ac_nbr(self, value):
        self._fund_opst_ac_nbr = value
    @property
    def fund_opst_ac_type(self):
        return self._fund_opst_ac_type

    @fund_opst_ac_type.setter
    def fund_opst_ac_type(self, value):
        self._fund_opst_ac_type = value
    @property
    def fund_opst_org_nm(self):
        return self._fund_opst_org_nm

    @fund_opst_org_nm.setter
    def fund_opst_org_nm(self, value):
        self._fund_opst_org_nm = value
    @property
    def personal_pay(self):
        return self._personal_pay

    @personal_pay.setter
    def personal_pay(self, value):
        self._personal_pay = value
    @property
    def repay_time(self):
        return self._repay_time

    @repay_time.setter
    def repay_time(self, value):
        self._repay_time = value
    @property
    def selt_id(self):
        return self._selt_id

    @selt_id.setter
    def selt_id(self, value):
        self._selt_id = value
    @property
    def withdraw_no(self):
        return self._withdraw_no

    @withdraw_no.setter
    def withdraw_no(self, value):
        self._withdraw_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_pay:
            if hasattr(self.advance_pay, 'to_alipay_dict'):
                params['advance_pay'] = self.advance_pay.to_alipay_dict()
            else:
                params['advance_pay'] = self.advance_pay
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_detail:
            if hasattr(self.claim_detail, 'to_alipay_dict'):
                params['claim_detail'] = self.claim_detail.to_alipay_dict()
            else:
                params['claim_detail'] = self.claim_detail
        if self.claim_status_desc:
            if hasattr(self.claim_status_desc, 'to_alipay_dict'):
                params['claim_status_desc'] = self.claim_status_desc.to_alipay_dict()
            else:
                params['claim_status_desc'] = self.claim_status_desc
        if self.fund_opst_ac_nbr:
            if hasattr(self.fund_opst_ac_nbr, 'to_alipay_dict'):
                params['fund_opst_ac_nbr'] = self.fund_opst_ac_nbr.to_alipay_dict()
            else:
                params['fund_opst_ac_nbr'] = self.fund_opst_ac_nbr
        if self.fund_opst_ac_type:
            if hasattr(self.fund_opst_ac_type, 'to_alipay_dict'):
                params['fund_opst_ac_type'] = self.fund_opst_ac_type.to_alipay_dict()
            else:
                params['fund_opst_ac_type'] = self.fund_opst_ac_type
        if self.fund_opst_org_nm:
            if hasattr(self.fund_opst_org_nm, 'to_alipay_dict'):
                params['fund_opst_org_nm'] = self.fund_opst_org_nm.to_alipay_dict()
            else:
                params['fund_opst_org_nm'] = self.fund_opst_org_nm
        if self.personal_pay:
            if hasattr(self.personal_pay, 'to_alipay_dict'):
                params['personal_pay'] = self.personal_pay.to_alipay_dict()
            else:
                params['personal_pay'] = self.personal_pay
        if self.repay_time:
            if hasattr(self.repay_time, 'to_alipay_dict'):
                params['repay_time'] = self.repay_time.to_alipay_dict()
            else:
                params['repay_time'] = self.repay_time
        if self.selt_id:
            if hasattr(self.selt_id, 'to_alipay_dict'):
                params['selt_id'] = self.selt_id.to_alipay_dict()
            else:
                params['selt_id'] = self.selt_id
        if self.withdraw_no:
            if hasattr(self.withdraw_no, 'to_alipay_dict'):
                params['withdraw_no'] = self.withdraw_no.to_alipay_dict()
            else:
                params['withdraw_no'] = self.withdraw_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SeltInfoList()
        if 'advance_pay' in d:
            o.advance_pay = d['advance_pay']
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_detail' in d:
            o.claim_detail = d['claim_detail']
        if 'claim_status_desc' in d:
            o.claim_status_desc = d['claim_status_desc']
        if 'fund_opst_ac_nbr' in d:
            o.fund_opst_ac_nbr = d['fund_opst_ac_nbr']
        if 'fund_opst_ac_type' in d:
            o.fund_opst_ac_type = d['fund_opst_ac_type']
        if 'fund_opst_org_nm' in d:
            o.fund_opst_org_nm = d['fund_opst_org_nm']
        if 'personal_pay' in d:
            o.personal_pay = d['personal_pay']
        if 'repay_time' in d:
            o.repay_time = d['repay_time']
        if 'selt_id' in d:
            o.selt_id = d['selt_id']
        if 'withdraw_no' in d:
            o.withdraw_no = d['withdraw_no']
        return o


