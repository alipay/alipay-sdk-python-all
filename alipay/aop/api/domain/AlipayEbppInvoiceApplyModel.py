#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceApplyOpenModel import InvoiceApplyOpenModel


class AlipayEbppInvoiceApplyModel(object):

    def __init__(self):
        self._action = None
        self._apply_from = None
        self._invoice_apply_model = None
        self._m_short_name = None
        self._sub_m_short_name = None
        self._user_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def apply_from(self):
        return self._apply_from

    @apply_from.setter
    def apply_from(self, value):
        self._apply_from = value
    @property
    def invoice_apply_model(self):
        return self._invoice_apply_model

    @invoice_apply_model.setter
    def invoice_apply_model(self, value):
        if isinstance(value, InvoiceApplyOpenModel):
            self._invoice_apply_model = value
        else:
            self._invoice_apply_model = InvoiceApplyOpenModel.from_alipay_dict(value)
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.apply_from:
            if hasattr(self.apply_from, 'to_alipay_dict'):
                params['apply_from'] = self.apply_from.to_alipay_dict()
            else:
                params['apply_from'] = self.apply_from
        if self.invoice_apply_model:
            if hasattr(self.invoice_apply_model, 'to_alipay_dict'):
                params['invoice_apply_model'] = self.invoice_apply_model.to_alipay_dict()
            else:
                params['invoice_apply_model'] = self.invoice_apply_model
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
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
        o = AlipayEbppInvoiceApplyModel()
        if 'action' in d:
            o.action = d['action']
        if 'apply_from' in d:
            o.apply_from = d['apply_from']
        if 'invoice_apply_model' in d:
            o.invoice_apply_model = d['invoice_apply_model']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


