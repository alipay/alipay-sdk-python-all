#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudFundWalletTemplateCreateModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._wallet_template_name = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def wallet_template_name(self):
        return self._wallet_template_name

    @wallet_template_name.setter
    def wallet_template_name(self, value):
        self._wallet_template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.wallet_template_name:
            if hasattr(self.wallet_template_name, 'to_alipay_dict'):
                params['wallet_template_name'] = self.wallet_template_name.to_alipay_dict()
            else:
                params['wallet_template_name'] = self.wallet_template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudFundWalletTemplateCreateModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'wallet_template_name' in d:
            o.wallet_template_name = d['wallet_template_name']
        return o


