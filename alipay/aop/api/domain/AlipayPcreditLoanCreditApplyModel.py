#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanCreditApplyModel(object):

    def __init__(self):
        self._authorized_status = None
        self._back_url = None
        self._out_biz_no = None
        self._out_request_no = None

    @property
    def authorized_status(self):
        return self._authorized_status

    @authorized_status.setter
    def authorized_status(self, value):
        self._authorized_status = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_status:
            if hasattr(self.authorized_status, 'to_alipay_dict'):
                params['authorized_status'] = self.authorized_status.to_alipay_dict()
            else:
                params['authorized_status'] = self.authorized_status
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanCreditApplyModel()
        if 'authorized_status' in d:
            o.authorized_status = d['authorized_status']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


