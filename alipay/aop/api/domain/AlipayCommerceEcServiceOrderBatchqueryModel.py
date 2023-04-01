#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcServiceOrderBatchqueryModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._buyer_id = None
        self._enterprise_id = None
        self._order_id_list = None
        self._page_num = None
        self._page_size = None
        self._service_id_list = None
        self._service_type_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def order_id_list(self):
        return self._order_id_list

    @order_id_list.setter
    def order_id_list(self, value):
        if isinstance(value, list):
            self._order_id_list = list()
            for i in value:
                self._order_id_list.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def service_id_list(self):
        return self._service_id_list

    @service_id_list.setter
    def service_id_list(self, value):
        if isinstance(value, list):
            self._service_id_list = list()
            for i in value:
                self._service_id_list.append(i)
    @property
    def service_type_list(self):
        return self._service_type_list

    @service_type_list.setter
    def service_type_list(self, value):
        if isinstance(value, list):
            self._service_type_list = list()
            for i in value:
                self._service_type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.order_id_list:
            if isinstance(self.order_id_list, list):
                for i in range(0, len(self.order_id_list)):
                    element = self.order_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_id_list[i] = element.to_alipay_dict()
            if hasattr(self.order_id_list, 'to_alipay_dict'):
                params['order_id_list'] = self.order_id_list.to_alipay_dict()
            else:
                params['order_id_list'] = self.order_id_list
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.service_id_list:
            if isinstance(self.service_id_list, list):
                for i in range(0, len(self.service_id_list)):
                    element = self.service_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_id_list[i] = element.to_alipay_dict()
            if hasattr(self.service_id_list, 'to_alipay_dict'):
                params['service_id_list'] = self.service_id_list.to_alipay_dict()
            else:
                params['service_id_list'] = self.service_id_list
        if self.service_type_list:
            if isinstance(self.service_type_list, list):
                for i in range(0, len(self.service_type_list)):
                    element = self.service_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_type_list[i] = element.to_alipay_dict()
            if hasattr(self.service_type_list, 'to_alipay_dict'):
                params['service_type_list'] = self.service_type_list.to_alipay_dict()
            else:
                params['service_type_list'] = self.service_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcServiceOrderBatchqueryModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'order_id_list' in d:
            o.order_id_list = d['order_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'service_id_list' in d:
            o.service_id_list = d['service_id_list']
        if 'service_type_list' in d:
            o.service_type_list = d['service_type_list']
        return o


