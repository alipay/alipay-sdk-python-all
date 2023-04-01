#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDossierRelationQueryModel(object):

    def __init__(self):
        self._ep_cert_no = None
        self._product_code = None
        self._relation_code_list = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def relation_code_list(self):
        return self._relation_code_list

    @relation_code_list.setter
    def relation_code_list(self, value):
        if isinstance(value, list):
            self._relation_code_list = list()
            for i in value:
                self._relation_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.relation_code_list:
            if isinstance(self.relation_code_list, list):
                for i in range(0, len(self.relation_code_list)):
                    element = self.relation_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relation_code_list[i] = element.to_alipay_dict()
            if hasattr(self.relation_code_list, 'to_alipay_dict'):
                params['relation_code_list'] = self.relation_code_list.to_alipay_dict()
            else:
                params['relation_code_list'] = self.relation_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDossierRelationQueryModel()
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'relation_code_list' in d:
            o.relation_code_list = d['relation_code_list']
        return o


