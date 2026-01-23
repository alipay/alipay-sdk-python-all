#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DecorationLeadsFeedbackContact import DecorationLeadsFeedbackContact
from alipay.aop.api.domain.DecorationLeadsFeedbackTransInfo import DecorationLeadsFeedbackTransInfo


class AlipayEbppIndustryDecorationLeadsSyncModel(object):

    def __init__(self):
        self._company_name = None
        self._contact = None
        self._leads_biz_id = None
        self._trans_info = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if isinstance(value, DecorationLeadsFeedbackContact):
            self._contact = value
        else:
            self._contact = DecorationLeadsFeedbackContact.from_alipay_dict(value)
    @property
    def leads_biz_id(self):
        return self._leads_biz_id

    @leads_biz_id.setter
    def leads_biz_id(self, value):
        self._leads_biz_id = value
    @property
    def trans_info(self):
        return self._trans_info

    @trans_info.setter
    def trans_info(self, value):
        if isinstance(value, DecorationLeadsFeedbackTransInfo):
            self._trans_info = value
        else:
            self._trans_info = DecorationLeadsFeedbackTransInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.leads_biz_id:
            if hasattr(self.leads_biz_id, 'to_alipay_dict'):
                params['leads_biz_id'] = self.leads_biz_id.to_alipay_dict()
            else:
                params['leads_biz_id'] = self.leads_biz_id
        if self.trans_info:
            if hasattr(self.trans_info, 'to_alipay_dict'):
                params['trans_info'] = self.trans_info.to_alipay_dict()
            else:
                params['trans_info'] = self.trans_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryDecorationLeadsSyncModel()
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact' in d:
            o.contact = d['contact']
        if 'leads_biz_id' in d:
            o.leads_biz_id = d['leads_biz_id']
        if 'trans_info' in d:
            o.trans_info = d['trans_info']
        return o


