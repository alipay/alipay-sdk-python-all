#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SolutionSiteInfo import SolutionSiteInfo


class AlipayTradeSolutionprodMerchantupgradeApplyModel(object):

    def __init__(self):
        self._back_url = None
        self._back_url_type = None
        self._city_name = None
        self._current_merchant_type = None
        self._out_biz_no = None
        self._province_name = None
        self._service = None
        self._sites = None
        self._smid = None
        self._solution_code = None
        self._target_merchant_type = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def back_url_type(self):
        return self._back_url_type

    @back_url_type.setter
    def back_url_type(self, value):
        self._back_url_type = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def current_merchant_type(self):
        return self._current_merchant_type

    @current_merchant_type.setter
    def current_merchant_type(self, value):
        self._current_merchant_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        if isinstance(value, list):
            self._service = list()
            for i in value:
                self._service.append(i)
    @property
    def sites(self):
        return self._sites

    @sites.setter
    def sites(self, value):
        if isinstance(value, list):
            self._sites = list()
            for i in value:
                if isinstance(i, SolutionSiteInfo):
                    self._sites.append(i)
                else:
                    self._sites.append(SolutionSiteInfo.from_alipay_dict(i))
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def target_merchant_type(self):
        return self._target_merchant_type

    @target_merchant_type.setter
    def target_merchant_type(self, value):
        self._target_merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.back_url_type:
            if hasattr(self.back_url_type, 'to_alipay_dict'):
                params['back_url_type'] = self.back_url_type.to_alipay_dict()
            else:
                params['back_url_type'] = self.back_url_type
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.current_merchant_type:
            if hasattr(self.current_merchant_type, 'to_alipay_dict'):
                params['current_merchant_type'] = self.current_merchant_type.to_alipay_dict()
            else:
                params['current_merchant_type'] = self.current_merchant_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.service:
            if isinstance(self.service, list):
                for i in range(0, len(self.service)):
                    element = self.service[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service[i] = element.to_alipay_dict()
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.sites:
            if isinstance(self.sites, list):
                for i in range(0, len(self.sites)):
                    element = self.sites[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sites[i] = element.to_alipay_dict()
            if hasattr(self.sites, 'to_alipay_dict'):
                params['sites'] = self.sites.to_alipay_dict()
            else:
                params['sites'] = self.sites
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.target_merchant_type:
            if hasattr(self.target_merchant_type, 'to_alipay_dict'):
                params['target_merchant_type'] = self.target_merchant_type.to_alipay_dict()
            else:
                params['target_merchant_type'] = self.target_merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSolutionprodMerchantupgradeApplyModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'back_url_type' in d:
            o.back_url_type = d['back_url_type']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'current_merchant_type' in d:
            o.current_merchant_type = d['current_merchant_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'service' in d:
            o.service = d['service']
        if 'sites' in d:
            o.sites = d['sites']
        if 'smid' in d:
            o.smid = d['smid']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'target_merchant_type' in d:
            o.target_merchant_type = d['target_merchant_type']
        return o


