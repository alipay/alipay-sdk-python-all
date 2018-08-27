#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayTransferThirdpartyBillCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._amount = None
        self._currency = None
        self._ext_param = None
        self._memo = None
        self._partner_id = None
        self._payee_account = None
        self._payee_type = None
        self._payer_account = None
        self._payer_type = None
        self._payment_id = None
        self._payment_source = None
        self._title = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_type(self):
        return self._payee_type

    @payee_type.setter
    def payee_type(self, value):
        self._payee_type = value
    @property
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        self._payer_account = value
    @property
    def payer_type(self):
        return self._payer_type

    @payer_type.setter
    def payer_type(self, value):
        self._payer_type = value
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @property
    def payment_source(self):
        return self._payment_source

    @payment_source.setter
    def payment_source(self, value):
        self._payment_source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.transfer.thirdparty.bill.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = json.dumps(obj=self.amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = json.dumps(obj=self.currency.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['currency'] = self.currency
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = json.dumps(obj=self.ext_param.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ext_param'] = self.ext_param
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = json.dumps(obj=self.memo.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['memo'] = self.memo
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = json.dumps(obj=self.partner_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['partner_id'] = self.partner_id
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = json.dumps(obj=self.payee_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_account'] = self.payee_account
        if self.payee_type:
            if hasattr(self.payee_type, 'to_alipay_dict'):
                params['payee_type'] = json.dumps(obj=self.payee_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_type'] = self.payee_type
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = json.dumps(obj=self.payer_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payer_account'] = self.payer_account
        if self.payer_type:
            if hasattr(self.payer_type, 'to_alipay_dict'):
                params['payer_type'] = json.dumps(obj=self.payer_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payer_type'] = self.payer_type
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = json.dumps(obj=self.payment_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payment_id'] = self.payment_id
        if self.payment_source:
            if hasattr(self.payment_source, 'to_alipay_dict'):
                params['payment_source'] = json.dumps(obj=self.payment_source.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payment_source'] = self.payment_source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = json.dumps(obj=self.title.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['title'] = self.title
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
