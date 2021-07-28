#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertInfo import CertInfo
from alipay.aop.api.domain.ExchangeRate import ExchangeRate
from alipay.aop.api.domain.AccPayeeInfo import AccPayeeInfo


class AccDetailModel(object):

    def __init__(self):
        self._alipay_order_no = None
        self._cert_info = None
        self._detail_id = None
        self._detail_no = None
        self._error_code = None
        self._error_msg = None
        self._exchange_rate = None
        self._gmt_create = None
        self._gmt_finish = None
        self._need_retry = None
        self._out_biz_no = None
        self._payee_info = None
        self._payment_amount = None
        self._payment_currency = None
        self._remark = None
        self._settlement_amount = None
        self._settlement_currency = None
        self._status = None
        self._sub_status = None
        self._trans_amount = None
        self._trans_currency = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def cert_info(self):
        return self._cert_info

    @cert_info.setter
    def cert_info(self, value):
        if isinstance(value, CertInfo):
            self._cert_info = value
        else:
            self._cert_info = CertInfo.from_alipay_dict(value)
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def detail_no(self):
        return self._detail_no

    @detail_no.setter
    def detail_no(self, value):
        self._detail_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        if isinstance(value, ExchangeRate):
            self._exchange_rate = value
        else:
            self._exchange_rate = ExchangeRate.from_alipay_dict(value)
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_finish(self):
        return self._gmt_finish

    @gmt_finish.setter
    def gmt_finish(self, value):
        self._gmt_finish = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, AccPayeeInfo):
            self._payee_info = value
        else:
            self._payee_info = AccPayeeInfo.from_alipay_dict(value)
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_currency(self):
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self._payment_currency = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def settlement_currency(self):
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self._settlement_currency = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.cert_info:
            if hasattr(self.cert_info, 'to_alipay_dict'):
                params['cert_info'] = self.cert_info.to_alipay_dict()
            else:
                params['cert_info'] = self.cert_info
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.detail_no:
            if hasattr(self.detail_no, 'to_alipay_dict'):
                params['detail_no'] = self.detail_no.to_alipay_dict()
            else:
                params['detail_no'] = self.detail_no
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_finish:
            if hasattr(self.gmt_finish, 'to_alipay_dict'):
                params['gmt_finish'] = self.gmt_finish.to_alipay_dict()
            else:
                params['gmt_finish'] = self.gmt_finish
        if self.need_retry:
            if hasattr(self.need_retry, 'to_alipay_dict'):
                params['need_retry'] = self.need_retry.to_alipay_dict()
            else:
                params['need_retry'] = self.need_retry
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_currency:
            if hasattr(self.payment_currency, 'to_alipay_dict'):
                params['payment_currency'] = self.payment_currency.to_alipay_dict()
            else:
                params['payment_currency'] = self.payment_currency
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.settlement_amount:
            if hasattr(self.settlement_amount, 'to_alipay_dict'):
                params['settlement_amount'] = self.settlement_amount.to_alipay_dict()
            else:
                params['settlement_amount'] = self.settlement_amount
        if self.settlement_currency:
            if hasattr(self.settlement_currency, 'to_alipay_dict'):
                params['settlement_currency'] = self.settlement_currency.to_alipay_dict()
            else:
                params['settlement_currency'] = self.settlement_currency
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccDetailModel()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'cert_info' in d:
            o.cert_info = d['cert_info']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'detail_no' in d:
            o.detail_no = d['detail_no']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_finish' in d:
            o.gmt_finish = d['gmt_finish']
        if 'need_retry' in d:
            o.need_retry = d['need_retry']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_currency' in d:
            o.payment_currency = d['payment_currency']
        if 'remark' in d:
            o.remark = d['remark']
        if 'settlement_amount' in d:
            o.settlement_amount = d['settlement_amount']
        if 'settlement_currency' in d:
            o.settlement_currency = d['settlement_currency']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        return o


