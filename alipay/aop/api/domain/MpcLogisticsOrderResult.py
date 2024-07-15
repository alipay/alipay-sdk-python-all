#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcLogisticsDetail import MpcLogisticsDetail


class MpcLogisticsOrderResult(object):

    def __init__(self):
        self._logistics_company_code = None
        self._logistics_company_name = None
        self._logistics_detail_list = None
        self._mail_no = None

    @property
    def logistics_company_code(self):
        return self._logistics_company_code

    @logistics_company_code.setter
    def logistics_company_code(self, value):
        self._logistics_company_code = value
    @property
    def logistics_company_name(self):
        return self._logistics_company_name

    @logistics_company_name.setter
    def logistics_company_name(self, value):
        self._logistics_company_name = value
    @property
    def logistics_detail_list(self):
        return self._logistics_detail_list

    @logistics_detail_list.setter
    def logistics_detail_list(self, value):
        if isinstance(value, list):
            self._logistics_detail_list = list()
            for i in value:
                if isinstance(i, MpcLogisticsDetail):
                    self._logistics_detail_list.append(i)
                else:
                    self._logistics_detail_list.append(MpcLogisticsDetail.from_alipay_dict(i))
    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, value):
        self._mail_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_company_code:
            if hasattr(self.logistics_company_code, 'to_alipay_dict'):
                params['logistics_company_code'] = self.logistics_company_code.to_alipay_dict()
            else:
                params['logistics_company_code'] = self.logistics_company_code
        if self.logistics_company_name:
            if hasattr(self.logistics_company_name, 'to_alipay_dict'):
                params['logistics_company_name'] = self.logistics_company_name.to_alipay_dict()
            else:
                params['logistics_company_name'] = self.logistics_company_name
        if self.logistics_detail_list:
            if isinstance(self.logistics_detail_list, list):
                for i in range(0, len(self.logistics_detail_list)):
                    element = self.logistics_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.logistics_detail_list, 'to_alipay_dict'):
                params['logistics_detail_list'] = self.logistics_detail_list.to_alipay_dict()
            else:
                params['logistics_detail_list'] = self.logistics_detail_list
        if self.mail_no:
            if hasattr(self.mail_no, 'to_alipay_dict'):
                params['mail_no'] = self.mail_no.to_alipay_dict()
            else:
                params['mail_no'] = self.mail_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcLogisticsOrderResult()
        if 'logistics_company_code' in d:
            o.logistics_company_code = d['logistics_company_code']
        if 'logistics_company_name' in d:
            o.logistics_company_name = d['logistics_company_name']
        if 'logistics_detail_list' in d:
            o.logistics_detail_list = d['logistics_detail_list']
        if 'mail_no' in d:
            o.mail_no = d['mail_no']
        return o


