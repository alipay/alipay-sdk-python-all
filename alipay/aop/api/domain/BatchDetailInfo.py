#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BatchDetailInfo(object):

    def __init__(self):
        self._batch_no = None
        self._detail_no = None
        self._ext_param = None
        self._fail_message = None
        self._last_modified = None
        self._message = None
        self._pay_amount = None
        self._pay_success_date = None
        self._status = None
        self._transfer_no = None
        self._user_id = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def detail_no(self):
        return self._detail_no

    @detail_no.setter
    def detail_no(self, value):
        self._detail_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_success_date(self):
        return self._pay_success_date

    @pay_success_date.setter
    def pay_success_date(self, value):
        self._pay_success_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.detail_no:
            if hasattr(self.detail_no, 'to_alipay_dict'):
                params['detail_no'] = self.detail_no.to_alipay_dict()
            else:
                params['detail_no'] = self.detail_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        if self.last_modified:
            if hasattr(self.last_modified, 'to_alipay_dict'):
                params['last_modified'] = self.last_modified.to_alipay_dict()
            else:
                params['last_modified'] = self.last_modified
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_success_date:
            if hasattr(self.pay_success_date, 'to_alipay_dict'):
                params['pay_success_date'] = self.pay_success_date.to_alipay_dict()
            else:
                params['pay_success_date'] = self.pay_success_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.transfer_no:
            if hasattr(self.transfer_no, 'to_alipay_dict'):
                params['transfer_no'] = self.transfer_no.to_alipay_dict()
            else:
                params['transfer_no'] = self.transfer_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchDetailInfo()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'detail_no' in d:
            o.detail_no = d['detail_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        if 'last_modified' in d:
            o.last_modified = d['last_modified']
        if 'message' in d:
            o.message = d['message']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_success_date' in d:
            o.pay_success_date = d['pay_success_date']
        if 'status' in d:
            o.status = d['status']
        if 'transfer_no' in d:
            o.transfer_no = d['transfer_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


