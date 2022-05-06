#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YunTaskVoucherTemplateInfo(object):

    def __init__(self):
        self._template_id = None
        self._voucher_name = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskVoucherTemplateInfo()
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        return o


