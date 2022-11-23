#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundOperationDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._amount = None
        self._close_code = None
        self._close_reason = None
        self._gmt_pay = None
        self._operation_id = None
        self._operation_status = None
        self._operation_type = None
        self._order_title = None
        self._out_request_no = None
        self._principal_account = None
        self._receive_asset = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def close_code(self):
        return self._close_code

    @close_code.setter
    def close_code(self, value):
        self._close_code = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def operation_status(self):
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        self._operation_status = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def principal_account(self):
        return self._principal_account

    @principal_account.setter
    def principal_account(self, value):
        self._principal_account = value
    @property
    def receive_asset(self):
        return self._receive_asset

    @receive_asset.setter
    def receive_asset(self, value):
        self._receive_asset = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.close_code:
            if hasattr(self.close_code, 'to_alipay_dict'):
                params['close_code'] = self.close_code.to_alipay_dict()
            else:
                params['close_code'] = self.close_code
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.operation_id:
            if hasattr(self.operation_id, 'to_alipay_dict'):
                params['operation_id'] = self.operation_id.to_alipay_dict()
            else:
                params['operation_id'] = self.operation_id
        if self.operation_status:
            if hasattr(self.operation_status, 'to_alipay_dict'):
                params['operation_status'] = self.operation_status.to_alipay_dict()
            else:
                params['operation_status'] = self.operation_status
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.principal_account:
            if hasattr(self.principal_account, 'to_alipay_dict'):
                params['principal_account'] = self.principal_account.to_alipay_dict()
            else:
                params['principal_account'] = self.principal_account
        if self.receive_asset:
            if hasattr(self.receive_asset, 'to_alipay_dict'):
                params['receive_asset'] = self.receive_asset.to_alipay_dict()
            else:
                params['receive_asset'] = self.receive_asset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundOperationDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'close_code' in d:
            o.close_code = d['close_code']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'operation_id' in d:
            o.operation_id = d['operation_id']
        if 'operation_status' in d:
            o.operation_status = d['operation_status']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'principal_account' in d:
            o.principal_account = d['principal_account']
        if 'receive_asset' in d:
            o.receive_asset = d['receive_asset']
        return o


