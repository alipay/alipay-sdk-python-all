#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeUpdateLeadsRequest(object):

    def __init__(self):
        self._bd_work_no = None
        self._leads_code = None
        self._leads_source_partner_id = None
        self._modifier = None

    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def leads_source_partner_id(self):
        return self._leads_source_partner_id

    @leads_source_partner_id.setter
    def leads_source_partner_id(self, value):
        self._leads_source_partner_id = value
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.leads_source_partner_id:
            if hasattr(self.leads_source_partner_id, 'to_alipay_dict'):
                params['leads_source_partner_id'] = self.leads_source_partner_id.to_alipay_dict()
            else:
                params['leads_source_partner_id'] = self.leads_source_partner_id
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeUpdateLeadsRequest()
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'leads_source_partner_id' in d:
            o.leads_source_partner_id = d['leads_source_partner_id']
        if 'modifier' in d:
            o.modifier = d['modifier']
        return o


