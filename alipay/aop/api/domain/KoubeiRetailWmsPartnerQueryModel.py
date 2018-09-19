#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsPartnerQueryModel(object):

    def __init__(self):
        self._operate_context = None
        self._partner_ids = None

    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def partner_ids(self):
        return self._partner_ids

    @partner_ids.setter
    def partner_ids(self, value):
        if isinstance(value, list):
            self._partner_ids = list()
            for i in value:
                self._partner_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.partner_ids:
            if isinstance(self.partner_ids, list):
                for i in range(0, len(self.partner_ids)):
                    element = self.partner_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.partner_ids[i] = element.to_alipay_dict()
            if hasattr(self.partner_ids, 'to_alipay_dict'):
                params['partner_ids'] = self.partner_ids.to_alipay_dict()
            else:
                params['partner_ids'] = self.partner_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsPartnerQueryModel()
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'partner_ids' in d:
            o.partner_ids = d['partner_ids']
        return o


