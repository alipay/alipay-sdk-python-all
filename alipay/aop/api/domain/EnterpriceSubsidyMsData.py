#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriceSubsidyMsData(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._claim_no = None
        self._claim_time = None
        self._company_name = None
        self._cur_company_id = None
        self._father_company_id = None
        self._father_company_name = None
        self._mdtrt_id = None
        self._medical_org_id = None
        self._medical_org_name = None
        self._name = None
        self._pay_fund_order_id = None
        self._pay_time = None
        self._residue_amount = None
        self._setl_id = None
        self._total_claim_amount = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_time(self):
        return self._claim_time

    @claim_time.setter
    def claim_time(self, value):
        self._claim_time = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def cur_company_id(self):
        return self._cur_company_id

    @cur_company_id.setter
    def cur_company_id(self, value):
        self._cur_company_id = value
    @property
    def father_company_id(self):
        return self._father_company_id

    @father_company_id.setter
    def father_company_id(self, value):
        self._father_company_id = value
    @property
    def father_company_name(self):
        return self._father_company_name

    @father_company_name.setter
    def father_company_name(self, value):
        self._father_company_name = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def residue_amount(self):
        return self._residue_amount

    @residue_amount.setter
    def residue_amount(self, value):
        self._residue_amount = value
    @property
    def setl_id(self):
        return self._setl_id

    @setl_id.setter
    def setl_id(self, value):
        self._setl_id = value
    @property
    def total_claim_amount(self):
        return self._total_claim_amount

    @total_claim_amount.setter
    def total_claim_amount(self, value):
        self._total_claim_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_time:
            if hasattr(self.claim_time, 'to_alipay_dict'):
                params['claim_time'] = self.claim_time.to_alipay_dict()
            else:
                params['claim_time'] = self.claim_time
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.cur_company_id:
            if hasattr(self.cur_company_id, 'to_alipay_dict'):
                params['cur_company_id'] = self.cur_company_id.to_alipay_dict()
            else:
                params['cur_company_id'] = self.cur_company_id
        if self.father_company_id:
            if hasattr(self.father_company_id, 'to_alipay_dict'):
                params['father_company_id'] = self.father_company_id.to_alipay_dict()
            else:
                params['father_company_id'] = self.father_company_id
        if self.father_company_name:
            if hasattr(self.father_company_name, 'to_alipay_dict'):
                params['father_company_name'] = self.father_company_name.to_alipay_dict()
            else:
                params['father_company_name'] = self.father_company_name
        if self.mdtrt_id:
            if hasattr(self.mdtrt_id, 'to_alipay_dict'):
                params['mdtrt_id'] = self.mdtrt_id.to_alipay_dict()
            else:
                params['mdtrt_id'] = self.mdtrt_id
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pay_fund_order_id:
            if hasattr(self.pay_fund_order_id, 'to_alipay_dict'):
                params['pay_fund_order_id'] = self.pay_fund_order_id.to_alipay_dict()
            else:
                params['pay_fund_order_id'] = self.pay_fund_order_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.residue_amount:
            if hasattr(self.residue_amount, 'to_alipay_dict'):
                params['residue_amount'] = self.residue_amount.to_alipay_dict()
            else:
                params['residue_amount'] = self.residue_amount
        if self.setl_id:
            if hasattr(self.setl_id, 'to_alipay_dict'):
                params['setl_id'] = self.setl_id.to_alipay_dict()
            else:
                params['setl_id'] = self.setl_id
        if self.total_claim_amount:
            if hasattr(self.total_claim_amount, 'to_alipay_dict'):
                params['total_claim_amount'] = self.total_claim_amount.to_alipay_dict()
            else:
                params['total_claim_amount'] = self.total_claim_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriceSubsidyMsData()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_time' in d:
            o.claim_time = d['claim_time']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'cur_company_id' in d:
            o.cur_company_id = d['cur_company_id']
        if 'father_company_id' in d:
            o.father_company_id = d['father_company_id']
        if 'father_company_name' in d:
            o.father_company_name = d['father_company_name']
        if 'mdtrt_id' in d:
            o.mdtrt_id = d['mdtrt_id']
        if 'medical_org_id' in d:
            o.medical_org_id = d['medical_org_id']
        if 'medical_org_name' in d:
            o.medical_org_name = d['medical_org_name']
        if 'name' in d:
            o.name = d['name']
        if 'pay_fund_order_id' in d:
            o.pay_fund_order_id = d['pay_fund_order_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'residue_amount' in d:
            o.residue_amount = d['residue_amount']
        if 'setl_id' in d:
            o.setl_id = d['setl_id']
        if 'total_claim_amount' in d:
            o.total_claim_amount = d['total_claim_amount']
        return o


