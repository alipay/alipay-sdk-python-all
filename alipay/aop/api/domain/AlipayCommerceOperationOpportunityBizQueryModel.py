#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationOpportunityBizQueryModel(object):

    def __init__(self):
        self._opportunity_id = None
        self._out_biz_no = None

    @property
    def opportunity_id(self):
        return self._opportunity_id

    @opportunity_id.setter
    def opportunity_id(self, value):
        self._opportunity_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.opportunity_id:
            if hasattr(self.opportunity_id, 'to_alipay_dict'):
                params['opportunity_id'] = self.opportunity_id.to_alipay_dict()
            else:
                params['opportunity_id'] = self.opportunity_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationOpportunityBizQueryModel()
        if 'opportunity_id' in d:
            o.opportunity_id = d['opportunity_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


