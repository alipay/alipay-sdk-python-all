#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainOrderCreateModel(object):

    def __init__(self):
        self._biz_status = None
        self._biz_status_txt = None
        self._ext_param = None
        self._out_order_no = None
        self._subject = None
        self._summary = None
        self._total_fee = None
        self._user_id = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def biz_status_txt(self):
        return self._biz_status_txt

    @biz_status_txt.setter
    def biz_status_txt(self, value):
        self._biz_status_txt = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.biz_status_txt:
            if hasattr(self.biz_status_txt, 'to_alipay_dict'):
                params['biz_status_txt'] = self.biz_status_txt.to_alipay_dict()
            else:
                params['biz_status_txt'] = self.biz_status_txt
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
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
        o = AlipayEcoMycarMaintainOrderCreateModel()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'biz_status_txt' in d:
            o.biz_status_txt = d['biz_status_txt']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'subject' in d:
            o.subject = d['subject']
        if 'summary' in d:
            o.summary = d['summary']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


