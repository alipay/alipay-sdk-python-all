#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneClaimOverdueQueryModel(object):

    def __init__(self):
        self._claim_no = None
        self._out_order_id = None
        self._overdue_no = None
        self._partner_org_id = None

    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def overdue_no(self):
        return self._overdue_no

    @overdue_no.setter
    def overdue_no(self, value):
        self._overdue_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.overdue_no:
            if hasattr(self.overdue_no, 'to_alipay_dict'):
                params['overdue_no'] = self.overdue_no.to_alipay_dict()
            else:
                params['overdue_no'] = self.overdue_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimOverdueQueryModel()
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'overdue_no' in d:
            o.overdue_no = d['overdue_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        return o


