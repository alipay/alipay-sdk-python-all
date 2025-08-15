#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnterpriceSubsidyMsData import EnterpriceSubsidyMsData


class EnterpriceSubsidyData(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._fail_reason = None
        self._mdtrt_id = None
        self._ms_data = None
        self._name = None
        self._offset_amount = None
        self._order_id = None
        self._pay_account = None
        self._pay_account_type = None
        self._pay_amount = None
        self._pay_fund_order_id = None
        self._pay_time = None
        self._setl_id = None
        self._transfer_result = None

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
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
    @property
    def ms_data(self):
        return self._ms_data

    @ms_data.setter
    def ms_data(self, value):
        if isinstance(value, EnterpriceSubsidyMsData):
            self._ms_data = value
        else:
            self._ms_data = EnterpriceSubsidyMsData.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def offset_amount(self):
        return self._offset_amount

    @offset_amount.setter
    def offset_amount(self, value):
        self._offset_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_account_type(self):
        return self._pay_account_type

    @pay_account_type.setter
    def pay_account_type(self, value):
        self._pay_account_type = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
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
    def setl_id(self):
        return self._setl_id

    @setl_id.setter
    def setl_id(self, value):
        self._setl_id = value
    @property
    def transfer_result(self):
        return self._transfer_result

    @transfer_result.setter
    def transfer_result(self, value):
        self._transfer_result = value


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
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.mdtrt_id:
            if hasattr(self.mdtrt_id, 'to_alipay_dict'):
                params['mdtrt_id'] = self.mdtrt_id.to_alipay_dict()
            else:
                params['mdtrt_id'] = self.mdtrt_id
        if self.ms_data:
            if hasattr(self.ms_data, 'to_alipay_dict'):
                params['ms_data'] = self.ms_data.to_alipay_dict()
            else:
                params['ms_data'] = self.ms_data
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.offset_amount:
            if hasattr(self.offset_amount, 'to_alipay_dict'):
                params['offset_amount'] = self.offset_amount.to_alipay_dict()
            else:
                params['offset_amount'] = self.offset_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_account_type:
            if hasattr(self.pay_account_type, 'to_alipay_dict'):
                params['pay_account_type'] = self.pay_account_type.to_alipay_dict()
            else:
                params['pay_account_type'] = self.pay_account_type
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
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
        if self.setl_id:
            if hasattr(self.setl_id, 'to_alipay_dict'):
                params['setl_id'] = self.setl_id.to_alipay_dict()
            else:
                params['setl_id'] = self.setl_id
        if self.transfer_result:
            if hasattr(self.transfer_result, 'to_alipay_dict'):
                params['transfer_result'] = self.transfer_result.to_alipay_dict()
            else:
                params['transfer_result'] = self.transfer_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriceSubsidyData()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'mdtrt_id' in d:
            o.mdtrt_id = d['mdtrt_id']
        if 'ms_data' in d:
            o.ms_data = d['ms_data']
        if 'name' in d:
            o.name = d['name']
        if 'offset_amount' in d:
            o.offset_amount = d['offset_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_account_type' in d:
            o.pay_account_type = d['pay_account_type']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_fund_order_id' in d:
            o.pay_fund_order_id = d['pay_fund_order_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'setl_id' in d:
            o.setl_id = d['setl_id']
        if 'transfer_result' in d:
            o.transfer_result = d['transfer_result']
        return o


