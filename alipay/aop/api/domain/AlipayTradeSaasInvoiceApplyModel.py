#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceBuyerInfo import InvoiceBuyerInfo
from alipay.aop.api.domain.InvoiceDeliverInfo import InvoiceDeliverInfo
from alipay.aop.api.domain.InvoiceIssuerInfo import InvoiceIssuerInfo
from alipay.aop.api.domain.InvoiceProductItemInfo import InvoiceProductItemInfo
from alipay.aop.api.domain.InvoiceMainInfo import InvoiceMainInfo
from alipay.aop.api.domain.InvoiceRemarkInfo import InvoiceRemarkInfo
from alipay.aop.api.domain.InvoiceSellerInfo import InvoiceSellerInfo
from alipay.aop.api.domain.InvoicePaymentInfo import InvoicePaymentInfo
from alipay.aop.api.domain.RedRelatedInvoiceInfo import RedRelatedInvoiceInfo


class AlipayTradeSaasInvoiceApplyModel(object):

    def __init__(self):
        self._invoice_buyer_info = None
        self._invoice_deliver_info = None
        self._invoice_issuer_info = None
        self._invoice_items = None
        self._invoice_main_info = None
        self._invoice_mode = None
        self._invoice_remark_info = None
        self._invoice_seller_info = None
        self._order_list = None
        self._out_request_no = None
        self._red_related_invoice_info = None

    @property
    def invoice_buyer_info(self):
        return self._invoice_buyer_info

    @invoice_buyer_info.setter
    def invoice_buyer_info(self, value):
        if isinstance(value, InvoiceBuyerInfo):
            self._invoice_buyer_info = value
        else:
            self._invoice_buyer_info = InvoiceBuyerInfo.from_alipay_dict(value)
    @property
    def invoice_deliver_info(self):
        return self._invoice_deliver_info

    @invoice_deliver_info.setter
    def invoice_deliver_info(self, value):
        if isinstance(value, InvoiceDeliverInfo):
            self._invoice_deliver_info = value
        else:
            self._invoice_deliver_info = InvoiceDeliverInfo.from_alipay_dict(value)
    @property
    def invoice_issuer_info(self):
        return self._invoice_issuer_info

    @invoice_issuer_info.setter
    def invoice_issuer_info(self, value):
        if isinstance(value, InvoiceIssuerInfo):
            self._invoice_issuer_info = value
        else:
            self._invoice_issuer_info = InvoiceIssuerInfo.from_alipay_dict(value)
    @property
    def invoice_items(self):
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, value):
        if isinstance(value, list):
            self._invoice_items = list()
            for i in value:
                if isinstance(i, InvoiceProductItemInfo):
                    self._invoice_items.append(i)
                else:
                    self._invoice_items.append(InvoiceProductItemInfo.from_alipay_dict(i))
    @property
    def invoice_main_info(self):
        return self._invoice_main_info

    @invoice_main_info.setter
    def invoice_main_info(self, value):
        if isinstance(value, InvoiceMainInfo):
            self._invoice_main_info = value
        else:
            self._invoice_main_info = InvoiceMainInfo.from_alipay_dict(value)
    @property
    def invoice_mode(self):
        return self._invoice_mode

    @invoice_mode.setter
    def invoice_mode(self, value):
        self._invoice_mode = value
    @property
    def invoice_remark_info(self):
        return self._invoice_remark_info

    @invoice_remark_info.setter
    def invoice_remark_info(self, value):
        if isinstance(value, InvoiceRemarkInfo):
            self._invoice_remark_info = value
        else:
            self._invoice_remark_info = InvoiceRemarkInfo.from_alipay_dict(value)
    @property
    def invoice_seller_info(self):
        return self._invoice_seller_info

    @invoice_seller_info.setter
    def invoice_seller_info(self, value):
        if isinstance(value, InvoiceSellerInfo):
            self._invoice_seller_info = value
        else:
            self._invoice_seller_info = InvoiceSellerInfo.from_alipay_dict(value)
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, InvoicePaymentInfo):
                    self._order_list.append(i)
                else:
                    self._order_list.append(InvoicePaymentInfo.from_alipay_dict(i))
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def red_related_invoice_info(self):
        return self._red_related_invoice_info

    @red_related_invoice_info.setter
    def red_related_invoice_info(self, value):
        if isinstance(value, RedRelatedInvoiceInfo):
            self._red_related_invoice_info = value
        else:
            self._red_related_invoice_info = RedRelatedInvoiceInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_buyer_info:
            if hasattr(self.invoice_buyer_info, 'to_alipay_dict'):
                params['invoice_buyer_info'] = self.invoice_buyer_info.to_alipay_dict()
            else:
                params['invoice_buyer_info'] = self.invoice_buyer_info
        if self.invoice_deliver_info:
            if hasattr(self.invoice_deliver_info, 'to_alipay_dict'):
                params['invoice_deliver_info'] = self.invoice_deliver_info.to_alipay_dict()
            else:
                params['invoice_deliver_info'] = self.invoice_deliver_info
        if self.invoice_issuer_info:
            if hasattr(self.invoice_issuer_info, 'to_alipay_dict'):
                params['invoice_issuer_info'] = self.invoice_issuer_info.to_alipay_dict()
            else:
                params['invoice_issuer_info'] = self.invoice_issuer_info
        if self.invoice_items:
            if isinstance(self.invoice_items, list):
                for i in range(0, len(self.invoice_items)):
                    element = self.invoice_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_items[i] = element.to_alipay_dict()
            if hasattr(self.invoice_items, 'to_alipay_dict'):
                params['invoice_items'] = self.invoice_items.to_alipay_dict()
            else:
                params['invoice_items'] = self.invoice_items
        if self.invoice_main_info:
            if hasattr(self.invoice_main_info, 'to_alipay_dict'):
                params['invoice_main_info'] = self.invoice_main_info.to_alipay_dict()
            else:
                params['invoice_main_info'] = self.invoice_main_info
        if self.invoice_mode:
            if hasattr(self.invoice_mode, 'to_alipay_dict'):
                params['invoice_mode'] = self.invoice_mode.to_alipay_dict()
            else:
                params['invoice_mode'] = self.invoice_mode
        if self.invoice_remark_info:
            if hasattr(self.invoice_remark_info, 'to_alipay_dict'):
                params['invoice_remark_info'] = self.invoice_remark_info.to_alipay_dict()
            else:
                params['invoice_remark_info'] = self.invoice_remark_info
        if self.invoice_seller_info:
            if hasattr(self.invoice_seller_info, 'to_alipay_dict'):
                params['invoice_seller_info'] = self.invoice_seller_info.to_alipay_dict()
            else:
                params['invoice_seller_info'] = self.invoice_seller_info
        if self.order_list:
            if isinstance(self.order_list, list):
                for i in range(0, len(self.order_list)):
                    element = self.order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_list[i] = element.to_alipay_dict()
            if hasattr(self.order_list, 'to_alipay_dict'):
                params['order_list'] = self.order_list.to_alipay_dict()
            else:
                params['order_list'] = self.order_list
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.red_related_invoice_info:
            if hasattr(self.red_related_invoice_info, 'to_alipay_dict'):
                params['red_related_invoice_info'] = self.red_related_invoice_info.to_alipay_dict()
            else:
                params['red_related_invoice_info'] = self.red_related_invoice_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasInvoiceApplyModel()
        if 'invoice_buyer_info' in d:
            o.invoice_buyer_info = d['invoice_buyer_info']
        if 'invoice_deliver_info' in d:
            o.invoice_deliver_info = d['invoice_deliver_info']
        if 'invoice_issuer_info' in d:
            o.invoice_issuer_info = d['invoice_issuer_info']
        if 'invoice_items' in d:
            o.invoice_items = d['invoice_items']
        if 'invoice_main_info' in d:
            o.invoice_main_info = d['invoice_main_info']
        if 'invoice_mode' in d:
            o.invoice_mode = d['invoice_mode']
        if 'invoice_remark_info' in d:
            o.invoice_remark_info = d['invoice_remark_info']
        if 'invoice_seller_info' in d:
            o.invoice_seller_info = d['invoice_seller_info']
        if 'order_list' in d:
            o.order_list = d['order_list']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'red_related_invoice_info' in d:
            o.red_related_invoice_info = d['red_related_invoice_info']
        return o


