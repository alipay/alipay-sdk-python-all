#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmepAnnualReportBasicInfo import ZmepAnnualReportBasicInfo
from alipay.aop.api.domain.ZmepAnnualReportInvestInfo import ZmepAnnualReportInvestInfo
from alipay.aop.api.domain.ZmepAnnualReportShareholderInfo import ZmepAnnualReportShareholderInfo
from alipay.aop.api.domain.ZmepAnnualReportWebsiteInfo import ZmepAnnualReportWebsiteInfo


class ZmepAnnualReportInfo(object):

    def __init__(self):
        self._basic_info = None
        self._invest_list = None
        self._public_date = None
        self._report_year = None
        self._shareholder_list = None
        self._website_list = None

    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        if isinstance(value, ZmepAnnualReportBasicInfo):
            self._basic_info = value
        else:
            self._basic_info = ZmepAnnualReportBasicInfo.from_alipay_dict(value)
    @property
    def invest_list(self):
        return self._invest_list

    @invest_list.setter
    def invest_list(self, value):
        if isinstance(value, ZmepAnnualReportInvestInfo):
            self._invest_list = value
        else:
            self._invest_list = ZmepAnnualReportInvestInfo.from_alipay_dict(value)
    @property
    def public_date(self):
        return self._public_date

    @public_date.setter
    def public_date(self, value):
        self._public_date = value
    @property
    def report_year(self):
        return self._report_year

    @report_year.setter
    def report_year(self, value):
        self._report_year = value
    @property
    def shareholder_list(self):
        return self._shareholder_list

    @shareholder_list.setter
    def shareholder_list(self, value):
        if isinstance(value, list):
            self._shareholder_list = list()
            for i in value:
                if isinstance(i, ZmepAnnualReportShareholderInfo):
                    self._shareholder_list.append(i)
                else:
                    self._shareholder_list.append(ZmepAnnualReportShareholderInfo.from_alipay_dict(i))
    @property
    def website_list(self):
        return self._website_list

    @website_list.setter
    def website_list(self, value):
        if isinstance(value, list):
            self._website_list = list()
            for i in value:
                if isinstance(i, ZmepAnnualReportWebsiteInfo):
                    self._website_list.append(i)
                else:
                    self._website_list.append(ZmepAnnualReportWebsiteInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.basic_info:
            if hasattr(self.basic_info, 'to_alipay_dict'):
                params['basic_info'] = self.basic_info.to_alipay_dict()
            else:
                params['basic_info'] = self.basic_info
        if self.invest_list:
            if hasattr(self.invest_list, 'to_alipay_dict'):
                params['invest_list'] = self.invest_list.to_alipay_dict()
            else:
                params['invest_list'] = self.invest_list
        if self.public_date:
            if hasattr(self.public_date, 'to_alipay_dict'):
                params['public_date'] = self.public_date.to_alipay_dict()
            else:
                params['public_date'] = self.public_date
        if self.report_year:
            if hasattr(self.report_year, 'to_alipay_dict'):
                params['report_year'] = self.report_year.to_alipay_dict()
            else:
                params['report_year'] = self.report_year
        if self.shareholder_list:
            if isinstance(self.shareholder_list, list):
                for i in range(0, len(self.shareholder_list)):
                    element = self.shareholder_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shareholder_list[i] = element.to_alipay_dict()
            if hasattr(self.shareholder_list, 'to_alipay_dict'):
                params['shareholder_list'] = self.shareholder_list.to_alipay_dict()
            else:
                params['shareholder_list'] = self.shareholder_list
        if self.website_list:
            if isinstance(self.website_list, list):
                for i in range(0, len(self.website_list)):
                    element = self.website_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.website_list[i] = element.to_alipay_dict()
            if hasattr(self.website_list, 'to_alipay_dict'):
                params['website_list'] = self.website_list.to_alipay_dict()
            else:
                params['website_list'] = self.website_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepAnnualReportInfo()
        if 'basic_info' in d:
            o.basic_info = d['basic_info']
        if 'invest_list' in d:
            o.invest_list = d['invest_list']
        if 'public_date' in d:
            o.public_date = d['public_date']
        if 'report_year' in d:
            o.report_year = d['report_year']
        if 'shareholder_list' in d:
            o.shareholder_list = d['shareholder_list']
        if 'website_list' in d:
            o.website_list = d['website_list']
        return o


