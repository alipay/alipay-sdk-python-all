#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryCustomerByEpCertNoRequest(object):

    def __init__(self):
        self._ep_cert_no_list = None

    @property
    def ep_cert_no_list(self):
        return self._ep_cert_no_list

    @ep_cert_no_list.setter
    def ep_cert_no_list(self, value):
        if isinstance(value, list):
            self._ep_cert_no_list = list()
            for i in value:
                self._ep_cert_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ep_cert_no_list:
            if isinstance(self.ep_cert_no_list, list):
                for i in range(0, len(self.ep_cert_no_list)):
                    element = self.ep_cert_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ep_cert_no_list[i] = element.to_alipay_dict()
            if hasattr(self.ep_cert_no_list, 'to_alipay_dict'):
                params['ep_cert_no_list'] = self.ep_cert_no_list.to_alipay_dict()
            else:
                params['ep_cert_no_list'] = self.ep_cert_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryCustomerByEpCertNoRequest()
        if 'ep_cert_no_list' in d:
            o.ep_cert_no_list = d['ep_cert_no_list']
        return o


