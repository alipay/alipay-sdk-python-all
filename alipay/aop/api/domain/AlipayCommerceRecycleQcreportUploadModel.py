#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQcReportCheckItems import RecycleQcReportCheckItems
from alipay.aop.api.domain.RecycleQcReportProductInfo import RecycleQcReportProductInfo
from alipay.aop.api.domain.RecycleQcReportSummaryInfo import RecycleQcReportSummaryInfo


class AlipayCommerceRecycleQcreportUploadModel(object):

    def __init__(self):
        self._check_items = None
        self._merchant_no = None
        self._merchant_report_url = None
        self._openid = None
        self._out_order_id = None
        self._product_info = None
        self._summary = None
        self._user_id = None

    @property
    def check_items(self):
        return self._check_items

    @check_items.setter
    def check_items(self, value):
        if isinstance(value, list):
            self._check_items = list()
            for i in value:
                if isinstance(i, RecycleQcReportCheckItems):
                    self._check_items.append(i)
                else:
                    self._check_items.append(RecycleQcReportCheckItems.from_alipay_dict(i))
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def merchant_report_url(self):
        return self._merchant_report_url

    @merchant_report_url.setter
    def merchant_report_url(self, value):
        self._merchant_report_url = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def product_info(self):
        return self._product_info

    @product_info.setter
    def product_info(self, value):
        if isinstance(value, RecycleQcReportProductInfo):
            self._product_info = value
        else:
            self._product_info = RecycleQcReportProductInfo.from_alipay_dict(value)
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, RecycleQcReportSummaryInfo):
            self._summary = value
        else:
            self._summary = RecycleQcReportSummaryInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_items:
            if isinstance(self.check_items, list):
                for i in range(0, len(self.check_items)):
                    element = self.check_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_items[i] = element.to_alipay_dict()
            if hasattr(self.check_items, 'to_alipay_dict'):
                params['check_items'] = self.check_items.to_alipay_dict()
            else:
                params['check_items'] = self.check_items
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.merchant_report_url:
            if hasattr(self.merchant_report_url, 'to_alipay_dict'):
                params['merchant_report_url'] = self.merchant_report_url.to_alipay_dict()
            else:
                params['merchant_report_url'] = self.merchant_report_url
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.product_info:
            if hasattr(self.product_info, 'to_alipay_dict'):
                params['product_info'] = self.product_info.to_alipay_dict()
            else:
                params['product_info'] = self.product_info
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleQcreportUploadModel()
        if 'check_items' in d:
            o.check_items = d['check_items']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'merchant_report_url' in d:
            o.merchant_report_url = d['merchant_report_url']
        if 'openid' in d:
            o.openid = d['openid']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'product_info' in d:
            o.product_info = d['product_info']
        if 'summary' in d:
            o.summary = d['summary']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


