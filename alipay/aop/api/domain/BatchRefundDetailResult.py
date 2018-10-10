#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundRoyaltyResult import RefundRoyaltyResult
from alipay.aop.api.domain.RefundUnfreezeResult import RefundUnfreezeResult


class BatchRefundDetailResult(object):

    def __init__(self):
        self._batch_no = None
        self._dback_status = None
        self._est_bank_ack_time = None
        self._est_bank_receipt_time = None
        self._has_deposit_back = None
        self._refund_amount = None
        self._refund_bank_name = None
        self._refund_royaltys = None
        self._refund_suppl_amount = None
        self._refund_suppl_result_code = None
        self._rest_suppl_amount = None
        self._result_code = None
        self._trade_no = None
        self._unfreeze_details = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def dback_status(self):
        return self._dback_status

    @dback_status.setter
    def dback_status(self, value):
        self._dback_status = value
    @property
    def est_bank_ack_time(self):
        return self._est_bank_ack_time

    @est_bank_ack_time.setter
    def est_bank_ack_time(self, value):
        self._est_bank_ack_time = value
    @property
    def est_bank_receipt_time(self):
        return self._est_bank_receipt_time

    @est_bank_receipt_time.setter
    def est_bank_receipt_time(self, value):
        self._est_bank_receipt_time = value
    @property
    def has_deposit_back(self):
        return self._has_deposit_back

    @has_deposit_back.setter
    def has_deposit_back(self, value):
        self._has_deposit_back = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_bank_name(self):
        return self._refund_bank_name

    @refund_bank_name.setter
    def refund_bank_name(self, value):
        self._refund_bank_name = value
    @property
    def refund_royaltys(self):
        return self._refund_royaltys

    @refund_royaltys.setter
    def refund_royaltys(self, value):
        if isinstance(value, list):
            self._refund_royaltys = list()
            for i in value:
                if isinstance(i, RefundRoyaltyResult):
                    self._refund_royaltys.append(i)
                else:
                    self._refund_royaltys.append(RefundRoyaltyResult.from_alipay_dict(i))
    @property
    def refund_suppl_amount(self):
        return self._refund_suppl_amount

    @refund_suppl_amount.setter
    def refund_suppl_amount(self, value):
        self._refund_suppl_amount = value
    @property
    def refund_suppl_result_code(self):
        return self._refund_suppl_result_code

    @refund_suppl_result_code.setter
    def refund_suppl_result_code(self, value):
        self._refund_suppl_result_code = value
    @property
    def rest_suppl_amount(self):
        return self._rest_suppl_amount

    @rest_suppl_amount.setter
    def rest_suppl_amount(self, value):
        self._rest_suppl_amount = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def unfreeze_details(self):
        return self._unfreeze_details

    @unfreeze_details.setter
    def unfreeze_details(self, value):
        if isinstance(value, RefundUnfreezeResult):
            self._unfreeze_details = value
        else:
            self._unfreeze_details = RefundUnfreezeResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.dback_status:
            if hasattr(self.dback_status, 'to_alipay_dict'):
                params['dback_status'] = self.dback_status.to_alipay_dict()
            else:
                params['dback_status'] = self.dback_status
        if self.est_bank_ack_time:
            if hasattr(self.est_bank_ack_time, 'to_alipay_dict'):
                params['est_bank_ack_time'] = self.est_bank_ack_time.to_alipay_dict()
            else:
                params['est_bank_ack_time'] = self.est_bank_ack_time
        if self.est_bank_receipt_time:
            if hasattr(self.est_bank_receipt_time, 'to_alipay_dict'):
                params['est_bank_receipt_time'] = self.est_bank_receipt_time.to_alipay_dict()
            else:
                params['est_bank_receipt_time'] = self.est_bank_receipt_time
        if self.has_deposit_back:
            if hasattr(self.has_deposit_back, 'to_alipay_dict'):
                params['has_deposit_back'] = self.has_deposit_back.to_alipay_dict()
            else:
                params['has_deposit_back'] = self.has_deposit_back
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_bank_name:
            if hasattr(self.refund_bank_name, 'to_alipay_dict'):
                params['refund_bank_name'] = self.refund_bank_name.to_alipay_dict()
            else:
                params['refund_bank_name'] = self.refund_bank_name
        if self.refund_royaltys:
            if isinstance(self.refund_royaltys, list):
                for i in range(0, len(self.refund_royaltys)):
                    element = self.refund_royaltys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_royaltys[i] = element.to_alipay_dict()
            if hasattr(self.refund_royaltys, 'to_alipay_dict'):
                params['refund_royaltys'] = self.refund_royaltys.to_alipay_dict()
            else:
                params['refund_royaltys'] = self.refund_royaltys
        if self.refund_suppl_amount:
            if hasattr(self.refund_suppl_amount, 'to_alipay_dict'):
                params['refund_suppl_amount'] = self.refund_suppl_amount.to_alipay_dict()
            else:
                params['refund_suppl_amount'] = self.refund_suppl_amount
        if self.refund_suppl_result_code:
            if hasattr(self.refund_suppl_result_code, 'to_alipay_dict'):
                params['refund_suppl_result_code'] = self.refund_suppl_result_code.to_alipay_dict()
            else:
                params['refund_suppl_result_code'] = self.refund_suppl_result_code
        if self.rest_suppl_amount:
            if hasattr(self.rest_suppl_amount, 'to_alipay_dict'):
                params['rest_suppl_amount'] = self.rest_suppl_amount.to_alipay_dict()
            else:
                params['rest_suppl_amount'] = self.rest_suppl_amount
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.unfreeze_details:
            if hasattr(self.unfreeze_details, 'to_alipay_dict'):
                params['unfreeze_details'] = self.unfreeze_details.to_alipay_dict()
            else:
                params['unfreeze_details'] = self.unfreeze_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchRefundDetailResult()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'dback_status' in d:
            o.dback_status = d['dback_status']
        if 'est_bank_ack_time' in d:
            o.est_bank_ack_time = d['est_bank_ack_time']
        if 'est_bank_receipt_time' in d:
            o.est_bank_receipt_time = d['est_bank_receipt_time']
        if 'has_deposit_back' in d:
            o.has_deposit_back = d['has_deposit_back']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_bank_name' in d:
            o.refund_bank_name = d['refund_bank_name']
        if 'refund_royaltys' in d:
            o.refund_royaltys = d['refund_royaltys']
        if 'refund_suppl_amount' in d:
            o.refund_suppl_amount = d['refund_suppl_amount']
        if 'refund_suppl_result_code' in d:
            o.refund_suppl_result_code = d['refund_suppl_result_code']
        if 'rest_suppl_amount' in d:
            o.rest_suppl_amount = d['rest_suppl_amount']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'unfreeze_details' in d:
            o.unfreeze_details = d['unfreeze_details']
        return o


