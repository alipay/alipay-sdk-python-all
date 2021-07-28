#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConfirmReceivableDTO(object):

    def __init__(self):
        self._confirm_model = None
        self._out_biz_no = None
        self._receivable_no = None

    @property
    def confirm_model(self):
        return self._confirm_model

    @confirm_model.setter
    def confirm_model(self, value):
        self._confirm_model = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def receivable_no(self):
        return self._receivable_no

    @receivable_no.setter
    def receivable_no(self, value):
        self._receivable_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_model:
            if hasattr(self.confirm_model, 'to_alipay_dict'):
                params['confirm_model'] = self.confirm_model.to_alipay_dict()
            else:
                params['confirm_model'] = self.confirm_model
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.receivable_no:
            if hasattr(self.receivable_no, 'to_alipay_dict'):
                params['receivable_no'] = self.receivable_no.to_alipay_dict()
            else:
                params['receivable_no'] = self.receivable_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConfirmReceivableDTO()
        if 'confirm_model' in d:
            o.confirm_model = d['confirm_model']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'receivable_no' in d:
            o.receivable_no = d['receivable_no']
        return o


