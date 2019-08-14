#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationBizfeeAftechUnsubscribeModel(object):

    def __init__(self):
        self._app_name = None
        self._ar_no = None
        self._gmt_service = None
        self._gmt_stop = None
        self._out_biz_no = None
        self._return_fee_amount = None
        self._return_fee_currency = None
        self._tnt_inst_id = None
        self._used_service_amount = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def gmt_stop(self):
        return self._gmt_stop

    @gmt_stop.setter
    def gmt_stop(self, value):
        self._gmt_stop = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def return_fee_amount(self):
        return self._return_fee_amount

    @return_fee_amount.setter
    def return_fee_amount(self, value):
        self._return_fee_amount = value
    @property
    def return_fee_currency(self):
        return self._return_fee_currency

    @return_fee_currency.setter
    def return_fee_currency(self, value):
        self._return_fee_currency = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def used_service_amount(self):
        return self._used_service_amount

    @used_service_amount.setter
    def used_service_amount(self, value):
        self._used_service_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.gmt_stop:
            if hasattr(self.gmt_stop, 'to_alipay_dict'):
                params['gmt_stop'] = self.gmt_stop.to_alipay_dict()
            else:
                params['gmt_stop'] = self.gmt_stop
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.return_fee_amount:
            if hasattr(self.return_fee_amount, 'to_alipay_dict'):
                params['return_fee_amount'] = self.return_fee_amount.to_alipay_dict()
            else:
                params['return_fee_amount'] = self.return_fee_amount
        if self.return_fee_currency:
            if hasattr(self.return_fee_currency, 'to_alipay_dict'):
                params['return_fee_currency'] = self.return_fee_currency.to_alipay_dict()
            else:
                params['return_fee_currency'] = self.return_fee_currency
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.used_service_amount:
            if hasattr(self.used_service_amount, 'to_alipay_dict'):
                params['used_service_amount'] = self.used_service_amount.to_alipay_dict()
            else:
                params['used_service_amount'] = self.used_service_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationBizfeeAftechUnsubscribeModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'gmt_stop' in d:
            o.gmt_stop = d['gmt_stop']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'return_fee_amount' in d:
            o.return_fee_amount = d['return_fee_amount']
        if 'return_fee_currency' in d:
            o.return_fee_currency = d['return_fee_currency']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'used_service_amount' in d:
            o.used_service_amount = d['used_service_amount']
        return o


