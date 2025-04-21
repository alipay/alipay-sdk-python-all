#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtendData import ExtendData
from alipay.aop.api.domain.ExtendData import ExtendData


class AlipayCommerceMedicalMisetorderInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMisetorderInfoQueryResponse, self).__init__()
        self._cert_no = None
        self._clr_optins = None
        self._clr_type = None
        self._insuplc_admdvs = None
        self._insutype = None
        self._mdtrt_id = None
        self._med_type = None
        self._medfee_sumamt = None
        self._mi_personal_amt = None
        self._mi_pool_amt = None
        self._pay_settle_info = None
        self._psn_cash_pay = None
        self._psn_cert_type = None
        self._psn_name = None
        self._psn_no = None
        self._refund_set_id = None
        self._refund_set_time = None
        self._refund_settle_info = None
        self._set_id = None
        self._set_time = None
        self._store_mi_code = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def clr_optins(self):
        return self._clr_optins

    @clr_optins.setter
    def clr_optins(self, value):
        self._clr_optins = value
    @property
    def clr_type(self):
        return self._clr_type

    @clr_type.setter
    def clr_type(self, value):
        self._clr_type = value
    @property
    def insuplc_admdvs(self):
        return self._insuplc_admdvs

    @insuplc_admdvs.setter
    def insuplc_admdvs(self, value):
        self._insuplc_admdvs = value
    @property
    def insutype(self):
        return self._insutype

    @insutype.setter
    def insutype(self, value):
        self._insutype = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
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
    def mi_personal_amt(self):
        return self._mi_personal_amt

    @mi_personal_amt.setter
    def mi_personal_amt(self, value):
        self._mi_personal_amt = value
    @property
    def mi_pool_amt(self):
        return self._mi_pool_amt

    @mi_pool_amt.setter
    def mi_pool_amt(self, value):
        self._mi_pool_amt = value
    @property
    def pay_settle_info(self):
        return self._pay_settle_info

    @pay_settle_info.setter
    def pay_settle_info(self, value):
        if isinstance(value, ExtendData):
            self._pay_settle_info = value
        else:
            self._pay_settle_info = ExtendData.from_alipay_dict(value)
    @property
    def psn_cash_pay(self):
        return self._psn_cash_pay

    @psn_cash_pay.setter
    def psn_cash_pay(self, value):
        self._psn_cash_pay = value
    @property
    def psn_cert_type(self):
        return self._psn_cert_type

    @psn_cert_type.setter
    def psn_cert_type(self, value):
        self._psn_cert_type = value
    @property
    def psn_name(self):
        return self._psn_name

    @psn_name.setter
    def psn_name(self, value):
        self._psn_name = value
    @property
    def psn_no(self):
        return self._psn_no

    @psn_no.setter
    def psn_no(self, value):
        self._psn_no = value
    @property
    def refund_set_id(self):
        return self._refund_set_id

    @refund_set_id.setter
    def refund_set_id(self, value):
        self._refund_set_id = value
    @property
    def refund_set_time(self):
        return self._refund_set_time

    @refund_set_time.setter
    def refund_set_time(self, value):
        self._refund_set_time = value
    @property
    def refund_settle_info(self):
        return self._refund_settle_info

    @refund_settle_info.setter
    def refund_settle_info(self, value):
        if isinstance(value, ExtendData):
            self._refund_settle_info = value
        else:
            self._refund_settle_info = ExtendData.from_alipay_dict(value)
    @property
    def set_id(self):
        return self._set_id

    @set_id.setter
    def set_id(self, value):
        self._set_id = value
    @property
    def set_time(self):
        return self._set_time

    @set_time.setter
    def set_time(self, value):
        self._set_time = value
    @property
    def store_mi_code(self):
        return self._store_mi_code

    @store_mi_code.setter
    def store_mi_code(self, value):
        self._store_mi_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMisetorderInfoQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'clr_optins' in response:
            self.clr_optins = response['clr_optins']
        if 'clr_type' in response:
            self.clr_type = response['clr_type']
        if 'insuplc_admdvs' in response:
            self.insuplc_admdvs = response['insuplc_admdvs']
        if 'insutype' in response:
            self.insutype = response['insutype']
        if 'mdtrt_id' in response:
            self.mdtrt_id = response['mdtrt_id']
        if 'med_type' in response:
            self.med_type = response['med_type']
        if 'medfee_sumamt' in response:
            self.medfee_sumamt = response['medfee_sumamt']
        if 'mi_personal_amt' in response:
            self.mi_personal_amt = response['mi_personal_amt']
        if 'mi_pool_amt' in response:
            self.mi_pool_amt = response['mi_pool_amt']
        if 'pay_settle_info' in response:
            self.pay_settle_info = response['pay_settle_info']
        if 'psn_cash_pay' in response:
            self.psn_cash_pay = response['psn_cash_pay']
        if 'psn_cert_type' in response:
            self.psn_cert_type = response['psn_cert_type']
        if 'psn_name' in response:
            self.psn_name = response['psn_name']
        if 'psn_no' in response:
            self.psn_no = response['psn_no']
        if 'refund_set_id' in response:
            self.refund_set_id = response['refund_set_id']
        if 'refund_set_time' in response:
            self.refund_set_time = response['refund_set_time']
        if 'refund_settle_info' in response:
            self.refund_settle_info = response['refund_settle_info']
        if 'set_id' in response:
            self.set_id = response['set_id']
        if 'set_time' in response:
            self.set_time = response['set_time']
        if 'store_mi_code' in response:
            self.store_mi_code = response['store_mi_code']
