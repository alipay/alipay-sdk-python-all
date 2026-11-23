#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInstanceAmountInfo import CertificateInstanceAmountInfo
from alipay.aop.api.domain.DeductionInfoList import DeductionInfoList
from alipay.aop.api.domain.PayBillInfo import PayBillInfo
from alipay.aop.api.domain.CertificateSkuInfo import CertificateSkuInfo
from alipay.aop.api.domain.CertificateTimesCardInfo import CertificateTimesCardInfo
from alipay.aop.api.domain.CertificateUseRuleInfo import CertificateUseRuleInfo


class CertificateQueryInfo(object):

    def __init__(self):
        self._amount_info = None
        self._can_use = None
        self._certificate_id = None
        self._code = None
        self._deduction_info_list = None
        self._out_order_id = None
        self._pay_bill_info = None
        self._sku_info = None
        self._status = None
        self._times_card_info = None
        self._use_rule_info = None
        self._valid_begin_time = None
        self._valid_end_time = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, CertificateInstanceAmountInfo):
            self._amount_info = value
        else:
            self._amount_info = CertificateInstanceAmountInfo.from_alipay_dict(value)
    @property
    def can_use(self):
        return self._can_use

    @can_use.setter
    def can_use(self, value):
        self._can_use = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def deduction_info_list(self):
        return self._deduction_info_list

    @deduction_info_list.setter
    def deduction_info_list(self, value):
        if isinstance(value, list):
            self._deduction_info_list = list()
            for i in value:
                if isinstance(i, DeductionInfoList):
                    self._deduction_info_list.append(i)
                else:
                    self._deduction_info_list.append(DeductionInfoList.from_alipay_dict(i))
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_bill_info(self):
        return self._pay_bill_info

    @pay_bill_info.setter
    def pay_bill_info(self, value):
        if isinstance(value, PayBillInfo):
            self._pay_bill_info = value
        else:
            self._pay_bill_info = PayBillInfo.from_alipay_dict(value)
    @property
    def sku_info(self):
        return self._sku_info

    @sku_info.setter
    def sku_info(self, value):
        if isinstance(value, CertificateSkuInfo):
            self._sku_info = value
        else:
            self._sku_info = CertificateSkuInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def times_card_info(self):
        return self._times_card_info

    @times_card_info.setter
    def times_card_info(self, value):
        if isinstance(value, CertificateTimesCardInfo):
            self._times_card_info = value
        else:
            self._times_card_info = CertificateTimesCardInfo.from_alipay_dict(value)
    @property
    def use_rule_info(self):
        return self._use_rule_info

    @use_rule_info.setter
    def use_rule_info(self, value):
        if isinstance(value, CertificateUseRuleInfo):
            self._use_rule_info = value
        else:
            self._use_rule_info = CertificateUseRuleInfo.from_alipay_dict(value)
    @property
    def valid_begin_time(self):
        return self._valid_begin_time

    @valid_begin_time.setter
    def valid_begin_time(self, value):
        self._valid_begin_time = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_info:
            if hasattr(self.amount_info, 'to_alipay_dict'):
                params['amount_info'] = self.amount_info.to_alipay_dict()
            else:
                params['amount_info'] = self.amount_info
        if self.can_use:
            if hasattr(self.can_use, 'to_alipay_dict'):
                params['can_use'] = self.can_use.to_alipay_dict()
            else:
                params['can_use'] = self.can_use
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.deduction_info_list:
            if isinstance(self.deduction_info_list, list):
                for i in range(0, len(self.deduction_info_list)):
                    element = self.deduction_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduction_info_list[i] = element.to_alipay_dict()
            if hasattr(self.deduction_info_list, 'to_alipay_dict'):
                params['deduction_info_list'] = self.deduction_info_list.to_alipay_dict()
            else:
                params['deduction_info_list'] = self.deduction_info_list
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.pay_bill_info:
            if hasattr(self.pay_bill_info, 'to_alipay_dict'):
                params['pay_bill_info'] = self.pay_bill_info.to_alipay_dict()
            else:
                params['pay_bill_info'] = self.pay_bill_info
        if self.sku_info:
            if hasattr(self.sku_info, 'to_alipay_dict'):
                params['sku_info'] = self.sku_info.to_alipay_dict()
            else:
                params['sku_info'] = self.sku_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.times_card_info:
            if hasattr(self.times_card_info, 'to_alipay_dict'):
                params['times_card_info'] = self.times_card_info.to_alipay_dict()
            else:
                params['times_card_info'] = self.times_card_info
        if self.use_rule_info:
            if hasattr(self.use_rule_info, 'to_alipay_dict'):
                params['use_rule_info'] = self.use_rule_info.to_alipay_dict()
            else:
                params['use_rule_info'] = self.use_rule_info
        if self.valid_begin_time:
            if hasattr(self.valid_begin_time, 'to_alipay_dict'):
                params['valid_begin_time'] = self.valid_begin_time.to_alipay_dict()
            else:
                params['valid_begin_time'] = self.valid_begin_time
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateQueryInfo()
        if 'amount_info' in d:
            o.amount_info = d['amount_info']
        if 'can_use' in d:
            o.can_use = d['can_use']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'code' in d:
            o.code = d['code']
        if 'deduction_info_list' in d:
            o.deduction_info_list = d['deduction_info_list']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_bill_info' in d:
            o.pay_bill_info = d['pay_bill_info']
        if 'sku_info' in d:
            o.sku_info = d['sku_info']
        if 'status' in d:
            o.status = d['status']
        if 'times_card_info' in d:
            o.times_card_info = d['times_card_info']
        if 'use_rule_info' in d:
            o.use_rule_info = d['use_rule_info']
        if 'valid_begin_time' in d:
            o.valid_begin_time = d['valid_begin_time']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        return o


