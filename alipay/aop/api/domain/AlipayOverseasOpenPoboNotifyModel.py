#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVPoboBeneficiaryInfo import TuitionISVPoboBeneficiaryInfo
from alipay.aop.api.domain.TuitionISVPoboBuyerInfo import TuitionISVPoboBuyerInfo
from alipay.aop.api.domain.IndrPoboManualOperationApplyRequestDTO import IndrPoboManualOperationApplyRequestDTO
from alipay.aop.api.domain.TuitionISVPoboPaymentInfo import TuitionISVPoboPaymentInfo
from alipay.aop.api.domain.TuitionISVPoboPaymentResult import TuitionISVPoboPaymentResult


class AlipayOverseasOpenPoboNotifyModel(object):

    def __init__(self):
        self._beneficiary_info = None
        self._buyer_info = None
        self._manual_operation_apply = None
        self._order_id = None
        self._payment_info = None
        self._payment_result = None

    @property
    def beneficiary_info(self):
        return self._beneficiary_info

    @beneficiary_info.setter
    def beneficiary_info(self, value):
        if isinstance(value, TuitionISVPoboBeneficiaryInfo):
            self._beneficiary_info = value
        else:
            self._beneficiary_info = TuitionISVPoboBeneficiaryInfo.from_alipay_dict(value)
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, TuitionISVPoboBuyerInfo):
            self._buyer_info = value
        else:
            self._buyer_info = TuitionISVPoboBuyerInfo.from_alipay_dict(value)
    @property
    def manual_operation_apply(self):
        return self._manual_operation_apply

    @manual_operation_apply.setter
    def manual_operation_apply(self, value):
        if isinstance(value, IndrPoboManualOperationApplyRequestDTO):
            self._manual_operation_apply = value
        else:
            self._manual_operation_apply = IndrPoboManualOperationApplyRequestDTO.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payment_info(self):
        return self._payment_info

    @payment_info.setter
    def payment_info(self, value):
        if isinstance(value, TuitionISVPoboPaymentInfo):
            self._payment_info = value
        else:
            self._payment_info = TuitionISVPoboPaymentInfo.from_alipay_dict(value)
    @property
    def payment_result(self):
        return self._payment_result

    @payment_result.setter
    def payment_result(self, value):
        if isinstance(value, TuitionISVPoboPaymentResult):
            self._payment_result = value
        else:
            self._payment_result = TuitionISVPoboPaymentResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_info:
            if hasattr(self.beneficiary_info, 'to_alipay_dict'):
                params['beneficiary_info'] = self.beneficiary_info.to_alipay_dict()
            else:
                params['beneficiary_info'] = self.beneficiary_info
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.manual_operation_apply:
            if hasattr(self.manual_operation_apply, 'to_alipay_dict'):
                params['manual_operation_apply'] = self.manual_operation_apply.to_alipay_dict()
            else:
                params['manual_operation_apply'] = self.manual_operation_apply
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payment_info:
            if hasattr(self.payment_info, 'to_alipay_dict'):
                params['payment_info'] = self.payment_info.to_alipay_dict()
            else:
                params['payment_info'] = self.payment_info
        if self.payment_result:
            if hasattr(self.payment_result, 'to_alipay_dict'):
                params['payment_result'] = self.payment_result.to_alipay_dict()
            else:
                params['payment_result'] = self.payment_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenPoboNotifyModel()
        if 'beneficiary_info' in d:
            o.beneficiary_info = d['beneficiary_info']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'manual_operation_apply' in d:
            o.manual_operation_apply = d['manual_operation_apply']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payment_info' in d:
            o.payment_info = d['payment_info']
        if 'payment_result' in d:
            o.payment_result = d['payment_result']
        return o


