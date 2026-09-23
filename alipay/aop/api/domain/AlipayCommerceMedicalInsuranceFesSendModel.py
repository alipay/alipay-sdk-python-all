#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceFesSendModel(object):

    def __init__(self):
        self._cur_company_id = None
        self._enc_content = None
        self._enterprise_url = None
        self._trans_date = None
        self._trans_no = None

    @property
    def cur_company_id(self):
        return self._cur_company_id

    @cur_company_id.setter
    def cur_company_id(self, value):
        self._cur_company_id = value
    @property
    def enc_content(self):
        return self._enc_content

    @enc_content.setter
    def enc_content(self, value):
        self._enc_content = value
    @property
    def enterprise_url(self):
        return self._enterprise_url

    @enterprise_url.setter
    def enterprise_url(self, value):
        self._enterprise_url = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_company_id:
            if hasattr(self.cur_company_id, 'to_alipay_dict'):
                params['cur_company_id'] = self.cur_company_id.to_alipay_dict()
            else:
                params['cur_company_id'] = self.cur_company_id
        if self.enc_content:
            if hasattr(self.enc_content, 'to_alipay_dict'):
                params['enc_content'] = self.enc_content.to_alipay_dict()
            else:
                params['enc_content'] = self.enc_content
        if self.enterprise_url:
            if hasattr(self.enterprise_url, 'to_alipay_dict'):
                params['enterprise_url'] = self.enterprise_url.to_alipay_dict()
            else:
                params['enterprise_url'] = self.enterprise_url
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        if self.trans_no:
            if hasattr(self.trans_no, 'to_alipay_dict'):
                params['trans_no'] = self.trans_no.to_alipay_dict()
            else:
                params['trans_no'] = self.trans_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceFesSendModel()
        if 'cur_company_id' in d:
            o.cur_company_id = d['cur_company_id']
        if 'enc_content' in d:
            o.enc_content = d['enc_content']
        if 'enterprise_url' in d:
            o.enterprise_url = d['enterprise_url']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        if 'trans_no' in d:
            o.trans_no = d['trans_no']
        return o


