#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GfacConsolidationEntryLineDTO import GfacConsolidationEntryLineDTO


class AlipayBossFncGfaccenterConsolidationAcceptModel(object):

    def __init__(self):
        self._acc_month = None
        self._adjust_period = None
        self._biz_chain = None
        self._biz_date_time = None
        self._biz_event_code = None
        self._biz_module = None
        self._biz_product_code = None
        self._coa_type = None
        self._exchange_date = None
        self._exchange_rate = None
        self._exchange_type = None
        self._expect_account_date = None
        self._je_desc = None
        self._je_lines = None
        self._je_name = None
        self._je_no = None
        self._memo = None
        self._orig_currency_code = None
        self._recon_inst = None
        self._sob_currency_code = None
        self._sob_type = None
        self._src_app = None
        self._submitter = None
        self._use_user_rate_info = None

    @property
    def acc_month(self):
        return self._acc_month

    @acc_month.setter
    def acc_month(self, value):
        self._acc_month = value
    @property
    def adjust_period(self):
        return self._adjust_period

    @adjust_period.setter
    def adjust_period(self, value):
        self._adjust_period = value
    @property
    def biz_chain(self):
        return self._biz_chain

    @biz_chain.setter
    def biz_chain(self, value):
        self._biz_chain = value
    @property
    def biz_date_time(self):
        return self._biz_date_time

    @biz_date_time.setter
    def biz_date_time(self, value):
        self._biz_date_time = value
    @property
    def biz_event_code(self):
        return self._biz_event_code

    @biz_event_code.setter
    def biz_event_code(self, value):
        self._biz_event_code = value
    @property
    def biz_module(self):
        return self._biz_module

    @biz_module.setter
    def biz_module(self, value):
        self._biz_module = value
    @property
    def biz_product_code(self):
        return self._biz_product_code

    @biz_product_code.setter
    def biz_product_code(self, value):
        self._biz_product_code = value
    @property
    def coa_type(self):
        return self._coa_type

    @coa_type.setter
    def coa_type(self, value):
        self._coa_type = value
    @property
    def exchange_date(self):
        return self._exchange_date

    @exchange_date.setter
    def exchange_date(self, value):
        self._exchange_date = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def exchange_type(self):
        return self._exchange_type

    @exchange_type.setter
    def exchange_type(self, value):
        self._exchange_type = value
    @property
    def expect_account_date(self):
        return self._expect_account_date

    @expect_account_date.setter
    def expect_account_date(self, value):
        self._expect_account_date = value
    @property
    def je_desc(self):
        return self._je_desc

    @je_desc.setter
    def je_desc(self, value):
        self._je_desc = value
    @property
    def je_lines(self):
        return self._je_lines

    @je_lines.setter
    def je_lines(self, value):
        if isinstance(value, list):
            self._je_lines = list()
            for i in value:
                if isinstance(i, GfacConsolidationEntryLineDTO):
                    self._je_lines.append(i)
                else:
                    self._je_lines.append(GfacConsolidationEntryLineDTO.from_alipay_dict(i))
    @property
    def je_name(self):
        return self._je_name

    @je_name.setter
    def je_name(self, value):
        self._je_name = value
    @property
    def je_no(self):
        return self._je_no

    @je_no.setter
    def je_no(self, value):
        self._je_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def orig_currency_code(self):
        return self._orig_currency_code

    @orig_currency_code.setter
    def orig_currency_code(self, value):
        self._orig_currency_code = value
    @property
    def recon_inst(self):
        return self._recon_inst

    @recon_inst.setter
    def recon_inst(self, value):
        self._recon_inst = value
    @property
    def sob_currency_code(self):
        return self._sob_currency_code

    @sob_currency_code.setter
    def sob_currency_code(self, value):
        self._sob_currency_code = value
    @property
    def sob_type(self):
        return self._sob_type

    @sob_type.setter
    def sob_type(self, value):
        self._sob_type = value
    @property
    def src_app(self):
        return self._src_app

    @src_app.setter
    def src_app(self, value):
        self._src_app = value
    @property
    def submitter(self):
        return self._submitter

    @submitter.setter
    def submitter(self, value):
        self._submitter = value
    @property
    def use_user_rate_info(self):
        return self._use_user_rate_info

    @use_user_rate_info.setter
    def use_user_rate_info(self, value):
        self._use_user_rate_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_month:
            if hasattr(self.acc_month, 'to_alipay_dict'):
                params['acc_month'] = self.acc_month.to_alipay_dict()
            else:
                params['acc_month'] = self.acc_month
        if self.adjust_period:
            if hasattr(self.adjust_period, 'to_alipay_dict'):
                params['adjust_period'] = self.adjust_period.to_alipay_dict()
            else:
                params['adjust_period'] = self.adjust_period
        if self.biz_chain:
            if hasattr(self.biz_chain, 'to_alipay_dict'):
                params['biz_chain'] = self.biz_chain.to_alipay_dict()
            else:
                params['biz_chain'] = self.biz_chain
        if self.biz_date_time:
            if hasattr(self.biz_date_time, 'to_alipay_dict'):
                params['biz_date_time'] = self.biz_date_time.to_alipay_dict()
            else:
                params['biz_date_time'] = self.biz_date_time
        if self.biz_event_code:
            if hasattr(self.biz_event_code, 'to_alipay_dict'):
                params['biz_event_code'] = self.biz_event_code.to_alipay_dict()
            else:
                params['biz_event_code'] = self.biz_event_code
        if self.biz_module:
            if hasattr(self.biz_module, 'to_alipay_dict'):
                params['biz_module'] = self.biz_module.to_alipay_dict()
            else:
                params['biz_module'] = self.biz_module
        if self.biz_product_code:
            if hasattr(self.biz_product_code, 'to_alipay_dict'):
                params['biz_product_code'] = self.biz_product_code.to_alipay_dict()
            else:
                params['biz_product_code'] = self.biz_product_code
        if self.coa_type:
            if hasattr(self.coa_type, 'to_alipay_dict'):
                params['coa_type'] = self.coa_type.to_alipay_dict()
            else:
                params['coa_type'] = self.coa_type
        if self.exchange_date:
            if hasattr(self.exchange_date, 'to_alipay_dict'):
                params['exchange_date'] = self.exchange_date.to_alipay_dict()
            else:
                params['exchange_date'] = self.exchange_date
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.exchange_type:
            if hasattr(self.exchange_type, 'to_alipay_dict'):
                params['exchange_type'] = self.exchange_type.to_alipay_dict()
            else:
                params['exchange_type'] = self.exchange_type
        if self.expect_account_date:
            if hasattr(self.expect_account_date, 'to_alipay_dict'):
                params['expect_account_date'] = self.expect_account_date.to_alipay_dict()
            else:
                params['expect_account_date'] = self.expect_account_date
        if self.je_desc:
            if hasattr(self.je_desc, 'to_alipay_dict'):
                params['je_desc'] = self.je_desc.to_alipay_dict()
            else:
                params['je_desc'] = self.je_desc
        if self.je_lines:
            if isinstance(self.je_lines, list):
                for i in range(0, len(self.je_lines)):
                    element = self.je_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.je_lines[i] = element.to_alipay_dict()
            if hasattr(self.je_lines, 'to_alipay_dict'):
                params['je_lines'] = self.je_lines.to_alipay_dict()
            else:
                params['je_lines'] = self.je_lines
        if self.je_name:
            if hasattr(self.je_name, 'to_alipay_dict'):
                params['je_name'] = self.je_name.to_alipay_dict()
            else:
                params['je_name'] = self.je_name
        if self.je_no:
            if hasattr(self.je_no, 'to_alipay_dict'):
                params['je_no'] = self.je_no.to_alipay_dict()
            else:
                params['je_no'] = self.je_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.orig_currency_code:
            if hasattr(self.orig_currency_code, 'to_alipay_dict'):
                params['orig_currency_code'] = self.orig_currency_code.to_alipay_dict()
            else:
                params['orig_currency_code'] = self.orig_currency_code
        if self.recon_inst:
            if hasattr(self.recon_inst, 'to_alipay_dict'):
                params['recon_inst'] = self.recon_inst.to_alipay_dict()
            else:
                params['recon_inst'] = self.recon_inst
        if self.sob_currency_code:
            if hasattr(self.sob_currency_code, 'to_alipay_dict'):
                params['sob_currency_code'] = self.sob_currency_code.to_alipay_dict()
            else:
                params['sob_currency_code'] = self.sob_currency_code
        if self.sob_type:
            if hasattr(self.sob_type, 'to_alipay_dict'):
                params['sob_type'] = self.sob_type.to_alipay_dict()
            else:
                params['sob_type'] = self.sob_type
        if self.src_app:
            if hasattr(self.src_app, 'to_alipay_dict'):
                params['src_app'] = self.src_app.to_alipay_dict()
            else:
                params['src_app'] = self.src_app
        if self.submitter:
            if hasattr(self.submitter, 'to_alipay_dict'):
                params['submitter'] = self.submitter.to_alipay_dict()
            else:
                params['submitter'] = self.submitter
        if self.use_user_rate_info:
            if hasattr(self.use_user_rate_info, 'to_alipay_dict'):
                params['use_user_rate_info'] = self.use_user_rate_info.to_alipay_dict()
            else:
                params['use_user_rate_info'] = self.use_user_rate_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfaccenterConsolidationAcceptModel()
        if 'acc_month' in d:
            o.acc_month = d['acc_month']
        if 'adjust_period' in d:
            o.adjust_period = d['adjust_period']
        if 'biz_chain' in d:
            o.biz_chain = d['biz_chain']
        if 'biz_date_time' in d:
            o.biz_date_time = d['biz_date_time']
        if 'biz_event_code' in d:
            o.biz_event_code = d['biz_event_code']
        if 'biz_module' in d:
            o.biz_module = d['biz_module']
        if 'biz_product_code' in d:
            o.biz_product_code = d['biz_product_code']
        if 'coa_type' in d:
            o.coa_type = d['coa_type']
        if 'exchange_date' in d:
            o.exchange_date = d['exchange_date']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'exchange_type' in d:
            o.exchange_type = d['exchange_type']
        if 'expect_account_date' in d:
            o.expect_account_date = d['expect_account_date']
        if 'je_desc' in d:
            o.je_desc = d['je_desc']
        if 'je_lines' in d:
            o.je_lines = d['je_lines']
        if 'je_name' in d:
            o.je_name = d['je_name']
        if 'je_no' in d:
            o.je_no = d['je_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'orig_currency_code' in d:
            o.orig_currency_code = d['orig_currency_code']
        if 'recon_inst' in d:
            o.recon_inst = d['recon_inst']
        if 'sob_currency_code' in d:
            o.sob_currency_code = d['sob_currency_code']
        if 'sob_type' in d:
            o.sob_type = d['sob_type']
        if 'src_app' in d:
            o.src_app = d['src_app']
        if 'submitter' in d:
            o.submitter = d['submitter']
        if 'use_user_rate_info' in d:
            o.use_user_rate_info = d['use_user_rate_info']
        return o


