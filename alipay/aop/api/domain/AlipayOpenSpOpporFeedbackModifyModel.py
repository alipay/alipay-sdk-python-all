#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpOpporFeedbackModifyModel(object):

    def __init__(self):
        self._expand_result = None
        self._isv_pid = None
        self._leads_id = None
        self._merchant_pid = None
        self._oppor_id = None
        self._sn = None

    @property
    def expand_result(self):
        return self._expand_result

    @expand_result.setter
    def expand_result(self, value):
        self._expand_result = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def oppor_id(self):
        return self._oppor_id

    @oppor_id.setter
    def oppor_id(self, value):
        self._oppor_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.expand_result:
            if hasattr(self.expand_result, 'to_alipay_dict'):
                params['expand_result'] = self.expand_result.to_alipay_dict()
            else:
                params['expand_result'] = self.expand_result
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.oppor_id:
            if hasattr(self.oppor_id, 'to_alipay_dict'):
                params['oppor_id'] = self.oppor_id.to_alipay_dict()
            else:
                params['oppor_id'] = self.oppor_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpOpporFeedbackModifyModel()
        if 'expand_result' in d:
            o.expand_result = d['expand_result']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'oppor_id' in d:
            o.oppor_id = d['oppor_id']
        if 'sn' in d:
            o.sn = d['sn']
        return o


