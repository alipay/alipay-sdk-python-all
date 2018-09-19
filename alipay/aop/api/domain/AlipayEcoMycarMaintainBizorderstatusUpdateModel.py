#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainBizorderstatusUpdateModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._biz_status_txt = None
        self._industry_code = None
        self._logistics_code = None
        self._logistics_company = None
        self._logistics_no = None
        self._order_no = None
        self._order_status = None
        self._pay_account = None
        self._pay_time = None
        self._sender_addr = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def biz_status_txt(self):
        return self._biz_status_txt

    @biz_status_txt.setter
    def biz_status_txt(self, value):
        self._biz_status_txt = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_company(self):
        return self._logistics_company

    @logistics_company.setter
    def logistics_company(self, value):
        self._logistics_company = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def sender_addr(self):
        return self._sender_addr

    @sender_addr.setter
    def sender_addr(self, value):
        self._sender_addr = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.biz_status_txt:
            if hasattr(self.biz_status_txt, 'to_alipay_dict'):
                params['biz_status_txt'] = self.biz_status_txt.to_alipay_dict()
            else:
                params['biz_status_txt'] = self.biz_status_txt
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_company:
            if hasattr(self.logistics_company, 'to_alipay_dict'):
                params['logistics_company'] = self.logistics_company.to_alipay_dict()
            else:
                params['logistics_company'] = self.logistics_company
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.sender_addr:
            if hasattr(self.sender_addr, 'to_alipay_dict'):
                params['sender_addr'] = self.sender_addr.to_alipay_dict()
            else:
                params['sender_addr'] = self.sender_addr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarMaintainBizorderstatusUpdateModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'biz_status_txt' in d:
            o.biz_status_txt = d['biz_status_txt']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_company' in d:
            o.logistics_company = d['logistics_company']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'sender_addr' in d:
            o.sender_addr = d['sender_addr']
        return o


