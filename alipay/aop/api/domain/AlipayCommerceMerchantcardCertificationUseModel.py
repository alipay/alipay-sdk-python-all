#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCertificateUseInfo import MerchantCertificateUseInfo


class AlipayCommerceMerchantcardCertificationUseModel(object):

    def __init__(self):
        self._certificate_use_info_list = None
        self._shop_id = None

    @property
    def certificate_use_info_list(self):
        return self._certificate_use_info_list

    @certificate_use_info_list.setter
    def certificate_use_info_list(self, value):
        if isinstance(value, list):
            self._certificate_use_info_list = list()
            for i in value:
                if isinstance(i, MerchantCertificateUseInfo):
                    self._certificate_use_info_list.append(i)
                else:
                    self._certificate_use_info_list.append(MerchantCertificateUseInfo.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_use_info_list:
            if isinstance(self.certificate_use_info_list, list):
                for i in range(0, len(self.certificate_use_info_list)):
                    element = self.certificate_use_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_use_info_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_use_info_list, 'to_alipay_dict'):
                params['certificate_use_info_list'] = self.certificate_use_info_list.to_alipay_dict()
            else:
                params['certificate_use_info_list'] = self.certificate_use_info_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardCertificationUseModel()
        if 'certificate_use_info_list' in d:
            o.certificate_use_info_list = d['certificate_use_info_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


