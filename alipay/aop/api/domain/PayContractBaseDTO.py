#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayContractBaseDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_source = None
        self._biz_pd_code = None
        self._idempotent_no = None
        self._ip_role_id = None
        self._ip_role_source = None
        self._pd_code = None
        self._sales_product_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_source(self):
        return self._agreement_source

    @agreement_source.setter
    def agreement_source(self, value):
        self._agreement_source = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_source(self):
        return self._ip_role_source

    @ip_role_source.setter
    def ip_role_source(self, value):
        self._ip_role_source = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_source:
            if hasattr(self.agreement_source, 'to_alipay_dict'):
                params['agreement_source'] = self.agreement_source.to_alipay_dict()
            else:
                params['agreement_source'] = self.agreement_source
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_source:
            if hasattr(self.ip_role_source, 'to_alipay_dict'):
                params['ip_role_source'] = self.ip_role_source.to_alipay_dict()
            else:
                params['ip_role_source'] = self.ip_role_source
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayContractBaseDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_source' in d:
            o.agreement_source = d['agreement_source']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_source' in d:
            o.ip_role_source = d['ip_role_source']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        return o


