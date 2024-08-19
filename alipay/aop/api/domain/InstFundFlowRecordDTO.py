#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstFundFlowRecordDTO(object):

    def __init__(self):
        self._biz_context = None
        self._biz_scene = None
        self._credit_account_no = None
        self._credit_account_type = None
        self._credit_open_id = None
        self._credit_user_id = None
        self._debit_account_no = None
        self._debit_account_type = None
        self._debit_open_id = None
        self._debit_user_id = None
        self._gmt_execute_time = None
        self._out_biz_no = None
        self._pay_result_code = None
        self._pay_result_desc = None
        self._record_type = None
        self._status = None
        self._trans_amount = None
        self._trans_currency = None
        self._unique_no = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def credit_account_no(self):
        return self._credit_account_no

    @credit_account_no.setter
    def credit_account_no(self, value):
        self._credit_account_no = value
    @property
    def credit_account_type(self):
        return self._credit_account_type

    @credit_account_type.setter
    def credit_account_type(self, value):
        self._credit_account_type = value
    @property
    def credit_open_id(self):
        return self._credit_open_id

    @credit_open_id.setter
    def credit_open_id(self, value):
        self._credit_open_id = value
    @property
    def credit_user_id(self):
        return self._credit_user_id

    @credit_user_id.setter
    def credit_user_id(self, value):
        self._credit_user_id = value
    @property
    def debit_account_no(self):
        return self._debit_account_no

    @debit_account_no.setter
    def debit_account_no(self, value):
        self._debit_account_no = value
    @property
    def debit_account_type(self):
        return self._debit_account_type

    @debit_account_type.setter
    def debit_account_type(self, value):
        self._debit_account_type = value
    @property
    def debit_open_id(self):
        return self._debit_open_id

    @debit_open_id.setter
    def debit_open_id(self, value):
        self._debit_open_id = value
    @property
    def debit_user_id(self):
        return self._debit_user_id

    @debit_user_id.setter
    def debit_user_id(self, value):
        self._debit_user_id = value
    @property
    def gmt_execute_time(self):
        return self._gmt_execute_time

    @gmt_execute_time.setter
    def gmt_execute_time(self, value):
        self._gmt_execute_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_result_code(self):
        return self._pay_result_code

    @pay_result_code.setter
    def pay_result_code(self, value):
        self._pay_result_code = value
    @property
    def pay_result_desc(self):
        return self._pay_result_desc

    @pay_result_desc.setter
    def pay_result_desc(self, value):
        self._pay_result_desc = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def unique_no(self):
        return self._unique_no

    @unique_no.setter
    def unique_no(self, value):
        self._unique_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.credit_account_no:
            if hasattr(self.credit_account_no, 'to_alipay_dict'):
                params['credit_account_no'] = self.credit_account_no.to_alipay_dict()
            else:
                params['credit_account_no'] = self.credit_account_no
        if self.credit_account_type:
            if hasattr(self.credit_account_type, 'to_alipay_dict'):
                params['credit_account_type'] = self.credit_account_type.to_alipay_dict()
            else:
                params['credit_account_type'] = self.credit_account_type
        if self.credit_open_id:
            if hasattr(self.credit_open_id, 'to_alipay_dict'):
                params['credit_open_id'] = self.credit_open_id.to_alipay_dict()
            else:
                params['credit_open_id'] = self.credit_open_id
        if self.credit_user_id:
            if hasattr(self.credit_user_id, 'to_alipay_dict'):
                params['credit_user_id'] = self.credit_user_id.to_alipay_dict()
            else:
                params['credit_user_id'] = self.credit_user_id
        if self.debit_account_no:
            if hasattr(self.debit_account_no, 'to_alipay_dict'):
                params['debit_account_no'] = self.debit_account_no.to_alipay_dict()
            else:
                params['debit_account_no'] = self.debit_account_no
        if self.debit_account_type:
            if hasattr(self.debit_account_type, 'to_alipay_dict'):
                params['debit_account_type'] = self.debit_account_type.to_alipay_dict()
            else:
                params['debit_account_type'] = self.debit_account_type
        if self.debit_open_id:
            if hasattr(self.debit_open_id, 'to_alipay_dict'):
                params['debit_open_id'] = self.debit_open_id.to_alipay_dict()
            else:
                params['debit_open_id'] = self.debit_open_id
        if self.debit_user_id:
            if hasattr(self.debit_user_id, 'to_alipay_dict'):
                params['debit_user_id'] = self.debit_user_id.to_alipay_dict()
            else:
                params['debit_user_id'] = self.debit_user_id
        if self.gmt_execute_time:
            if hasattr(self.gmt_execute_time, 'to_alipay_dict'):
                params['gmt_execute_time'] = self.gmt_execute_time.to_alipay_dict()
            else:
                params['gmt_execute_time'] = self.gmt_execute_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_result_code:
            if hasattr(self.pay_result_code, 'to_alipay_dict'):
                params['pay_result_code'] = self.pay_result_code.to_alipay_dict()
            else:
                params['pay_result_code'] = self.pay_result_code
        if self.pay_result_desc:
            if hasattr(self.pay_result_desc, 'to_alipay_dict'):
                params['pay_result_desc'] = self.pay_result_desc.to_alipay_dict()
            else:
                params['pay_result_desc'] = self.pay_result_desc
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        if self.unique_no:
            if hasattr(self.unique_no, 'to_alipay_dict'):
                params['unique_no'] = self.unique_no.to_alipay_dict()
            else:
                params['unique_no'] = self.unique_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstFundFlowRecordDTO()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'credit_account_no' in d:
            o.credit_account_no = d['credit_account_no']
        if 'credit_account_type' in d:
            o.credit_account_type = d['credit_account_type']
        if 'credit_open_id' in d:
            o.credit_open_id = d['credit_open_id']
        if 'credit_user_id' in d:
            o.credit_user_id = d['credit_user_id']
        if 'debit_account_no' in d:
            o.debit_account_no = d['debit_account_no']
        if 'debit_account_type' in d:
            o.debit_account_type = d['debit_account_type']
        if 'debit_open_id' in d:
            o.debit_open_id = d['debit_open_id']
        if 'debit_user_id' in d:
            o.debit_user_id = d['debit_user_id']
        if 'gmt_execute_time' in d:
            o.gmt_execute_time = d['gmt_execute_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_result_code' in d:
            o.pay_result_code = d['pay_result_code']
        if 'pay_result_desc' in d:
            o.pay_result_desc = d['pay_result_desc']
        if 'record_type' in d:
            o.record_type = d['record_type']
        if 'status' in d:
            o.status = d['status']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        if 'unique_no' in d:
            o.unique_no = d['unique_no']
        return o


