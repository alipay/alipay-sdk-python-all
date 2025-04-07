#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleCheckDetailItem import VehicleCheckDetailItem


class CheckReportData(object):

    def __init__(self):
        self._buyback_auth = None
        self._report_origin_code = None
        self._vehicle_check_detail = None
        self._vehicle_check_url = None
        self._vehicle_exclusions = None
        self._vehicle_score = None

    @property
    def buyback_auth(self):
        return self._buyback_auth

    @buyback_auth.setter
    def buyback_auth(self, value):
        self._buyback_auth = value
    @property
    def report_origin_code(self):
        return self._report_origin_code

    @report_origin_code.setter
    def report_origin_code(self, value):
        self._report_origin_code = value
    @property
    def vehicle_check_detail(self):
        return self._vehicle_check_detail

    @vehicle_check_detail.setter
    def vehicle_check_detail(self, value):
        if isinstance(value, list):
            self._vehicle_check_detail = list()
            for i in value:
                if isinstance(i, VehicleCheckDetailItem):
                    self._vehicle_check_detail.append(i)
                else:
                    self._vehicle_check_detail.append(VehicleCheckDetailItem.from_alipay_dict(i))
    @property
    def vehicle_check_url(self):
        return self._vehicle_check_url

    @vehicle_check_url.setter
    def vehicle_check_url(self, value):
        self._vehicle_check_url = value
    @property
    def vehicle_exclusions(self):
        return self._vehicle_exclusions

    @vehicle_exclusions.setter
    def vehicle_exclusions(self, value):
        if isinstance(value, list):
            self._vehicle_exclusions = list()
            for i in value:
                self._vehicle_exclusions.append(i)
    @property
    def vehicle_score(self):
        return self._vehicle_score

    @vehicle_score.setter
    def vehicle_score(self, value):
        self._vehicle_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyback_auth:
            if hasattr(self.buyback_auth, 'to_alipay_dict'):
                params['buyback_auth'] = self.buyback_auth.to_alipay_dict()
            else:
                params['buyback_auth'] = self.buyback_auth
        if self.report_origin_code:
            if hasattr(self.report_origin_code, 'to_alipay_dict'):
                params['report_origin_code'] = self.report_origin_code.to_alipay_dict()
            else:
                params['report_origin_code'] = self.report_origin_code
        if self.vehicle_check_detail:
            if isinstance(self.vehicle_check_detail, list):
                for i in range(0, len(self.vehicle_check_detail)):
                    element = self.vehicle_check_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_check_detail[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_check_detail, 'to_alipay_dict'):
                params['vehicle_check_detail'] = self.vehicle_check_detail.to_alipay_dict()
            else:
                params['vehicle_check_detail'] = self.vehicle_check_detail
        if self.vehicle_check_url:
            if hasattr(self.vehicle_check_url, 'to_alipay_dict'):
                params['vehicle_check_url'] = self.vehicle_check_url.to_alipay_dict()
            else:
                params['vehicle_check_url'] = self.vehicle_check_url
        if self.vehicle_exclusions:
            if isinstance(self.vehicle_exclusions, list):
                for i in range(0, len(self.vehicle_exclusions)):
                    element = self.vehicle_exclusions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_exclusions[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_exclusions, 'to_alipay_dict'):
                params['vehicle_exclusions'] = self.vehicle_exclusions.to_alipay_dict()
            else:
                params['vehicle_exclusions'] = self.vehicle_exclusions
        if self.vehicle_score:
            if hasattr(self.vehicle_score, 'to_alipay_dict'):
                params['vehicle_score'] = self.vehicle_score.to_alipay_dict()
            else:
                params['vehicle_score'] = self.vehicle_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckReportData()
        if 'buyback_auth' in d:
            o.buyback_auth = d['buyback_auth']
        if 'report_origin_code' in d:
            o.report_origin_code = d['report_origin_code']
        if 'vehicle_check_detail' in d:
            o.vehicle_check_detail = d['vehicle_check_detail']
        if 'vehicle_check_url' in d:
            o.vehicle_check_url = d['vehicle_check_url']
        if 'vehicle_exclusions' in d:
            o.vehicle_exclusions = d['vehicle_exclusions']
        if 'vehicle_score' in d:
            o.vehicle_score = d['vehicle_score']
        return o


