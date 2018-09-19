#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransAacollectBatchCreateModel(object):

    def __init__(self):
        self._batch_memo = None
        self._channel = None
        self._ext_param = None
        self._limit_items_total = None
        self._pay_amount_single = None
        self._pay_amount_total = None
        self._payee_user_id = None
        self._payer_user_ids = None
        self._real_items_total = None
        self._show_items_total = None
        self._source = None

    @property
    def batch_memo(self):
        return self._batch_memo

    @batch_memo.setter
    def batch_memo(self, value):
        self._batch_memo = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def limit_items_total(self):
        return self._limit_items_total

    @limit_items_total.setter
    def limit_items_total(self, value):
        self._limit_items_total = value
    @property
    def pay_amount_single(self):
        return self._pay_amount_single

    @pay_amount_single.setter
    def pay_amount_single(self, value):
        self._pay_amount_single = value
    @property
    def pay_amount_total(self):
        return self._pay_amount_total

    @pay_amount_total.setter
    def pay_amount_total(self, value):
        self._pay_amount_total = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value
    @property
    def payer_user_ids(self):
        return self._payer_user_ids

    @payer_user_ids.setter
    def payer_user_ids(self, value):
        self._payer_user_ids = value
    @property
    def real_items_total(self):
        return self._real_items_total

    @real_items_total.setter
    def real_items_total(self, value):
        self._real_items_total = value
    @property
    def show_items_total(self):
        return self._show_items_total

    @show_items_total.setter
    def show_items_total(self, value):
        self._show_items_total = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_memo:
            if hasattr(self.batch_memo, 'to_alipay_dict'):
                params['batch_memo'] = self.batch_memo.to_alipay_dict()
            else:
                params['batch_memo'] = self.batch_memo
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.limit_items_total:
            if hasattr(self.limit_items_total, 'to_alipay_dict'):
                params['limit_items_total'] = self.limit_items_total.to_alipay_dict()
            else:
                params['limit_items_total'] = self.limit_items_total
        if self.pay_amount_single:
            if hasattr(self.pay_amount_single, 'to_alipay_dict'):
                params['pay_amount_single'] = self.pay_amount_single.to_alipay_dict()
            else:
                params['pay_amount_single'] = self.pay_amount_single
        if self.pay_amount_total:
            if hasattr(self.pay_amount_total, 'to_alipay_dict'):
                params['pay_amount_total'] = self.pay_amount_total.to_alipay_dict()
            else:
                params['pay_amount_total'] = self.pay_amount_total
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        if self.payer_user_ids:
            if hasattr(self.payer_user_ids, 'to_alipay_dict'):
                params['payer_user_ids'] = self.payer_user_ids.to_alipay_dict()
            else:
                params['payer_user_ids'] = self.payer_user_ids
        if self.real_items_total:
            if hasattr(self.real_items_total, 'to_alipay_dict'):
                params['real_items_total'] = self.real_items_total.to_alipay_dict()
            else:
                params['real_items_total'] = self.real_items_total
        if self.show_items_total:
            if hasattr(self.show_items_total, 'to_alipay_dict'):
                params['show_items_total'] = self.show_items_total.to_alipay_dict()
            else:
                params['show_items_total'] = self.show_items_total
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransAacollectBatchCreateModel()
        if 'batch_memo' in d:
            o.batch_memo = d['batch_memo']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'limit_items_total' in d:
            o.limit_items_total = d['limit_items_total']
        if 'pay_amount_single' in d:
            o.pay_amount_single = d['pay_amount_single']
        if 'pay_amount_total' in d:
            o.pay_amount_total = d['pay_amount_total']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        if 'payer_user_ids' in d:
            o.payer_user_ids = d['payer_user_ids']
        if 'real_items_total' in d:
            o.real_items_total = d['real_items_total']
        if 'show_items_total' in d:
            o.show_items_total = d['show_items_total']
        if 'source' in d:
            o.source = d['source']
        return o


