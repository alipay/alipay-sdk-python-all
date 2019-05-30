#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneProdBillDetail import SceneProdBillDetail


class MybankCreditSceneprodBillSyncModel(object):

    def __init__(self):
        self._app_seq_no = None
        self._bill_list = None
        self._cert_name = None
        self._cert_no = None
        self._drawdown_no = None
        self._ext_param = None
        self._org_code = None
        self._out_order_no = None
        self._product_code = None
        self._site = None
        self._site_user_id = None

    @property
    def app_seq_no(self):
        return self._app_seq_no

    @app_seq_no.setter
    def app_seq_no(self, value):
        self._app_seq_no = value
    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, SceneProdBillDetail):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(SceneProdBillDetail.from_alipay_dict(i))
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
        if self.app_seq_no:
            if hasattr(self.app_seq_no, 'to_alipay_dict'):
                params['app_seq_no'] = self.app_seq_no.to_alipay_dict()
            else:
                params['app_seq_no'] = self.app_seq_no
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
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        o = MybankCreditSceneprodBillSyncModel()
        if 'app_seq_no' in d:
            o.app_seq_no = d['app_seq_no']
        if 'bill_list' in d:
            o.bill_list = d['bill_list']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


