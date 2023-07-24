#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDossierAuthassetQueryModel(object):

    def __init__(self):
        self._ep_asset_type_list = None
        self._ep_cert_no = None

    @property
    def ep_asset_type_list(self):
        return self._ep_asset_type_list

    @ep_asset_type_list.setter
    def ep_asset_type_list(self, value):
        if isinstance(value, list):
            self._ep_asset_type_list = list()
            for i in value:
                self._ep_asset_type_list.append(i)
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_asset_type_list:
            if isinstance(self.ep_asset_type_list, list):
                for i in range(0, len(self.ep_asset_type_list)):
                    element = self.ep_asset_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ep_asset_type_list[i] = element.to_alipay_dict()
            if hasattr(self.ep_asset_type_list, 'to_alipay_dict'):
                params['ep_asset_type_list'] = self.ep_asset_type_list.to_alipay_dict()
            else:
                params['ep_asset_type_list'] = self.ep_asset_type_list
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDossierAuthassetQueryModel()
        if 'ep_asset_type_list' in d:
            o.ep_asset_type_list = d['ep_asset_type_list']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        return o


