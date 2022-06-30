#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalOnlineCreateAndPayInfo(object):

    def __init__(self):
        self._chnl_ord_sn = None
        self._med_org_ord = None
        self._out_trade_no = None
        self._pay_order_id = None
        self._pay_url = None
        self._status = None

    @property
    def chnl_ord_sn(self):
        return self._chnl_ord_sn

    @chnl_ord_sn.setter
    def chnl_ord_sn(self, value):
        self._chnl_ord_sn = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.chnl_ord_sn:
            if hasattr(self.chnl_ord_sn, 'to_alipay_dict'):
                params['chnl_ord_sn'] = self.chnl_ord_sn.to_alipay_dict()
            else:
                params['chnl_ord_sn'] = self.chnl_ord_sn
        if self.med_org_ord:
            if hasattr(self.med_org_ord, 'to_alipay_dict'):
                params['med_org_ord'] = self.med_org_ord.to_alipay_dict()
            else:
                params['med_org_ord'] = self.med_org_ord
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.pay_url:
            if hasattr(self.pay_url, 'to_alipay_dict'):
                params['pay_url'] = self.pay_url.to_alipay_dict()
            else:
                params['pay_url'] = self.pay_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalOnlineCreateAndPayInfo()
        if 'chnl_ord_sn' in d:
            o.chnl_ord_sn = d['chnl_ord_sn']
        if 'med_org_ord' in d:
            o.med_org_ord = d['med_org_ord']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'pay_url' in d:
            o.pay_url = d['pay_url']
        if 'status' in d:
            o.status = d['status']
        return o


