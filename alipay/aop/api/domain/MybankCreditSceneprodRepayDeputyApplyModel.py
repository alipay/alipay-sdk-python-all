#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneProdDeputyPaymentBillDetail import SceneProdDeputyPaymentBillDetail


class MybankCreditSceneprodRepayDeputyApplyModel(object):

    def __init__(self):
        self._app_seqno = None
        self._bill_list = None
        self._drawdown_no = None
        self._operation_type = None
        self._org_code = None
        self._product_code = None
        self._site = None
        self._site_user_id = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, SceneProdDeputyPaymentBillDetail):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(SceneProdDeputyPaymentBillDetail.from_alipay_dict(i))
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seqno:
            if hasattr(self.app_seqno, 'to_alipay_dict'):
                params['app_seqno'] = self.app_seqno.to_alipay_dict()
            else:
                params['app_seqno'] = self.app_seqno
        if self.bill_list:
            if isinstance(self.bill_list, list):
                for i in range(0, len(self.bill_list)):
                    element = self.bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_list, 'to_alipay_dict'):
                params['bill_list'] = self.bill_list.to_alipay_dict()
            else:
                params['bill_list'] = self.bill_list
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodRepayDeputyApplyModel()
        if 'app_seqno' in d:
            o.app_seqno = d['app_seqno']
        if 'bill_list' in d:
            o.bill_list = d['bill_list']
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


